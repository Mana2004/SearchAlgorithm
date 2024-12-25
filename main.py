from Algorithm import Algorithm
from Bloom_Filter import Bloom_Filter

def main():
    file_path = 'D:/meow/programm/search_al/usernames.txt'
    algorithm = Algorithm(file_path)
    bloom = Bloom_Filter(file_path)

    #sorted_file_path = 'D:/meow/programm/search_al/sorted_usernames.txt'
    #with open(sorted_file_path, 'w') as sorted_file:
    #    for username in algorithm.usernames:
    #        sorted_file.write(username + '\n')

    target_username = input("enter the username to search for: ")
    line_number1 = algorithm.linear_search(target_username)
    line_number2 = algorithm.binary_search(target_username)
    line_number3 = algorithm.hash_table_search(target_username)
    line_number4 = bloom.bloom_filter_search(target_username)


    if line_number1 != -1:
        print(f"Username '{target_username}' linear search {line_number1}.")
    else:
        print(f"Username '{target_username}' not found.")


    if line_number2 != -1:
        print(f"Username '{target_username}' binary search {line_number2}.")
    else:
        print(f"Username '{target_username}' not found.")


    if line_number3 != -1:
        print(f"Username '{target_username}' hash table search {line_number3}.")
    else:
        print(f"Username '{target_username}' not found.")
    

    print(f"Username '{target_username}' bloom filter search {line_number4}.")


if __name__ == "__main__":
    main()
