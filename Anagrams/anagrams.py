import load_dictionary
word_list=load_dictionary.load('2of4brif.txt')
anagram_list=[]
name=input("\n input a name to generate an anagram\n")
print(f"input name ={name}")
name=name.lower()
print(f"Using name ={name}")
name_sorted=sorted(name)
for word in word_list:
    word=word.lower()
    if word !=name:
        if sorted(word)==name_sorted:
            anagram_list.append(word)
print()
if len(anagram_list)==0:
    print('You need a larger dictionary or a new name')
else:
    print("Anagrams = ",*anagram_list,sep='\n')