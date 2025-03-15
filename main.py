from stats import process
from stats import calculate_letters
from stats import sort_dict

def get_book_text(path):
    with open(path) as file:
        content = file.read()
    return content


def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    no_words = process(text)
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