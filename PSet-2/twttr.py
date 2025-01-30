#problem : to obtain and input from the user and omit and remove all the vowels from the it, and print the output
'''
the vowels are in a list,
the word from user and in a for loop, the string elements are traversed
they are checked if they belong in the vowel, if yes it is replaced with <blank>,
if it doesnt no changes are made, it remains as it is,
then the changed <word> variable is printed as output
'''

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
word=input("Input: ")
for i in word:
    if i in vowels:
        word=word.replace(i,'')
print("Output :",word)
