from dropper.core import generate_message

if __name__ == "__main__":
    username = input("Enter username: ")
    message = generate_message(username)
    print("\nGenerated Message:\n", message)
