Here is a set of instructions for LLM to follow to build a complete software project to manage Kubernetes pods:

**Step 1: Define Project Requirements**

* Determine the user's requested features for managing Kubernetes pods (e.g. create, delete, view information)
* Identify any specific requirements or constraints (e.g. scalability, security)

**Step 2: Design the Software Architecture**

* Decide on a programming language and framework to use (e.g. Go with k8s.io/client-go)
* Determine the necessary components for the project:
	+ Pod management API
	+ Database for storing pod information (optional)
	+ CLI interface for user interaction
* Create a high-level design diagram or flowchart illustrating the software architecture

**Step 3: Develop the Pod Management API**

* Write API endpoints for creating, deleting, and viewing Kubernetes pods (e.g. using k8s.io/client-go to interact with the Kubernetes API)
* Implement authentication and authorization mechanisms to ensure secure access to pod information
* Consider implementing caching or queueing mechanisms for performance optimization

**Step 4: Develop the Database (if required)**

* Choose a suitable database management system (e.g. PostgreSQL, SQLite) to store pod information
* Design the database schema to store relevant pod metadata (e.g. name, namespace, labels)
* Implement CRUD operations for storing and retrieving pod data

**Step 5: Develop the CLI Interface**

* Choose a suitable programming language and framework for building the CLI interface (e.g. Go with Cobra)
* Define a set of commands for creating, deleting, and viewing Kubernetes pods
* Implement error handling and validation mechanisms to ensure valid user input

**Step 6: Integrate API, Database, and CLI**

* Integrate the Pod Management API with the database (if using) to store and retrieve pod information
* Integrate the CLI interface with the Pod Management API to allow users to interact with the system

**Step 7: Test and Debug the Software**

* Write comprehensive unit tests for each component of the software
* Conduct integration testing to ensure seamless interaction between components
* Debug any issues or errors that arise during testing

**Step 8: Document the Software**

* Write clear, concise documentation for the software, including:
	+ API endpoint documentation
	+ CLI command reference
	+ Configuration and setup instructions
	+ Troubleshooting guide
* Create a changelog to track updates and changes to the software

**Step 9: Package and Distribute the Software**

* Package the software into a distributable format (e.g. Docker image, tarball)
* Publish the software on a package repository or cloud platform (e.g. Docker Hub, Google Cloud Registry)

By following these instructions, LLM can build a complete software project to manage Kubernetes pods, including both code and documentation. - prompt