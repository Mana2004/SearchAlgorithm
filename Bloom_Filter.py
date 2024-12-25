import hashlib
import time

class Bloom_Filter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.array_size = 1000  
        self.hash_function_count = 5  
        self.array = [False] * self.array_size
        self.usernames = {}
        self.build_bloom_filter()

    def read_file(self):
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file]

    def build_bloom_filter(self):
        usernames = self.read_file()
        line_number = 0  # Initialize line number counter
        for username in usernames:
            self.usernames[username] = line_number  # Store line number in dictionary
            for i in range(self.hash_function_count):
                seed = i + 1
                combined_data = f"{username}{seed}".encode('utf-8')  
                username_hash = hashlib.sha256(combined_data).hexdigest()
                hash_int = int(username_hash, 16)
                index = hash_int % self.array_size
                self.array[index] = True
            line_number += 1  # Increment line number for each username

    def bloom_filter_search(self, target_username):
        start_time = time.perf_counter()

        found_false = False

        for i in range(self.hash_function_count):
            seed = i + 1
            combined_data = f"{target_username}{seed}".encode('utf-8')  
            target_username_hash = hashlib.sha256(combined_data).hexdigest()
            hash_int = int(target_username_hash, 16)
            index = hash_int % self.array_size

            if not self.array[index]:
                found_false = True
                break
        
        if found_false:
            return None, f"{time.perf_counter() - start_time:.10f} seconds"  # Return None if not found
        else:
            line_number = self.usernames.get(target_username)
            return line_number, f"{time.perf_counter() - start_time:.10f} seconds"

