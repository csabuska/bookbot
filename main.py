from stats import get_num_words, summary_of_chars_dict, sorting_dictionary
import sys

def get_book_text(path_to_file:str):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #print(f"First argument: {sys.argv[0]}")
    #print(f"Second argument: {sys.argv[1]}")

    book = get_book_text(book_path)
    num_words = get_num_words(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    to_print = sorting_dictionary(summary_of_chars_dict(book))
    for item in to_print:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")
    



    
    return None

main()




