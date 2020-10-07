"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    # return 'Contents of your file as one long string'
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    # loop over words, first 2 words is the tuple, 3rd word is a value
    # move forward in list by 1
    # create list if first and second word aren't there, otherwise add it to list

    contents = open_and_read_file("green-eggs.txt")
    words = contents.split()

    for i in range(0, len(words) - 3):
        # word_list = [words[i], words[i + 1], words[i + 2]] 
        tuple_word = (words[i], words[i + 1])
        list_word = [words[i + 3]]
        print(tuple_word, list_word)

    # for word in word_list:
    #     (word[i], word[i + 1])
    #     print(word_list)

    # tuple_words = [(words[i], words[i + 1]) for i in range(0, len(words) - 1)]
    # key = tuple_words
    # value = [words[i + 2] for i in range(len(words) - 2)]
    # chains[key] = value

    # print(f"tuples {tuple_words}")

    # list_values = list.extend(words[i + 2])
    # print(list_values)
    # for words in contents:
    #     list = []
    #     list_values = list.extend(words[i + 2])
    #     print(list_values)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
