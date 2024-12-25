import hashlib
import time

class Algorithm:
    #intializing the requirements
    def __init__(self, file_path):  
        self.file_path = file_path

    #reads usernames.txt file
    def read_file(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return usernames


    #linear search checks every line to see if it's the wanted username
    def linear_search(self, target_username):
        usernames = self.read_file()

        start_time = time.time()

        line_number = 0

        for line in usernames:
            line_number += 1   
            if line == target_username:
                return line_number, f"{time.time() - start_time:.6f} seconds"
        return -1, f"{time.time() - start_time:.6f} seconds"


    #binary search sorts the usernames in a case insensetive manner
    #then breaks the list in half then checks those halfs
    def binary_search(self, target_username):
        usernames = self.read_file()

        start_time = time.perf_counter()

        sorted_usernames = sorted(usernames, key=lambda s: s.casefold())
        low = 0
        high = len(sorted_usernames) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_username = sorted_usernames[mid]
            if mid_username.casefold() == target_username.casefold():
                return mid + 1, f"{time.perf_counter() - start_time:.6f} seconds"
            elif mid_username.casefold() < target_username.casefold():
                low = mid + 1
            else:
                high = mid - 1
        return -1, f"{time.perf_counter() - start_time:.6f} seconds"


    #creats a hash dictionary using usernames also stores line numbers
    #it gets the target username's hash from the table if it couldn't find it the -1
    def hash_table_search(self, target_username):
        usernames = self.read_file()

        start_time = time.time()

        hash_table = {}
        line_number = 0

        for line in usernames:
            username_hash = hashlib.sha256(line.encode()).hexdigest()
            hash_table[username_hash] = line_number 
            line_number += 1
        target_username_hash = hashlib.sha256(target_username.encode()).hexdigest()
        line_number = hash_table.get(target_username_hash, -1)
        return line_number, f"{time.time() - start_time:.6f} seconds"