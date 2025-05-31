from stats import word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print_report(book_path)

def get_book_text(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def print_report(book_path):
    text = get_book_text(book_path)
    word_count_result = word_count(text)
    char_counts = count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count_result} words found in the document\n")

    for char, count in sorted(char_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"'{char}: {count}'")

    print("--- End report ---")

main()
