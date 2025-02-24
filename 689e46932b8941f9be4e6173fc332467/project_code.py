import subprocess
import yaml
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_kubectl_command(command):
    """Helper function to run kubectl commands."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {e.stderr}")
        raise

def deploy_deployment(deployment_name, image_name, replicas):
    """Deploy a new Kubernetes deployment."""
    deployment_yaml = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": deployment_name},
        "spec": {
            "replicas": replicas,
            "selector": {"matchLabels": {"app": deployment_name}},
            "template": {
                "metadata": {"labels": {"app": deployment_name}},
                "spec": {
                    "containers": [{"name": deployment_name, "image": image_name}]
                }
            }
        }
    }

    # Write YAML to a temporary file
    with open(f"{deployment_name}.yaml", "w") as file:
        yaml.dump(deployment_yaml, file)

    # Apply the YAML file
    run_kubectl_command(f"kubectl apply -f {deployment_name}.yaml")
    logging.info(f"Deployment '{deployment_name}' deployed successfully.")

def delete_deployment(deployment_name):
    """Delete an existing Kubernetes deployment."""
    run_kubectl_command(f"kubectl delete deployment {deployment_name}")
    logging.info(f"Deployment '{deployment_name}' deleted successfully.")

def get_deployment_info(deployment_name):
    """Get information about a specific Kubernetes deployment."""
    output = run_kubectl_command(f"kubectl get deployment {deployment_name} -o json")
    return json.loads(output)

def view_pods():
    """List all pods in the cluster."""
    output = run_kubectl_command("kubectl get pods")
    print(output)

if __name__ == "__main__":
    # Example usage
    try:
        # Deploy a new deployment
        deploy_deployment("my-app", "nginx:latest", 3)
        
        # View information about the deployment
        deployment_info = get_deployment_info("my-app")
        print("Deployment Info:", deployment_info)

        # View all pods
        view_pods()

        # Delete the deployment
        delete_deployment("my-app")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
