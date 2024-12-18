class Algorithm:
    def __init__(self, file_path):  # Corrected constructor name
        self.file_path = file_path

    def linear_search(self, target_username):
        with open(self.file_path, 'r') as file:
            line_number = 0  # Use a separate variable for line numbers
            for line in file:
                line_number += 1  # Increment the line number
                username = line.strip()  # Strip whitespace from the line
                if username == target_username:
                    return line_number  # Return the line number where the username is found
        return -1  # Return -1 if the username is not found
