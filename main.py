def main():
    book_path = "books/frankenstein.txt"
    #book_path = "books/test_text.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars_dict = get_chars_dict(text)
    sorted_chars_list = get_sorted_chars_list(num_chars_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()

    for character in sorted_chars_list:
        if character.isalpha():
            print(f"The '{character}' character was found {num_chars_dict[character]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text_input):
    words = text_input.split()
    return len(words)

def get_chars_dict(text_input):
    words = text_input.lower()
    character_dict = {}
    for character in words:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def get_sorted_chars_list(chars_dict):
    chars_list = list(chars_dict.keys())
    chars_list.sort()
    return chars_list

main()