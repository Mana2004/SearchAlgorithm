#Search Algorithms

This project implements four different search algorithms to locate a target username in a text file (`usernames.txt`).

1. **Linear Search**
2. **Binary Search**
3. **Hash Table Search**
4. **Bloom Filter Search**

---

### Linear Search:

It checks each element in the list one by one until it finds the target username.

The algorithm reads the `usernames.txt` file and stores all usernames in a list.
The algorithm iterates over each line (username) in the list.
It compares each username with the target username.
If the target username is found, the algorithm returns the line number and the time taken.
If the username is not found, it returns `-1` and the time taken.

--issue: Inefficient for large datasets


### Binary Search:

Binary search is for searching sorted data. It works by repeatedly dividing the input list in half.

The algorithm reads the `usernames.txt` file and stores all usernames in a list.
It sorts the usernames in a case-insensitive manner.
The algorithm then repeatedly divides the list into two halves and checks the middle element.
If the target username is found at the middle, it returns the line number and the time taken.
If the target username is smaller than the middle element, the algorithm narrows its search to the left half; if it's larger, it narrows the search to the right half.
The algorithm continues until the target username is found.

--issue: The list must be sorted first, which adds overhead for unsorted datasets.


### Hash Table Search:

Hash table search uses a hash function to store each username and line number in a dictionary.

The algorithm reads the `usernames.txt` file and generates a hash value for each username.
It stores each hash value and line number in a dictionary.
When searching for a target username, the algorithm computes the hash of the target username.
It'll search the hash_table, if it exists then it'll retrive a line number.

--issue: Requires additional memory to store the hash table.


### Bloom Filter Search:

A Bloom filter is a space-efficient data structure, that is used to test whether an element is a member of a set. 

The algorithm reads the `usernames.txt` file and creates a Bloom filter to store username.
The Bloom filter uses k = 9 hash functions to put each username in different indexes in a bit array.
When searching for a target username, the algorithm hashes the username using the same hash functions.
If all indexes in the bit array are True, the username is probably in the set. If any position is False, the username is definitely not in the set.
The algorithm returns the line number if the username is probably present or -1 if the username is definitely absent.

--Pros: Extremely fast lookups, uses very little memory, and can handle very large datasets.
--issue: May return false positives

---

## Why Bloom Filter is the Best Algorithm For This Project:

1.memory efficient --> using a fixed-size bit array 
2.fast --> costant time complexity
3.scalability --> can handle very large datasets

---

## requirements:

1. installing python3
2. installing hashlib ( run in cmd : pip install hashlib )
3. github repository
   git clone https://github.com/Mana2004/SearchAlgorithm.git
