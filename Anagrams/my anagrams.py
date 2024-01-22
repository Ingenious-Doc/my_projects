import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')


def find_anagrams():
    anagram_list = []
    user_input=input("\n enter word to anagram\n")
    words=set(word_list)
    for word in words:
        if sorted(word)==sorted(user_input) and word!=user_input:
            anagram_list.append(word)
        

    return  anagram_list
print(find_anagrams())