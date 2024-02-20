def email_slicer(email):
    # Split the email address at the '@' character
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    return username, domain


# Main code
if __name__ == "__main__":
    # Input from the user
    email_input = input("Enter your email address: ")

    # Slicing the email
    username, domain = email_slicer(email_input)

    # Output the result
    print(f"Username: {username}")
    print(f"Domain: {domain}")
