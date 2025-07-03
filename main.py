import sys
from stats import get_word_count, get_character_appearance_count, sort_character_count

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()

    return contents

def create_book_report(title, word_count, character_count):
    # book_title = title.split("/")
    # book_title = f"{book_title[1]}{book_title[2]}"

    report = ""

    report += "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {title}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"
    for key, value in character_count.items():
        if key.isalpha():
            report += f"{key}: {value}\n"

    report += "============= END ==============="

    return report

def main():
    # for debugging purposes
    # filepath = "./books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = get_word_count(text)
    character_count = get_character_appearance_count(text)
    book_report = create_book_report(filepath, word_count, sort_character_count(character_count))

    print(book_report)

main()