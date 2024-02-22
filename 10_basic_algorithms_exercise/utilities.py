# strings for palindrome test
palindrome_word = "deified"
palindrome_word_two = "deed"
non_palindrome_word = "summer"
palindrome_phrases_one = "Name now one man"
palindrome_phrases_two = "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod"
non_palindrome_phrases = "Notable palindromic phrases in English"
palindrome_phrases_three = (
    "T. Eliot, top bard, notes putrid tang emanating, is sad; I'd assign it a name: gnat dirt "
    "upset on drab pot toilet.")

string_list = [palindrome_word, palindrome_word_two, non_palindrome_word, palindrome_phrases_one,
               palindrome_phrases_two, non_palindrome_phrases, palindrome_phrases_three]


# removes punctuations, spaces and concatenate in single string of lower letters
def punctuation_and_spaces_remover(string: str):
    return "".join([c for c in string if c.isalnum()]).lower()


# checks if given number is int
def is_int(number):
    if isinstance(number, int):
        return True
    else:
        return False


# compares length of two words
def is_word_len_equal(w_one: str, w_two: str):
    if len(w_one) == len(w_two):
        return True
    else:
        return False


# checks if each letter from the first word is contained in the second word
def letters_uniformity(str_one: str, str_two: str):
    letters_differences_between_words = [letter for letter in str_one if letter not in str_two]
    if not letters_differences_between_words:
        return True
    else:
        return False
