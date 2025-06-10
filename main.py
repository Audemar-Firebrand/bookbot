def get_book_text(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

from stats import book_word_count
word_count = book_word_count()

from stats import character_count
result = character_count()

from stats import bookbot_report
report = bookbot_report(result)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print(f"--------- Character Count -------")
for item in report:
    print(f"{item["char"]}: {item["num"]}")
print("============= END ===============")