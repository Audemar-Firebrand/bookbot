def get_book_text(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def book_word_count():
    with open("books/frankenstein.txt") as f:
       file_contents = f.read()
       words = file_contents.split()
       word_count = len(words)
    print(f"{word_count} words found in the document")

call: book_word_count()