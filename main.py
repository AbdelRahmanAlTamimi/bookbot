def main(): 
    book_path = "books/frankenstein.txt"
    text = read_book_content(book_path)
    num_words = count_words(text)
    num_chars_dict = count_characters(text)
    print(num_chars_dict)


def count_words(text):
    words_list = text.split()
    print(len(words_list))


def count_characters(text):
    char_dict = {}
    for char in text:
        lowerd = char.lower()
        if lowerd in char_dict:
            char_dict[lowerd] += 1
        else:
            char_dict[lowerd] = 1
    
    return char_dict


def read_book_content(path):
    with open(path) as f:
        return f.read()

   

    
main()