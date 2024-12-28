from collections import Counter
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
def word_count(book):
    words = book.split()
    count = len(words)
    return count
def character_count(book):
    special_characters = "!@#$%^&*()-1234567890[].:?;_,/"
    escape_characters = '\'\"\n\\'
    lower_case_text = book.lower()
    char_count = Counter(lower_case_text)
    if ' ' in char_count:
        del char_count[' ']
    for special_character in special_characters:
        if special_character in char_count:
            del char_count[special_character]
    for escape_character in escape_characters:
        if escape_character in char_count:
            del char_count[escape_character]
    print("Character frequencies:")
    for char, count in char_count.items():
        print(f"'{char}': {count}")

book = main()
print("--- Begin report of books/frankenstein.txt ---")
print("Word count: " + str(word_count(book)))
character_count(book)
print("--- End report ---")