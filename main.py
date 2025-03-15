from stats import process

def get_book_text(path):
    with open(path) as file:
        content = file.read()
    return content



def main():
    file_path = "./books/frankenstein.txt"
    text = get_book_text(file_path)
    no_words = process(text)
    print(f"{no_words} words found in the document")

main()