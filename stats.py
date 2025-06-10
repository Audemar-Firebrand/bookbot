def book_word_count():
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
       words = file_contents.split()
       word_count = len(words)
    return word_count

def character_count():
    num_characters = {}
    with open("books/frankenstein.txt") as f:
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
