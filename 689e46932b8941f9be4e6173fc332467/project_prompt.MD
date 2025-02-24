[prompt] Here is a set of instructions for building a script to manage Kubernetes deployments and pods:

**Script Requirements**

* The script should be able to deploy a new Kubernetes deployment and pod
* The script should be able to delete an existing Kubernetes deployment and pod
* The script should be able to view information about existing Kubernetes deployments and pods

**Step 1: Set up the Environment**

1. Install kubectl (Kubernetes command-line tool) on your machine
2. Configure kubectl to connect to your desired Kubernetes cluster

**Step 2: Define Deployment and Pod Functions**

1. Write a function `deploy_deployment` that takes in parameters:
	* deployment_name: The name of the deployment to be deployed
	* image_name: The name of the Docker image to use for the deployment
	* replicas: The number of replicas to create for the deployment
2. Write a function `delete_deployment` that takes in the parameter `deployment_name`
3. Write a function `get_deployment_info` that takes in the parameter `deployment_name` and returns information about the deployment (e.g. status, pods, etc.)
4. Write a function `view_pods` that lists all pods in the cluster

**Step 3: Implement Deployment Functionality**

1. In the `deploy_deployment` function:
	* Create a new YAML file for the deployment using the provided parameters
	* Apply the YAML file to create the deployment and pods
	* Verify the deployment is created successfully
2. In the `delete_deployment` function:
	* Delete the specified deployment using kubectl
	* Verify the deployment is deleted successfully

**Step 4: Implement Viewing Functionality**

1. In the `get_deployment_info` function:
	* Use kubectl to get information about the specified deployment (e.g. status, pods, etc.)
	* Return the obtained information
2. In the `view_pods` function:
	* Use kubectl to list all pods in the cluster
	* Print the list of pods

**Step 5: Test the Script**

1. Run the script with various parameters (e.g. different deployment names, images, and replica counts) to test its functionality
2. Verify that the script can successfully deploy, delete, and view information about Kubernetes deployments and pods

**Additional Tips**

* Consider adding error handling and logging to your script to improve robustness and debugging capabilities
* You may want to use a scripting language like Python or Bash for this task, as they have built-in support for working with YAML files and command-line tools like kubectl.