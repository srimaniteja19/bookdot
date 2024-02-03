def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_dict = sorted(
        chars_dict.items(), key=lambda x: x[1], reverse=True)
    remove_non_alpha = list(
        filter(lambda x: x[0].isalpha(), sorted_chars_dict))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{num_words} words found in the document')
    print('\n')
    for i in remove_non_alpha:
        print(f'The {i[0]} character was found {i[1]} times')


def get_num_words(text):
    return len(text.split())


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


if __name__ == '__main__':
    main()
