#WordIndex.py
#Name:Mia Garcia
#Date: 3/2/26
#Assignment:Lab 6

import os

def main():
    filename = input("Enter filename: ")

    if not os.path.isfile(filename):
        print("Error: File not found.")
        return

    words = {}
    line_number = 0

    with open(filename, 'r') as textFile:
        for line in textFile:
            line_number += 1
            line = line.lower()

            line_words = line.split()

            words_seen_this_line = set()

            for word in line_words:
                word = word.strip(".,!?;:")

                if word == "":
                    continue

                if word not in words_seen_this_line:
                    words.setdefault(word, []).append(line_number)
                    words_seen_this_line.add(word)

    print("\nIndex:\n")
    for word in sorted(words):
        print(f"{word}: {sorted(words[word])}")


if __name__ == '__main__':
    main()