from Algorithm import Algorithm

def main():
    file_path = 'D:/meow/programm/search_al/larger_data.txt'
    algorithm = Algorithm(file_path)

    #sorted_file_path = 'D:/meow/programm/search_al/sorted_usernames.txt'
    #with open(sorted_file_path, 'w') as sorted_file:
    #    for username in algorithm.usernames:
    #        sorted_file.write(username + '\n')

    target_username = input("enter the username to search for: ")
    line_number1 = algorithm.linear_search(target_username)
    line_number2 = algorithm.binary_search(target_username)
    line_number3 = algorithm.optimized_search(target_username)
    line_number4 = algorithm.bloom_filter_search(target_username)


    if line_number1 != -1:
        print(f"Username '{target_username}' found at line {line_number1}.")
    else:
        print(f"Username '{target_username}' not found.")


    if line_number2 != -1:
        print(f"Username '{target_username}' found at line {line_number2}.")
    else:
        print(f"Username '{target_username}' not found.")


    if line_number3 != -1:
        print(f"Username '{target_username}' found at line {line_number3}.")
    else:
        print(f"Username '{target_username}' not found.")
    

    if line_number4 != -1:
        print(f"Username '{target_username}' found at line {line_number4}.")
    else:
        print(f"Username '{target_username}' not found.")

if __name__ == "__main__":
    main()
