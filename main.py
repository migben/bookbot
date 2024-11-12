def count_words(book):

    with open(book, 'r') as f:
        # print(len(f.read().split()))
        word_count = len(f.read().split())
    return f"{word_count} words found in the document"

def count_characters(book):
    char_count = {}
    with open(book, 'r') as f :
        for char in f.read().lower():
            if char.isalpha():
                char_count[char] = char_count.get(char, 0) + 1
    sorted_char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
    # print(char_count)
    return sorted_char_count

def report():
    chart_count = count_characters("books/frankenstein.txt")
    print("--- Begin report of books/frankenstein.txt ---")
    print(count_words("books/frankenstein.txt"))
    print(" ")
    for i in chart_count:
        print(f"The {i} character was found {chart_count[i]} times")
    print("--- End report ---")


# count_characters("books/frankenstein.txt")
# count_words("books/frankenstein.txt")

report()
