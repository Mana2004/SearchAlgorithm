import hashlib
import time

class Algorithm:
    def __init__(self, file_path):  
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return usernames



    def linear_search(self, target_username):
        start_time = time.time()
        usernames = self.read_file()
        line_number = 0  
        for line in usernames:
            line_number += 1   
            if line == target_username:
                return line_number, f"{time.time() - start_time:.4f} seconds"
        return -1, f"{time.time() - start_time:.4f} seconds"



    def binary_search(self, target_username):
        start_time = time.time()
        usernames = self.read_file()
        sorted_usernames = sorted(usernames, key=lambda s: s.casefold())
        low = 0
        high = len(sorted_usernames) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_username = sorted_usernames[mid]
            if mid_username.casefold() == target_username.casefold():
                return mid + 1, f"{time.time() - start_time:.4f} seconds"
            elif mid_username.casefold() < target_username.casefold():
                low = mid + 1
            else:
                high = mid - 1
        return -1, f"{time.time() - start_time:.4f} seconds"



    #Hash Table
    def optimized_search(self, target_username):
        start_time = time.time()
        usernames = self.read_file()
        hash_table = {}
        for line_number, line in enumerate(usernames, 1):
            username_hash = hashlib.sha256(line.encode()).hexdigest()
            hash_table[username_hash] = line_number
        username_hash = hashlib.sha256(target_username.encode()).hexdigest()
        result = hash_table.get(username_hash, -1)  # Safe lookup
        return result, f"{time.time() - start_time:.4f} seconds"



    def bloom_filter_search(self, target_username):
        start_time = time.time()
        usernames = self.read_file()
        bloom_size = 1000
        hash_function = 3
        bloom_filter = [False] * bloom_size
        for username in usernames:
            for i in range(hash_function):
                index = int(hashlib.sha256(f'{username}{i}'.encode()).hexdigest(), 16) % bloom_size
                bloom_filter[index] = True
        for i in range(hash_function):
            index = int(hashlib.sha256(f'{target_username}{i}'.encode()).hexdigest(), 16) % bloom_size
            if not bloom_filter[index]:
                return -1, f"{time.time() - start_time:.4f} seconds"
        line_number = 0
        for line in usernames:
            line_number += 1
            if line == target_username:
                return line_number, f"{time.time() - start_time:.4f} seconds"
        return -1, f"{time.time() - start_time:.4f} seconds"
