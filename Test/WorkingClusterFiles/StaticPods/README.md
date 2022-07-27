Deploy docker and kuberenetes on your first master node

/bin/bash kubeDocker.sh

Configure and save keepAlived and Haproxy configuration files on your node

/etc/haproxy/haproxy.cfg
/etc/keepalived/check_apiserver.sh
/etc/keepalived/keepalived.conf

Create pod yaml files for keepAlived and Haproxy and save them to the kuberenets manifest files

/etc/kubernetes/haproxy.yaml
/etc/kubernetes/keepalived.yaml

Initialize kuberentes cluster with command

kubeadm init --control-plane-endpoint=10.177.12.50:6443 --apiserver-bind-port 8443 --pod-network-cidr=10.244.0.0/16 --upload-certs



