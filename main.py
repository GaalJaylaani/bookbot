from stats import get_num_words, get_ch_num, chars_dictsorted
import sys


def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_ch_num(text)
    chars_sorted_list = chars_dictsorted(char_dict)
    print("Usage: python3 main.py <path_to_book>")
    print_report(book_path, num_words, chars_sorted_list)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")







main()