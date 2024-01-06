
def main() -> int:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    count_of_words = count_letters(text)
    char_list = list(count_of_words.items())
    char_list = sorted(char_list, key = lambda x:x[1], reverse=True)
    for char, count in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
        
    count_of_words = count_letters(text)

def count_letters(text):
    count_of_words = {}
    for c in text:
        if c.lower() in count_of_words:
            count_of_words[c.lower()] += 1
        else:
            count_of_words[c.lower()] = 1
    return count_of_words

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
if __name__ == "__main__":
    main()