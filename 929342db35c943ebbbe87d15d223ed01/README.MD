## Overview
This is a Python script that utilizes the Kubernetes API to manage pods. The script provides functions to create, delete, and update pods in a Kubernetes cluster.

### Importing Libraries
The script begins by importing the necessary libraries:
* `client` and `config` from `kubernetes` to interact with the Kubernetes API
* `json` for handling JSON data (although it's not used in this script)
* `logging` to handle logging messages

### Logging Setup
The script sets up logging with the following configuration:
* Logging level: `INFO`
* Log format: `%(asctime)s - %(levelname)s - %(message)s`

### Functions
The script defines four main functions:

#### load_kube_config
 Loads the Kubernetes configuration from the default location.
* If the configuration cannot be loaded, an error message is logged and the exception is re-raised.

#### create_pod
 Creates a new pod in the specified namespace.
* Args:
	+ `namespace` (str): The namespace to create the pod in.
	+ `pod_name` (str): The name of the pod.
	+ `container_image` (str): The container image to use for the pod.
* Creates a pod manifest with the specified name and image, and uses the `CoreV1Api` to create the pod.
* Logs a success message if the pod is created successfully, or an error message if an exception occurs.

#### delete_pod
 Deletes a pod from the specified namespace.
* Args:
	+ `namespace` (str): The namespace to delete the pod from.
	+ `pod_name` (str): The name of the pod to delete.
* Uses the `CoreV1Api` to delete the pod.
* Logs a success message if the pod is deleted successfully, or an error message if an exception occurs.

#### update_pod
 Updates the image of a pod in the specified namespace.
* Args:
	+ `namespace` (str): The namespace where the pod resides.
	+ `pod_name` (str): The name of the pod to update.
	+ `new_image` (str): The new container image to use.
* Creates a patch with the new image and uses the `CoreV1Api` to update the pod.
* Logs a success message if the pod is updated successfully, or an error message if an exception occurs.

### Main Function
The `main` function demonstrates pod management by:
1. Loading the Kubernetes configuration.
2. Creating a pod with the `nginx:latest` image.
3. Updating the pod to use the `nginx:alpine` image.
4. Deleting the pod.

### Example Output
If the script runs successfully, the output will look like this:
```
2023-12-01 12:00:00,000 - INFO - Pod 'test-pod' created successfully.
2023-12-01 12:00:00,000 - INFO - Pod 'test-pod' updated successfully.
2023-12-01 12:00:00,000 - INFO - Pod 'test-pod' deleted successfully.
```
If an error occurs during pod creation, update, or deletion, an error message will be logged with the exception details.