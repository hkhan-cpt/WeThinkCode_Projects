import string


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
    """Takes string of text as input and changes it into a list of lowercase words.

    Args:
        text (string): Words being processed through the function.

    Returns:
        [list]: Text converted into list of strings.
    """
    list_of_words = list(filter(lambda word: word != "", split(" ,;?.!", text.lower())))
    return list_of_words


def words_longer_than(length, text):
    """Takes an integer and string of text as input and filters it to return any words with more characters than the specified length. 

    Args:
        length (integer): Specified length.
        text (string): Words being processed through the function.

    Returns:
        [list]: Words longer than specified length.
    """
    words_longer_than_length = list(filter(lambda word: len(word) > length, split(" ,;?.!", text.lower())))
    return words_longer_than_length


def words_lengths_map(text):
    """Takes a string of text as input and returns a dicionary of length of words mapped to the number of words found in the text of each length. 

    Args:
        text (string): Words being processed through the function.

    Returns:
        [dictionary]: Word lengths mapped to number of words in the text of each length.
    """
    word_lengths = list(map(lambda word: len(word), split(" ,;?.!", text.lower())))
    word_lengths_no_0 = list(filter(lambda word_length: word_length != 0 , word_lengths))
    word_lengths_set = set(word_lengths_no_0)
    dict_length = {key: word_lengths_no_0.count(key) for key in word_lengths_set}
    return dict_length


def letters_count_map(text):
    """Takes a string of text as input and returns a dicionary of the alphabet mapped to the number of times each letter is found in the text. 

    Args:
        text (string): Words being processed through the function.

    Returns:
        [dictionary]: Alphabet mapped to the number of times each letter is found in the text.
    """
    word_list_lowercase = text.lower()
    alphabet = string.ascii_lowercase
    dict_char = {key: word_list_lowercase.count(key) for key in alphabet}
    return dict_char


def most_used_character(text):
    """Takes a string of text as input and returns a letter, from the dicionary returned in letter_count_map, which appears the most times in the text. 

    Args:
        text (string): Words being processed through the function.

    Returns:
        [dictionary]: Letter which appears the most times in the text.  
    """
    if text == "":
        return None
    else:
        char_count = letters_count_map(text)
        most_used_char = max(char_count, key = lambda char: char_count[char])
        return most_used_char


if __name__ == "__main__":
    text = "These are indeed interesting, an obvious understatement, times. What say you?"
    # text = ""
    # text = "X"

    list_of_words = convert_to_word_list(text)
    # print (list_of_words)

    length = 10
    words_longer_than_length = words_longer_than(length, text)
    # print (words_longer_than_length)

    dict_length = words_lengths_map(text)
    # print (dict_length)

    dict_char = letters_count_map(text)
    # print (dict_char)

    most_used_char = most_used_character(text)
    # print (most_used_char)