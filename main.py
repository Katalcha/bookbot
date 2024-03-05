def main():
    path_to_book = "books/frankenstein.txt"

    book_text = get_book_text(path_to_book)
    book_words = get_num_words(book_text)
    chars_dict = get_char_dict(book_text)
    chars_list = char_dict_to_list(chars_dict)

    print(f"\n--- Begin report of {path_to_book} ---\n")
    print(f"{book_words} words found in the document\n")
    get_details(chars_list)
    print(f"\n--- End report ---\n")

def sort_on(dict):
    return dict["num"]

def char_dict_to_list(chars_dict):
    list = []
    for char in chars_dict:
        list.append({"char": char, "num": chars_dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list

def get_details(chars_list):
    for elem in chars_list:
        if elem["char"].isalpha():
            print(f"The '{elem["char"]}' character was found {elem["num"]} times")
        else:
            continue

def get_book_text(path_to_book):
    with open(path_to_book) as file:
        return file.read()

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_char_dict(book_text):
    chars = {}
    for char in book_text:
        lower = char.lower()
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

main()
