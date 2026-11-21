"""Demonstrate the login module with a sample account."""

def login(username, password):
    return username == "student" and password == "demo123"


if __name__ == "__main__":
    print("Login successful" if login("student", "demo123") else "Invalid credentials")
