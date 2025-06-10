def get_book_text(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

from stats import book_word_count
call: book_word_count()