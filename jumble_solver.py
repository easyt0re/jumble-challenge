'''
a python script that takes a text file (a list of words)
and a word to find all anagrams and sub-anagrams
'''

import sys
from collections import defaultdict

def get_all_substrs(sorted_word):
    '''a recursive function to get all the sub-strings of the given sorted word (str).

    Args: sorted_word: a word sorted in str type

    Returns: a list where each item is a (sorted) str

    with a sorted word that is Counter(letter_1:n_1, letter_2:n_2, ..., letter_m:n_m)
    number of all sub-string = (n_1 + 1) * (n_2 + 1) * ... * (n_m + 1) (empty string is included)
    this avoids duplicates and wasted iterations
    all the sub-string =  all sub-strings for all the letters in the front
                        + all choices for number of the last letter
    '''
    new_list_substrs = [] # an empty list later with str as items

    # get the last letter b/c it's sorted
    last_letter = sorted_word[-1:]
    # strip the last letter(s) to get ready for recursion
    new_sorted_word = sorted_word.strip(last_letter)
    # how many last letter(s)
    last_letter_num = len(sorted_word) - len(new_sorted_word)

    if len(new_sorted_word) != 0:
        # do recursive
        old_list_substrs = get_all_substrs(new_sorted_word)
    else:
        # end of recursive, no more letters in the front
        old_list_substrs = ['']

    # if the word contains n last letters
    # the sub-string only have n+1 choices (0 to n)
    # on how many of this last letter to include
    add_list_substrs = [last_letter * each_num for each_num in range(last_letter_num + 1)]
    new_list = [each_old_substr + each_add_substr
                for each_add_substr in add_list_substrs
                for each_old_substr in old_list_substrs]
    new_list_substrs.extend(new_list)
    return new_list_substrs


def main():
    '''this is the main function.
    '''
    dict_file_name = sys.argv[1]
    jumble = sys.argv[2]

    # 1
    # sort all words in the text file
    # the words with the same sorted result are anagrams
    # use `set` to avoid duplication
    sorted_words = defaultdict(set)

    with open(dict_file_name, "r") as text_file:
        for word in text_file:
            word = word.strip()
            sorted_id = ''.join(sorted(word)) # each word is sorted to form an "ID"
            sorted_words[sorted_id].add(word) # words with the same ID are saved under the same ID

    # 2
    # given a word, find its sorted form and its subs
    sorted_jumble = ''.join(sorted(jumble.lower()))

    # v3, use math
    # generate the combinations directly
    # without using set to eliminate duplicate
    sorted_all_subs = get_all_substrs(sorted_jumble)

    for each_sub in sorted_all_subs:
        if each_sub in sorted_words:
            if len(each_sub) == len(jumble):
                print("\n".join(sorted_words[each_sub] - {jumble}))
                # the word itself is taken out
            else:
                print("\n".join(sorted_words[each_sub]))

if __name__ == '__main__':
    main()
