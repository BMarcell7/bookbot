
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    return file_content
        
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) +1
    return char_count

def sort_on(char_count):
    sorted_char_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_list

if __name__ == "__main__":
    file_path = "books/frankenstein.txt"
    book_text = main()
    
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_characters = sort_on(char_count)
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    for char, count in sorted_characters:
        print(f"The '{char}' character was found {count} times")
    print(f"--- End report ---")