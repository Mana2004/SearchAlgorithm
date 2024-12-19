import hashlib
import time

start_time = time.time()

class Algorithm:
    def __init__(self, file_path):  
        self.file_path = file_path
        #self.usernames = self.sort_usernames()

    def read_file(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return usernames


    def linear_search(self, target_username):
        usernames = self.read_file()
        line_number = 0  
        for line in usernames:
            line_number += 1 
            username = line.strip()  
            if username == target_username:
                return line_number,time.time() - start_time
        return -1 


    """def sort_usernames(self):
        usernames = self.read_file()
        return sorted(usernames, key=lambda s: s.casefold())

    def binary_search(self, target_username):
        sorted_usernames = sorted(self.usernames)
        low = 0
        high = len(sorted_usernames) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_username = sorted_usernames[mid]
            if mid_username == target_username:
                return self.usernames.index(mid_username) + 1, time.time() - start_time
            elif mid_username < target_username:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    

    def create_hash_table(self):
        usernames = self.read_file()
        hash_table = {}
        line_number = 0  
        for line in usernames:
            line_number += 1  
            username_hash = hashlib.sha256(line.encode()).hexdigest()
            hash_table[username_hash] = (line, line_number)  
        return hash_table
    
    def optimized_search(self, target_username):
        username_hash = hashlib.sha256(target_username.encode()).hexdigest()
        hash_table = self.create_hash_table()
        result = hash_table.get(username_hash)
        if result:
            return result[1], time.time() - start_time
        else:
            return -1"""

