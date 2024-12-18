from Algorithm import Algorithm

def main():
    file_path = 'D:/meow/programm/search_al/usernames.txt'
    algorithm = Algorithm(file_path)

    target_username = input("enter the username to search for: ")
    line_number = algorithm.linear_search(target_username)

    if line_number != -1:
        print(f"Username '{target_username}' found at line {line_number}.")
    else:
        print(f"Username '{target_username}' not found.")

if __name__ == "__main__":
    main()
