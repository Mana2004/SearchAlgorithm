# Open the file in read mode
with open('D:/meow/programm/search_al/usernames.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # lsPrint each line
        print(line.strip())