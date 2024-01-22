def main():
    vowels=['a','e','i','o','u']
    my_word=input('\nInsert word\n')
    if my_word[0] not in vowels:
        my_word=my_word[1:]+my_word[0]+'ay'
    print(my_word)
if __name__=="__main__":
    main()