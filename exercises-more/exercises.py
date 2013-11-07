# PROB 1
# Return the number of words in the string s. Words are separated by spaces.
# e.g. num_words("abc def") == 2
def num_words(s):
   s = s.split()
   return len(s)

# PROB 2
# Return the sum of all the numbers in lst. If lst is empty, return 0.
def sum_list(lst):
    n = 0
    for num in lst:
        n += num
    return n

# PROB 3
# Return True if x is in lst, otherwise return False.
def appears_in_list(x, lst):
    return x in lst

# PROB 4
# Return the number of unique strings in lst.
# e.g. num_unique(["a", "b", "a", "c", "a"]) == 3
def num_unique(lst):
    s = set()
    for a in lst:
        s.add(a)
    return len(s)

# PROB 5
# Return a new list, where the contents of the new list are lst in reverse order.
# e.g. reverse_list([3, 2, 1]) == [1, 2, 3]
def reverse_list(lst):
    lst.reverse()
    return lst

# PROB 6
# Return a new list containing the elements of lst in sorted decreasing order.
# e.g. sort_reverse([5, 7, 6, 8]) == [8, 7, 6, 5]
def sort_reverse(lst):
    #
    #for i in len(lst) - 2:
    #    if list[i] > list[i + 1]
    lst.sort()
    return reverse_list(lst)

# PROB 7
# Return a new string containing the same contents of s, but with all the
# vowels (upper and lower case) removed. Vowels do not include 'y'
# e.g. remove_vowels("abcdeABCDE") == "bcdBCD"
def remove_vowels(s):
    s = s.replace("a", "")
    s = s.replace("A", "")
    s = s.replace("e", "")
    s = s.replace("E", "")
    s = s.replace("i", "")
    s = s.replace("I", "")
    s = s.replace("o", "")
    s = s.replace("O", "")
    s = s.replace("u", "")
    s = s.replace("U", "")
    return s

# PROB 8
# Return the longest word in the lst. If the lst is empty, return None.
# e.g. longest_word(["a", "aaaaaa", "aaa", "aaaa"]) == "aaaaaa"
def longest_word(lst):
    n = 0
    g = ""
    for word in lst:
        if (len(word) > n):
            g = word
            n = len(word)
    if n == 0:
        return None
    else:
        return g

# PROB 9
# Return a dictionary, mapping each word to the number of times the word
# appears in lst.
# e.g. word_frequency(["a", "a", "aaa", "b", "b", "b"]) == {"a": 2, "aaa": 1, "b": 3}
def word_frequency(lst):
    di = {}
    for word in lst:
        if word in di.keys():
            di[word] += 1
        else:
            di[word] = 1
    return di

# PROB 10
# Return the tuple (word, count) for the word that appears the most frequently
# in the list, and the number of times the word appears. If the list is empty, return None.
# e.g. most_frequent_word(["a", "a", "aaa", "b", "b", "b"]) == ("b", 3)
def most_frequent_word(lst):
    di = word_frequency(lst)
    hold = ""
    n = 0
    for key in di:
        if di[key] > n:
            hold = key
            n = di[key]
    if n == 0:
        return None
    else:
        return (hold, n)

# PROB 11
# Compares the two lists and finds all the positions that are mismatched in the list.
# Assume that len(lst1) == len(lst2). Return a list containing the indices of all the
# mismatched positions in the list.
# e.g. find_mismatch(["a", "b", "c", "d", "e"], ["f", "b", "c", "g", "e"]) == [0, 3]
def find_mismatch(lst1, lst2):
    num = []
    a = 0
    for l in lst1:
        if l not in lst2[a]:
            num.append(a)
        a += 1
    return num

# PROB 12
# Returns the list of words that are in word_list but not in vocab_list.
def spell_checker(vocab_list, word_list):
    lstr = []
    for word in word_list:
        if not word in vocab_list:
            lstr.append(word)
    return lstr

