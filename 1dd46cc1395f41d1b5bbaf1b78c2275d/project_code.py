# Project Planning (Example using a simple task list)

project_plan = {
    "Project Name": "Example Software Project",
    "Start Date": "2023-10-27",
    "End Date": "2024-03-27",
    "Milestones": [
        {"name": "Design Phase Complete", "date": "2023-11-15"},
        {"name": "Implementation Phase Complete", "date": "2024-01-15"},
        {"name": "Testing Phase Complete", "date": "2024-02-15"},
        {"name": "Deployment", "date": "2024-03-01"},
    ],
    "Tasks": [
        {"name": "Gather Requirements", "status": "completed", "responsible": "John Doe"},
         {"name": "Create System Architecture design", "status": "completed", "responsible": "John Doe, Emma Smith"},
        {"name": "Design Database Schema", "status": "completed", "responsible": "Jane Smith"},
        {"name": "Develop Module A", "status": "in progress", "responsible": "David Lee"},
        {"name": "Develop Module B", "status": "todo", "responsible": "Alice Brown"},
        {"name": "Integrate Modules", "status": "todo", "responsible": "David Lee, Alice Brown"},
        {"name": "Perform Unit Testing", "status": "todo", "responsible": "QA Team"},
        {"name": "Perform Integration Testing", "status": "todo", "responsible": "QA Team"},
        {"name": "Create User Documentation", "status": "todo", "responsible": "Technical Writer"},
        {"name": "Deploy to Staging", "status": "todo", "responsible": "DevOps Team"},
        {"name": "Deploy to Production", "status": "todo", "responsible": "DevOps Team"},
    ],
}


# Design and Architecture (Example using a simple class diagram)

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def get_profile(self):
        return f"User: {self.username}, Email: {self.email}"


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: {self.price}"


class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def get_order_summary(self):
        product_names = ", ".join(product.name for product in self.products)
        return f"Order ID: {self.id}, User: {self.user.username}, Products: {product_names}, Total: {self.total_amount}"



# Implementation (Example continuing from the design)

def create_sample_data():
    user1 = User(1, "john_doe", "john@example.com")
    user2 = User(2, "jane_smith", "jane@example.com")

    product1 = Product(101, "Laptop", 1200)
    product2 = Product(102, "Mouse", 25)
    product3 = Product(103, "Keyboard", 75)

    order1 = Order(1001, user1, [product1, product2])
    order2 = Order(1002, user2, [product2, product3])
    
    return user1, user2, product1, product2, product3, order1, order2


# Testing and Quality Assurance (Example using unittest)

import unittest

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = User(1, "test_user", "test@example.com")
        self.product1 = Product(1, "Test Product 1", 10)
        self.product2 = Product(2, "Test Product 2", 20)
        self.order = Order(1, self.user, [self.product1, self.product2])

    def test_calculate_total(self):
        self.assertEqual(self.order.calculate_total(), 30)

    def test_get_order_summary(self):
        expected_summary = "Order ID: 1, User: test_user, Products: Test Product 1, Test Product 2, Total: 30"
        self.assertEqual(self.order.get_order_summary(), expected_summary)

    def test_user_profile(self):
        self.assertEqual(self.user.get_profile(), "User: test_user, Email: test@example.com")    
    def test_product_details(self):
         self.assertEqual(self.product1.get_details(), "Product: Test Product 1, Price: 10")



# Documentation and Knowledge Base (Example -  function documentation)

def process_order(order):
    """
    Processes an order and updates the inventory.

    Args:
        order (Order): The order object to be processed.

    Returns:
        bool: True if the order was processed successfully, False otherwise.

    Raises:
        ValueError: If the order is invalid or the inventory is insufficient.
    """
    try:
        if not isinstance(order, Order):
            raise ValueError("Invalid order object provided.")
        
        # Simulate inventory check and update
        print(f"Processing order {order.id}...")
        # Add more complex logic here (e.g., database updates, API calls)
        print(f"Order {order.id} processed successfully.")
        return True
    except ValueError as e:
        print(f"Error processing order: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

#  Deployment and Maintenance.  (Example using a simplified deployment script)
def deploy():
    """Simulates a deployment process."""
    print("Starting deployment...")
    print("1. Building application...")
    print("2. Running tests...")
    # In a real-world scenario, you'd run your test suite here (unittest, pytest, etc.)
    print("3. Deploying to staging environment...")
    print("4. Running integration tests in staging...")
    print("5. Deploying to production environment...")
    print("Deployment complete.")



# Release and Feedback - (Example - Simulating feedback collection)

def collect_feedback():
    """Simulates collecting user feedback."""
    feedback = input("Please provide your feedback on the latest release: ")
    print(f"Thank you for your feedback: {feedback}")
    # Here you'd save the feedback to a database, file, or send it to a feedback service.
    return feedback

# Monitoring and Improvement  (Example - simulating logging and metrics)

import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_monitoring():
    """Simulates monitoring application metrics."""
    logging.info("Starting monitoring...")
    for i in range(5):
        #Simulate some work, errors and metric recording.
        time.sleep(1)
        logging.info(f"Application running... iteration {i+1}")
        if i == 2:
             logging.warning("Potential performance bottleneck detected.")
        if i == 3:
            try:
               1 / 0  # Simulate an error
            except ZeroDivisionError:
               logging.error("Critical error: Division by zero.")


    logging.info("Monitoring complete.")


if __name__ == "__main__":
    print("--- Project Planning ---")
    print(project_plan)

    print("\n--- Design and Architecture (Sample Data) ---")
    user1, user2, product1, product2, product3, order1, order2 = create_sample_data()
    print(user1.get_profile())
    print(order1.get_order_summary())
    print(order2.get_order_summary())
    

    print("\n--- Testing ---")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOrder)
    unittest.TextTestRunner(verbosity=2).run(suite)

    print("\n--- Documentation ---")
    help(process_order)  # Show the docstring
    processed = process_order(order1)


    print("\n--- Deployment ---")
    deploy()
    
    print("\n--- Release and Feedback ---")
    collect_feedback()

    print("\n--- Monitoring ---")
    simulate_monitoring()

