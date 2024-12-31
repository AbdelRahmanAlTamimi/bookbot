def main():
    book_path = "books/frankenstein.txt"
    text = read_book_content(book_path)
    num_words = count_words(text)
    num_chars_dict = count_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(num_chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def print_report(path, num_words, chars_sorted_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for item in chars_sorted_list:
        char = item["char"]
        count = item["num"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def count_words(text):
    words_list = text.split()
    return len(words_list)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_characters(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered in char_dict:
                char_dict[lowered] += 1
            else:
                char_dict[lowered] = 1
    return char_dict


def read_book_content(path):
    with open(path) as f:
        return f.read()


main()