import sys

def book_word_count():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    return word_count

def character_count():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_characters = {}
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        for character in file_contents:
            if character.lower() in num_characters:
                num_characters[character.lower()] += 1
            else:
                num_characters[character.lower()] = 1
    return num_characters

def bookbot_report(num_characters):
    numbers = []
    for character in num_characters:
        if character.isalpha() == True:
            numbers.append({"char": character, "num": num_characters[character]})
    def sort_on(dict):
        return dict["num"]
    numbers.sort(reverse=True, key=sort_on)
    return numbers
