#Problem : To obtain the veggie/fruit from user and add it to the dict, then print all the stuffs and how many times theyre present in the dict (like their nos)
'''
1. dict is created and the input is obtained from user, if its already there in the list, then its key is incremented by 1
2. if its not there then its key is declared to 1, ie adding it to the dict with key as 1 and the value as 'item'
3. then when CTRL + D, is pressed, the dict elements in the sorted dict are printed using for loop, then exited
'''
import sys
grocery_list={}
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item]+=1
        else:
            grocery_list[item]=1
    except EOFError:
        new=sorted(grocery_list)
        for i in new:
            print(f"{grocery_list[i]} {i}")
        sys.exit()

