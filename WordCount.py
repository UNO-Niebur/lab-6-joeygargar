#WordCount.py
#Name: Mia Garcia
#Date:3/2/26
#Assignment:Lab 6

import os

def main():
    filename = input("Enter filename: ")

    if not os.path.isfile(filename):
        print("Error: File not found.")
        return

    with open(filename, 'r') as textFile:
        line_count = 0
        word_count = 0
        char_count = 0

        for line in textFile:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)

if __name__ == '__main__':
    main()