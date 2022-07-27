#!/bin/bash

#get ip address for kubernetes network

# latest working script 

while getopts ":n:s:v:" options; do
    case "${options}" in
        n) net=${OPTARG};;
        s) sub=${OPTARG};;
        v) version=${OPTARG};;
    esac
done

resultNet=`echo $net | awk -F"\." ' $1 <=255 && $2 <= 255 && $3 <= 255 && $4 <= 255 '`
echo $resultNet

if (($sub > 0 && $sub < 31));
then
  networkCIDR=`echo $resultNet/$sub`
fi


#docker installation

apt update
apt install docker.io

#kubernetes installation

apt update
apt install -y apt-transport-https ca-certificates curl
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt update
if ! [ -z "$version" ]
then
    version="="$version"-00"
fi
apt install -qy kubelet$version kubeadm$version kubectl$version --allow-downgrades
apt-mark hold kubelet kubeadm kubectl

touch /etc/docker/daemon.json
cat > /etc/docker/daemon.json <<EOF
{
    "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF
systemctl daemon-reload
systemctl restart docker
systemctl restart kubelet

swapoff -a

kubeadm init --pod-network-cidr=$networkCIDR | tee outputFile.txt

#generates file that installs docker, kubernetes and joins the kubernetes network

touch kubernetesWorker.sh
cat > kubernetesWorker.sh <<EOF
#!/bin/bash 

#docker installation

apt update
apt install docker.io

#kubernetes installation

apt update
apt install -y apt-transport-https ca-certificates curl
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt update
apt install -qy kubelet$version kubeadm$version kubectl$version --allow-downgrades
apt-mark hold kubelet kubeadm kubectl

touch /etc/docker/daemon.json
cat > /etc/docker/daemon.json <<FEND
{
    "exec-opts": ["native.cgroupdriver=systemd"]
}
FEND
systemctl daemon-reload
systemctl restart docker
systemctl restart kubelet

swapoff -a
EOF
grep "kubeadm join" outputFile.txt >> kubernetesWorker.sh 
grep discovery-token-ca-cert-hash outputFile.txt >> kubernetesWorker.sh

rm -r outputFile.txt

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
chmod -R a+rw $HOME/.kube/config

# calico installation

kubectl create -f https://projectcalico.docs.tigera.io/manifests/tigera-operator.yaml

curl https://projectcalico.docs.tigera.io/manifests/custom-resources.yaml > calico.yaml

sed -i "s|192.168.0.0/16|$networkCIDR|g" calico.yaml

kubectl create -f calico.yaml

rm -r calico.yaml

# untaint nodes so that they can schedule pods 

#kubectl taint nodes --all node-role.kubernetes.io/master-
#kubectl taint nodes --all  node-role.kubernetes.io/control-plane:NoSchedule-

# enable port 6443 

ufw allow 6443