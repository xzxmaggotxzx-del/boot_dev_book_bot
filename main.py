import sys

from stats import count_words
from stats import count_symbols
from stats import sort_symbols

def get_book_text(file):
    file_contents = ""
    
    with open(file) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_string = get_book_text(book_path)
    num_words = count_words(book_string)
    symbols_dict = count_symbols(book_string)
    symbols_dict_sorted = sort_symbols(symbols_dict)

    # print(f"{num_words} words found in the document")
    # print(symbols_dict)
    # print(symbols_dict_sorted)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    for symols_item in symbols_dict_sorted:
        char = symols_item["char"]
        num = symols_item["num"]

        if char.isalpha():
            print(f"{char}: {num}")

    print(f"============= END ===============")


main()