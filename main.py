def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents

def count():
    words = main().split()
    total = 0
    for i in words:
        total += 1
    # print(total)
    return total

def each_character():
    lowered_words = main().lower()
    words = ''.join(sorted(lowered_words))
    # print(words)
    character = {}
    for i in words:
        # check = i in character
        # if check == False:
        #     character[i] = 0
        # character[i] += 1

        if i in character:
            character[i] += 1
        else:
            character[i] = 1
    return character

def report():
    counts = count()
    character = each_character()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counts} words found in the document")

    for i in character:
        print(f"The '{i}' character was found {character[i]} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    # main()
    # count()
    # each_character()
    report()
