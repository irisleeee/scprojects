"""
File: anagram.py
Name: Iris Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
PYTHON_LIST = []
ANA_LIST = []                 # List contains the anagrams found


def main():
    global ANA_LIST
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        str = input('Find anagram for: ')
        ANA_LIST = []
        if str == EXIT:
            break
        else:
            find_anagrams(str)
            print('Searching...')
            print(len(ANA_LIST), 'anagrams: ', ANA_LIST)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            PYTHON_LIST.append(line)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    lst = []
    for i in range(len(s)):
        lst.append(s[i])

    find_anagrams_helper(lst, "", len(s))


def find_anagrams_helper(lst, current_w, len_s):
    if len(current_w) == len_s:
        if current_w in PYTHON_LIST and current_w not in ANA_LIST:
            print('Searching...')
            print('Found: ', current_w)
            ANA_LIST.append(current_w)
    else:
        for j in lst:
            if j not in current_w:

                # Choose
                current_w += j
                # Explore
                if has_prefix(current_w) is True:
                    find_anagrams_helper(lst, current_w, len_s)
                # Un-choose
                current_w = current_w[:-1]



            elif j in current_w and lst.count(j) > 1 and lst.count(j) >= current_w.count(j):
                # Choose
                current_w += j
                # Explore
                if has_prefix(current_w) is True:
                    find_anagrams_helper(lst, current_w, len_s)
                # Un-choose
                current_w = current_w[:-1]
            else:
                pass


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for w in PYTHON_LIST:
        if w.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
