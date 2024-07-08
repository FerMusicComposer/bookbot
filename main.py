def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
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
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()
