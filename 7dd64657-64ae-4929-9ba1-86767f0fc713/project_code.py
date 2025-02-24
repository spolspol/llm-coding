javapackage com.company;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hi, this is a sample code of login page."); // Code to print the statement initially

        Scanner scanner = new Scanner(System.in);  // Scanner was not imported initailly
        Authenticate AuthenticateMethod = new Authenticate();

        while (true) { // Infinite loop to take credentials repeatedly

            // Reading username and password from std input
            System.out.print("Enter your username: ");
            String username = scanner.nextLine();

            System.out.print("Enter your password: ");
            String password = scanner.nextLine();

            // Authenticating the user.
            if (AuthenticateMethod.ValidateUser(username, password)) {

                System.out.println("succesful login");
                break; // exiting loop if credentials are correct and we can now have access .

            } else {

                System.out.println("fail to login");
                continue;
            }

        }

    }
}

import java.util.Scanner;
package com.company;

public class Authenticate {

    //these details will be later removed and stored in a database .

    private static final String USERNAME = "admin";
    private static final String PASSWORD = "password";

    public boolean ValidateUser(String username, String password) {
        if (USERNAME != null && USERNAME.equals(username)) {
            // Password comparison only done if username is valid.
            if (PASSWORD != null && PASSWORD.equals(password)) {
                return true;
            }
        }
        return false;
    }

}
