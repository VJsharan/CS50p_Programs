#PRETTY SIMPLE, IF the greeting starts with h, give 20 bucks otherwise 100 bucks,
#also remove existing whitespace and make it case insensitive for all sorts of cases
greet=input("Greeting:").strip().lower()
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
