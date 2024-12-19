class Algorithm:
    def __init__(self, file_path):  
        self.file_path = file_path
        self.usernames = self.sort_usernames()

    def linear_search(self, target_username):
        with open(self.file_path, 'r') as file:
            line_number = 0  
            for line in file:
                line_number += 1 
                username = line.strip()  
                if username == target_username:
                    return line_number  
        return -1 
         
    def sort_usernames(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return sorted(usernames, key=lambda s: s.casefold())

    def binary_search(self, target_username):
        sorted_usernames = sorted(self.usernames)
        low = 0
        high = len(sorted_usernames) - 1
        while low <= high:
            mid = (low + high) // 2
            mid_username = sorted_usernames[mid]
            if mid_username == target_username:
                return self.usernames.index(mid_username) + 1
            elif mid_username < target_username:
                low = mid + 1
            else:
                high = mid - 1
        return -1