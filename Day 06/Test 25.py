"""Day 06 EXCEPTION HANDLING """

# Write a Python function process_input(data) that takes a string data as input and performs the following actions:
# 1. If the string is empty, return the message "Error: Empty input provided.".
# 2. If the string exceeds 255 characters, return the message "Error: Input exceeds maximum length.".
# 3. If the string contains any numeric characters, return the message "Error: Input contains invalid characters.".
# 4. If none of the above conditions apply, return the message "Input processed successfully.".
# Program should handle all above scenarios by raising a CustomError 
# Finally, ensure the message "Program execution completed." is always printed.

# Constraint
# data is a string with a maximum length of 255 characters.

class CustomError(Exception):
    pass
    
def process_input(data):
    try:
        if not data:
            raise CustomError("Error: Empty input provided")

    
        if len(data)>255:
            raise CustomError("Error: Input exceeds maximum length")

        if any(char.isdigit() for char in data):
            raise CustomError("Error: Input contains invalid characters")

        return "input processed successfully"

    except CustomError as e:
        return str(e)
    finally:
        print("Program execution completed")



