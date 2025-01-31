#intermediate code 
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2<=len(s)<=6 and s[0]!='0' and s[0:2].isalpha() and s.isalnum():
        if len(s)==2 and s.isalpha():
            return True
        if len(s)>2:
                for char in s:
                    if char.isdigit() and char!=0:
                        if s[index[char]:].numeric():
                            return True
                    else:
                        return False
    else:
        return False
main()
