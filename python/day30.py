"""
Question:

1. You are tasked with processing a list of user data that contains the user's name, age, and email. The program should:
2. Process the data using a decorator.
3. Use a context manager for managing some process (like handling resources, here we simulate it).
4. Create a custom class to handle the user data.
"""

import functools
from contextlib import contextmanager

# 1. Dummy data directly in a list of dictionaries
users_data = [
    {"name": "John", "age": 25, "email": "john@example.com"},
    {"name": "Jane", "age": 30, "email": "jane@example.com"},
    {"name": "Dave", "age": 22, "email": "dave@example.com"},
    {"name": "Alice", "age": 28, "email": "alice@example.com"},
    {"name": "Bob", "age": 35, "email": "bob@example.com"}
]

# 2. Decorator to modify how data is processed
def data_processor_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Processing data...")
        result = func(*args, **kwargs)
        print("Data processed successfully!")
        return result
    return wrapper

# 3. Context manager to simulate resource handling (for example, processing a resource)
@contextmanager
def process_resource():
    print("Starting resource processing...")
    yield
    print("Resource processing completed.")

# 4. Custom class to handle user data
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = int(age)
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

# 5. Main logic to read, process and calculate average age
class UserManager:
    @data_processor_decorator
    def read_users(self, data):
        users = []
        for user_data in data:
            user = User(user_data['name'], user_data['age'], user_data['email'])
            users.append(user)
        return users
    
    def calculate_average_age(self, users):
        total_age = sum(user.age for user in users)
        return total_age / len(users) if users else 0

    def display_users(self, users):
        for user in users:
            print(user)

# 6. Execute the code
if __name__ == "__main__":
    user_manager = UserManager()

    # Using the context manager to simulate resource processing
    with process_resource():
        # Read the users from the in-memory data
        users = user_manager.read_users(users_data)
        
        # Display user details
        print("\nUsers List:")
        user_manager.display_users(users)
        
        # Calculate and display the average age
        avg_age = user_manager.calculate_average_age(users)
        print(f"\nAverage Age of Users: {avg_age:.2f}")
