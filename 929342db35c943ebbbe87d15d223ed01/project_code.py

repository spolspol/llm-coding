from kubernetes import client, config
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_kube_config():
    """
    Loads the Kubernetes configuration from the default location.
    """
    try:
        config.load_kube_config()
    except Exception as e:
        logging.error(f"Failed to load kubeconfig: {e}")
        raise

def create_pod(namespace, pod_name, container_image):
    """
    Creates a new pod in the specified namespace.

    Args:
        namespace (str): The namespace to create the pod in.
        pod_name (str): The name of the pod.
        container_image (str): The container image to use for the pod.
    """
    try:
        api_instance = client.CoreV1Api()
        pod_manifest = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {"name": pod_name},
            "spec": {
                "containers": [{"name": pod_name, "image": container_image}]
            },
        }
        api_instance.create_namespaced_pod(namespace, pod_manifest)
        logging.info(f"Pod '{pod_name}' created successfully.")
    except Exception as e:
        logging.error(f"Failed to create pod: {e}")
        raise

def delete_pod(namespace, pod_name):
    """
    Deletes a pod from the specified namespace.

    Args:
        namespace (str): The namespace to delete the pod from.
        pod_name (str): The name of the pod to delete.
    """
    try:
        api_instance = client.CoreV1Api()
        api_instance.delete_namespaced_pod(pod_name, namespace)
        logging.info(f"Pod '{pod_name}' deleted successfully.")
    except Exception as e:
        logging.error(f"Failed to delete pod: {e}")
        raise

def update_pod(namespace, pod_name, new_image):
    """
    Updates the image of a pod in the specified namespace.

    Args:
        namespace (str): The namespace where the pod resides.
        pod_name (str): The name of the pod to update.
        new_image (str): The new container image to use.
    """
    try:
        api_instance = client.CoreV1Api()
        patch = {"spec": {"containers": [{"name": pod_name, "image": new_image}]}}
        api_instance.patch_namespaced_pod(pod_name, namespace, patch)
        logging.info(f"Pod '{pod_name}' updated successfully.")
    except Exception as e:
        logging.error(f"Failed to update pod: {e}")
        raise

def main():
    """
    Main function to demonstrate pod management.
    """
    try:
        load_kube_config()
        namespace = "default"
        pod_name = "test-pod"
        container_image = "nginx:latest"

        create_pod(namespace, pod_name, container_image)
        update_pod(namespace, pod_name, "nginx:alpine")
        delete_pod(namespace, pod_name)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
