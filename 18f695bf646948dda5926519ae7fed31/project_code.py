from kubernetes import client, config

def view_pod(name, namespace="default"):
    config.load_kube_config()
    api = client.CoreV1Api()
    
    # Fetch pod details
    pod = api.read_namespaced_pod(name=name, namespace=namespace)
    pod_status = pod.status.phase
    pod_ip = pod.status.pod_ip
    pod_node = pod.spec.node_name
    
    # Fetch pod logs
    pod_logs = api.read_namespaced_pod_log(name=name, namespace=namespace)
    
    # Format and display the information
    print(f"Pod Name: {name}")
    print(f"Namespace: {namespace}")
    print(f"Status: {pod_status}")
    print(f"Pod IP: {pod_ip}")
    print(f"Node: {pod_node}")
    print("Logs:")
    print(pod_logs)

# Example usage
# view_pod("my-pod", "default")
