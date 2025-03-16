from stats import process
from stats import calculate_letters
from stats import sort_dict
import sys

def get_path():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        return sys.argv[1]
    

def get_book_text(path):
    try:
        with open(path) as file:
            content = file.read()
    except FileNotFoundError:
        print("File is not there: Check your path")
        sys.exit(1)
    except:
        print("Error occured while reading the file Try again")
        sys.exit(1)
    return content


def main():
    file_path = get_path()
    text = get_book_text(file_path)
    no_words = process(text) #calculates total words
    letters = calculate_letters(text)
    sorted_l = sort_dict(letters)
    print("============ BOOKBOT ============",
        "Analyzing book found at books/frankenstein.txt...",
        "----------- Word Count ----------",
        f"Found {no_words} total words",
        "--------- Character Count -------", sep="\n" ) 
    for key in sorted_l:
        print(f"{key}: {sorted_l[key]}")
    print("============= END ===============")

main()