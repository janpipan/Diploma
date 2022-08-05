#!/bin/bash 

#docker installation following the instructions on https://docs.docker.com/engine/install/ubuntu/

apt update
apt install -y ca-certificates curl gnupg lsb-release

mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update
apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

systemctl start docker
systemctl start containerd

# comment line starting with disabled plugins in /etc/containerd/config to enable cri

sed -i '/^disabled_plugins/ s/./#&/' /etc/containerd/config.toml

# kubeadm, kubelet and kubectl installation following the instructions on https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/

apt update
apt install -y apt-transport-https

curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list

apt update
apt install -y kubelet kubeadm kubectl
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

# disable swap

swapoff -a

# permanently disable swap

sed -i '/^\/swap.img/ s/./#&/' /etc/fstab