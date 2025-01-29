''' problem : to convert the given camelCase into snake_case
    solved by taking the inputs and iterating through them checking if they fall under the ASCII codes 65 to 90 which is for uppercase alphabets
    then if its falling, its replaced with the _ and then the rest is appended after the underscore, then its converted to lowercase and printed'''

word = input("camelCase : ")
new = ''
for i in word:
        if ord(i)>=65 and ord(i)<=90:
            new += "_" + i
        else:
            new +=i
print(new.lower())
