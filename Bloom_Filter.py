import hashlib
import time

class Bloom_Filter:
    #intializing the requirements
    def __init__(self, file_path):
        self.file_path = file_path
        self.array_size = 1000  
        self.hash_function_count = 5  
        self.array = [False] * self.array_size
        self.usernames = {}
        self.build_bloom_filter()

    #reads usernames.txt file
    def read_file(self):
        with open(self.file_path, 'r') as file:
            return [line.strip() for line in file]

    #creates the bloom filter also stores line numbers in a dictionary
    def build_bloom_filter(self):
        usernames = self.read_file()
        line_number = 0  
        for username in usernames:
            self.usernames[username] = line_number  
            for i in range(self.hash_function_count):
                seed = i + 1
                combined_data = f"{username}{seed}".encode('utf-8')  
                username_hash = hashlib.sha256(combined_data).hexdigest()
                hash_int = int(username_hash, 16)
                index = hash_int % self.array_size
                self.array[index] = True
            line_number += 1  

    #creates target username hash then checks if those indexes doesn't exist
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
        
    #even if one index exists the target username is probably in the list
        if found_false:
            return -1, f"{time.perf_counter() - start_time:.10f} seconds"  
        else:
            line_number = self.usernames.get(target_username)
            return line_number, f"{time.perf_counter() - start_time:.10f} seconds"

