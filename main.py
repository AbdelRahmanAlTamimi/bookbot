def read_book_content():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

   
def count_words(text):
    words_list = text.split()
    print(len(words_list))
    
    
    
def main(): 
    count_words(read_book_content())
    
main()