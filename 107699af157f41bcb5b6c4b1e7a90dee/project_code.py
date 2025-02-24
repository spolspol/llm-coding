# Import necessary libraries
import kubernetes
from kubernetes import client, config

# Load the kube config
config.load_kube_config()

# Initialize the Kubernetes API client
v1 = client.CoreV1Api()

# Function to list all namespaces
def list_namespaces():
    ret = v1.list_namespace()
    for i in ret.items:
        print(i.metadata.name)

# Function to create a namespace
def create_namespace(name):
    namespace = client.V1Namespace(metadata=client.V1ObjectMeta(name=name))
    v1.create_namespace(namespace)

# Function to delete a namespace
def delete_namespace(name):
    v1.delete_namespace(name)

# Function to list all pods in a namespace
def list_pods(namespace):
    ret = v1.list_namespaced_pod(namespace)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

# Function to create a pod
def create_pod(namespace, pod_name, image):
    container = client.V1Container(
        name=pod_name,
        image=image
    )
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": pod_name}),
        spec=client.V1PodSpec(containers=[container])
    )
    spec = client.V1PodSpec(containers=[container])
    pod = client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=client.V1ObjectMeta(name=pod_name),
        spec=spec
    )
    v1.create_namespaced_pod(namespace, pod)

# Function to delete a pod
def delete_pod(namespace, pod_name):
    v1.delete_namespaced_pod(pod_name, namespace)

# Example usage
if __name__ == "__main__":
    list_namespaces()
    create_namespace("test-namespace")
    list_pods("default")
    create_pod("default", "test-pod", "nginx")
    delete_pod("default", "test-pod")
    delete_namespace("test-namespace")
