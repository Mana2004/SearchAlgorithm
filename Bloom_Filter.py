import hashlib
import time

class Bloom_Filter:
    def __init__(self, file_path):  
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return usernames

    def bloom_filter_search(self, target_username):
        start_time = time.time()

        usernames = self.read_file()
        hash_function = 5  
        array_size = 1000  
        array = [False] * array_size
        index_list = []  

        for i in range(hash_function):
            for username in usernames:
                seed = i + 1
                combined_data = f"{username}{seed}".encode('utf-8')  
                username_hash = hashlib.sha256(combined_data).hexdigest()
                hash_int = int(username_hash, 16)
                index = hash_int % array_size
                array[index] = True
                index_list.append(index)

        target_indexes = []
        found_false = False

        for i in range(hash_function):
            seed = i + 1
            combined_data = f"{target_username}{seed}".encode('utf-8')  
            target_username_hash = hashlib.sha256(combined_data).hexdigest()
            hash_int = int(target_username_hash, 16)
            index = hash_int % array_size
            target_indexes.append(index)

            if not array[index]:
                found_false = True
        
        if found_false:
            print(f"{target_username} is definitely not in the set.")
            return False, f"{time.time() - start_time:.4f} seconds"
        else:
            print(f"{target_username} might be in the set.")
            return True, f"{time.time() - start_time:.4f} seconds"