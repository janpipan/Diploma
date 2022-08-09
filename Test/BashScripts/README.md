First you have to create configuration files for keepalived and haproxy on your node. 


Paths /etc/keepalived/check_apiserver.sh /etc/keepalived/keepalived.conf /etc/haproxy/haproxy.cfg

Create yaml files and place them in /etc/kubernetes/manifests

If you have set haproxy to run on port 6443 you have to bind api server to different port when initializing or adding new master nodes to the cluster

Examples: kubeadm init --control-plane-endpoint=10.177.12.50:6443 --apiserver-bind-port 8443 --pod-network-cidr=10.244.0.0/16 --upload-certs
kubeadm join 10.177.12.50:6443 --token jia77a.vgj638nvzkwmnh52 --discovery-token-ca-cert-hash sha256:ecc4541590cf057197a1c71905a64ff4792322931fd4e9ba0a7ca39692ee7d7e --control-plane --certificate-key d8ab675b08dcc845395d9cf5a45f647fa8a7c62e886b95221a2f0fbf8fbe30bc --apiserver-bind-port 8443

After you have initialized kuberentes cluster you have to deploy cluster network (flannel, calico...)

When cluster network is deployed you can start adding your nodes to the cluster


To immediately schedule new pods on notReady nodes you have to add tolerations to the deployment file. 


Docker installation

docker-ce #installs 

Docker removal

sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

To display taints on node use command 
    kubectl get nodes -o=jsonpath='{range .items[*]}{.metadata.name}{"\n"}{range .spec.taints[*]}{"\t\t"}{.key}{"\n"}'






