def check_anagrams(first_words, second_words):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"
    if len(first_words) == len(second_words):
        for i, first_word in enumerate(first_words):
            if len(first_word) != len(second_words[i]):
                print 0
                continue
            else:
                if (sorted(first_word) == sorted(second_words[i])):
                    print 1
                else: print 0

# check_anagrams(["cinema", "host", "aba", "train"], ["iceman", "shot", "bab", "rain"])__author__ = 'annguyen'
