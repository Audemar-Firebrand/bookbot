def book_word_count():
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
       words = file_contents.split()
       word_count = len(words)
    print(f"{word_count} words found in the document")

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
        