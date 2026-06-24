# Task 2: Create Another Module (string_utils.py)

# 1. capitalize_words(text)
# returns text with each word capitalized

def capitalize_words(text):
    return text.title()


# 2. reverse_string(text)
# returns reversed string

def reverse_string(text):
    return text[::-1]


# 3. word_count(text)
# returns number of words in the text

def word_count(text):
    return len(text.split())