def find_longest_word(document, longest_word=""):
    if document == "":
        return longest_word
        
    word_split = document.split(maxsplit=1)

    if len(word_split) < 1:
        return longest_word

    first_word = word_split[0]
    
    # print(f"word: {first_word} | character count: {len(first_word)}")

    if len(first_word) > len(longest_word):
        longest_word = first_word
        
    if len(word_split) > 1:
        return find_longest_word(word_split[1], longest_word)
    else:
        return longest_word