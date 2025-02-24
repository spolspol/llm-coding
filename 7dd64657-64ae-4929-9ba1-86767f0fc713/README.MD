# Application Overview

This application is a simple console-based login page that prompts the user to enter a username and password. It validates the credentials against predefined values and grants access upon successful authentication. The application uses a `Scanner` for input and a custom `Authenticate` class for validation.

## Features

- User input for username and password.
- Authentication logic to validate credentials.
- Infinite loop for repeated login attempts until successful.

## Output Documentation

When the application runs, it will display the following output:

1. A greeting message: "Hi, this is a sample code of login page."
2. Prompts for username and password.
3. Authentication result: "successful login" if credentials are correct, or "fail to login" if they are incorrect.

## Installation and Configuration

### Prerequisites

- Java Development Kit (JDK) installed on your system. You can download it from the official Oracle website or use an open-source alternative like OpenJDK.
- An Integrated Development Environment (IDE) like IntelliJ IDEA, Eclipse, or a simple text editor like Visual Studio Code.

### Steps to Install and Configure

1. **Clone or Download the Project:**
   - If you have the project in a version control system like Git, clone the repository to your local machine.
   - Alternatively, download the project files and extract them to a directory of your choice.

2. **Set Up the Project in Your IDE:**
   - Open your IDE and create a new Java project.
   - Import the project files into your IDE. Ensure that the package structure (`com.company`) is correctly set up.

3. **Install Necessary Libraries:**
   - The application uses the `java.util.Scanner` class for input. This is part of the standard Java library, so no additional installation is required.

4. **Configure the Environment:**
   - Ensure that your IDE is configured to use the correct JDK version.
   - Set the `Main` class as the entry point of the application.

5. **Run the Application:**
   - Compile and run the `Main` class. The application will start, and you will see the initial greeting message followed by prompts for username and password.

### Notes

- The current implementation uses hardcoded credentials (`admin` and `password`). In a real-world scenario, these should be stored securely, such as in a database or a secure configuration file.
- The application uses an infinite loop for login attempts. Consider adding a limit to the number of attempts for security purposes.
- Ensure that the `Authenticate` class is in the same package as the `Main` class (`com.company`) or adjust the import statements accordingly.

## Running the Application

To run the application, simply execute the `Main` class. You will be prompted to enter a username and password. Enter the predefined credentials (`admin` and `password`) to successfully log in. If the credentials are incorrect, you will be prompted to try again.