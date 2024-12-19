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
            username = line.strip()  
            if username == target_username:
                return line_number, f"{time.time() - start_time:.4f} seconds"
        return -1



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
                return mid + 1 ,f"{time.time() - start_time:.4f} seconds"
            elif mid_username.casefold() < target_username.casefold():
                low = mid + 1
            else:
                high = mid - 1
        return -1
    

    #hash_tabel
    def optimized_search(self, target_username):
        start_time = time.time()
        usernames = self.read_file()
        hash_tabel = {}
        line_number = 0
        for line in usernames:
            line_number += 1
            username_hash = hashlib.sha256(line.encode()).hexdigest()
            hash_tabel[username_hash] = line_number
        username_hash = hashlib.sha256(target_username.encode()).hexdigest()
        result = hash_tabel[username_hash]
        if result:
            return result, f"{time.time() - start_time:.4f} seconds"
        else:
            return -1
        
    