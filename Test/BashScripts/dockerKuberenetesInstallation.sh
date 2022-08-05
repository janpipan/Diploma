#!/bin/bash

#docker installation

#apt update
#apt install -y docker.io

apt update


#kubernetes installation

apt update
apt install -y apt-transport-https ca-certificates curl
curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt update
apt install -qy kubelet kubeadm kubectl 
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

