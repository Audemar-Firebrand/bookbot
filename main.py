def get_book_text(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
call: get_book_text()