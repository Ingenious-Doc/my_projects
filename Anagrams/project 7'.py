import sys
from itertools import permutations
from collections import Counter
import load_dictionary


def prep_words(name,word_list_ini):
    """Prepare word list for finding anagrams"""
    print(f"Length initial word list = {len(word_list_ini)}")
    len_name=len(name)
    word_list=[word.lower for word in word_list_ini if len(word)==len(name)]
    print(f"length of new word_list ={len(word_list)}")
    return word_list


def cv_map_words(word_list):
    """Map letters in words to consonants and vowels"""
    vowels="aeiouy"
    cv_mapped_words=[]
    for word in word_list:
        temp=""
        for letter in word:
            if letter in vowels:
                temp+="v"
            else:
                temp+='c'
        cv_mapped_words.append(temp)
    total=len(set(cv_mapped_words))
    target=0.05
    n=int(total*target)
    count_pruned=Counter(cv_mapped_words).most_common(total-n)
    filtered_cv_map=set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print("length filtered_cv_map={}".format(len(filtered_cv_map)))
    return filtered_cv_map


def cv_map_filter(name,filtered_cv_map):
    """Remove permutations of words based on unlikely cons-vowel combos"""
    perms={''.join(i) for i in permutations(name)}
    print("Length of initial permutations set ={}".format(len(perms)))
    vowels='aeiouy'
    filter_1=set()
    for candidate in perms:
        temp=""
        for letter in candidate:
            if letter in vowels:
                temp+='v'
            else:
                temp+='c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print('# Choices after filter_1={}'.format(len(filter_1)))
    return filter_1


def trigram_filter(filter_1,tirgrams_filtered):
    """remove unlikley trigrams from permutations"""
    filtered=set()
    for candidate in filter_1:
        for triplet in tirgrams_filtered:
            triplet=triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2=filter_1-filtered
    print("# of choices after fileter_2 ={} ".format(len(filter_2)))
    return filter_2



def main():
    """Load files, run filters, allow user to view anagrams byy 1st letter"""
    name="tmvoordle"
    name=name.lower()
    word_list_ini=load_dictionary.load("2of4brif.txt")
    trigrams_filtered=load_dictionary.load('least_likely_trigrams.txt')
    word_list=prep_words(name,word_list_ini)
    filtered_cv_map=cv_map_words(word_list)
    filter_1=cv_map_filter(name,filtered_cv_map)
    filter_2=trigram_filter(filter_1,trigrams_filtered)
    filter_3=letter_pair_filter(filter_2)
    view_by_letter(name,filter_3)

