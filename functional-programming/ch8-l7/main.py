from functools import lru_cache

@lru_cache()
def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        trimmed_word = word[1:-1]
        return is_palindrome(trimmed_word)
    return False
