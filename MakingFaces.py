#problem : like in discord and whatsapp to convert the :) and :( into the emojis 🙂 and 🙁 respectively  
def main():
    print(convert())

def convert():
    x=input()
    if (":)" in x and ":(" in x):
        x=x.replace(":)","🙂")
        x=x.replace(":(","🙁")
        return x
    elif ":)" in x:
        return (x.replace(":)","🙂"))
    elif ":(" in x:
        return (x.replace(":(","🙁"))

    else:
        return 0
main()
