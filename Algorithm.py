class Algorithm:
    def __init__(self, file_path):  
        self.file_path = file_path
        self.usernames = self.load_usernames()

    def load_usernames(self):
        with open(self.file_path, 'r') as file:
            usernames = [line.strip() for line in file]
        return sorted(usernames)

    #def linear_search(self, target_username):
     #   with open(self.file_path, 'r') as file:
      #      line_number = 0  
       #     for line in file:
        #        line_number += 1 
         #       username = line.strip()  
          #      if username == target_username:
           #         return line_number  
        #return -1  

    def binary_search(self, target_username):
        low = 0
        high = len(self.usernames) - 1  # Use self.usernames here
        while low <= high:
            mid = (low + high) // 2
            mid_username = self.usernames[mid]  # Use self.usernames here
            if mid_username == target_username:
                return mid  # Return the index of the found username
            elif mid_username < target_username:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # Indicate not found