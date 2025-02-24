### Overview
The code provided is a Python script that interacts with a Kubernetes cluster. It uses the `subprocess` module to execute `kubectl` commands and manage deployments.

### Functions
#### `run_kubectl_command`
*   **Purpose:** Execute a `kubectl` command using `subprocess`.
*   **Parameters:** `command` (a string representing the `kubectl` command to be executed).
*   **Return Value:** The output of the `kubectl` command as a string.
*   **Error Handling:** If the command fails, it logs an error message and raises a `subprocess.CalledProcessError`.

#### `deploy_deployment`
*   **Purpose:** Deploy a new Kubernetes deployment.
*   **Parameters:**
    *   `deployment_name` (a string representing the name of the deployment).
    *   `image_name` (a string representing the Docker image to be used).
    *   `replicas` (an integer representing the number of replicas to create).
*   **Action:**
    1.  Create a YAML dictionary representing the deployment.
    2.  Write the YAML dictionary to a temporary file.
    3.  Apply the YAML file using `kubectl apply`.
    4.  Log a success message.

#### `delete_deployment`
*   **Purpose:** Delete an existing Kubernetes deployment.
*   **Parameters:** `deployment_name` (a string representing the name of the deployment to delete).
*   **Action:**
    1.  Execute a `kubectl delete` command to delete the deployment.
    2.  Log a success message.

#### `get_deployment_info`
*   **Purpose:** Get information about a specific Kubernetes deployment.
*   **Parameters:** `deployment_name` (a string representing the name of the deployment).
*   **Return Value:** A dictionary representing the deployment information.
*   **Action:**
    1.  Execute a `kubectl get` command to retrieve the deployment information in JSON format.
    2.  Parse the JSON output into a Python dictionary.

#### `view_pods`
*   **Purpose:** List all pods in the cluster.
*   **Action:**
    1.  Execute a `kubectl get` command to retrieve the pods.
    2.  Print the output.

### Example Usage
The script includes an example usage section that demonstrates how to:
1.  Deploy a new deployment named "my-app" using the "nginx:latest" image with 3 replicas.
2.  Retrieve and print information about the "my-app" deployment.
3.  List all pods in the cluster.
4.  Delete the "my-app" deployment.

### Logging
The script uses the `logging` module to log messages at different levels (e.g., INFO, ERROR). The logging level is set to INFO, and the format includes the timestamp, log level, and message.

### Dependencies
The script depends on the following Python modules:
*   `subprocess`
*   `yaml`
*   `json`
*   `logging`