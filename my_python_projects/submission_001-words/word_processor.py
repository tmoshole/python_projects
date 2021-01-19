import string
text = "These are indeed interesting, an obvious understatement, times. What say you?"
length = 10
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """
    the funcion is converting the string into lower cases and splits the string and returns it as a list.
    """
    text = text.lower()
    text_split = split(" ,.!?",text)
    text_split = list(filter(lambda word: len(word) > 0, text_split))
    return text_split
    

def words_longer_than(length, text):
    """
    the funtion is returning words based on specified length.
    """
    filtered_list = list(filter(lambda word: len(word) > length, convert_to_word_list(text)))
    return filtered_list
    print(filtered_list)
    


def words_lengths_map(text):
    """this function returns a dictionary that maps the number of words in a text.
    """

    lengths = list(map(lambda word: len(word), filter(lambda word: len(word)>0,convert_to_word_list(text))))
    lengths.sort()
    words_length = {key: lengths.count(key) for key in lengths}
    return words_length


def letters_count_map(text):
    """
    This function returns a dictionary that maps each alphabet letter a to z 
    to the number of times that letter occurs in the text.
    """
    text = text.lower()
    char_count = {key:text.count(key) for key in string.ascii_lowercase}
    return char_count
    

def most_used_character(text):
    """
    This funtion returns the letter that occures the most in a text of string.
    """
    if len(text) == 0:
        return None

    count = letters_count_map(text)

    k_max = max(count.keys(), key = (lambda  i: count[i]))
    return(k_max)

if __name__ == "__main__":
    print(convert_to_word_list(text))
    print(words_longer_than(length, text))
    print(words_lengths_map(text))
    print(letters_count_map(text))
    print(most_used_character(text))