import sys
if len(sys.argv) < 2:
     raise Exception("Usage: python3 main.py <path_to_book>")
from stats import word_count
from stats import char_count
from stats import char_num
from stats import dict_sort_list
def get_book_text(file_path):
    with open(sys.argv[1]) as file_path:
            file_contents = file_path.read()
    return file_contents
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found", word_count(get_book_text(sys.argv[1])), "total words")
    print("--------- Character Count -------")
    overall_count = char_count(get_book_text(sys.argv[1]))
    sorted_dict = dict_sort_list(overall_count)
    for entry in sorted_dict:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
main()

