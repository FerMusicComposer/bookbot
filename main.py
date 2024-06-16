def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print("")
    words = word_count(text)
    print(f"the word count for this text is: {words}")


def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()
