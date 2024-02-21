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
