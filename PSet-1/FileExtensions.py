#checks if the given filename ends with the specified on on the if conditions, makes it easier by stripping off the whitespaces and making it lowercase for easy checking and just returns whichever type it is
user_input=input("File name: ").strip().lower()
if user_input.endswith(".gif"):
    print("image/gif")
elif user_input.endswith(".jpg"):
    print("image/jpeg")
elif user_input.endswith(".jpeg"):
    print("image/jpeg")
elif user_input.endswith(".png"):
    print("image/png")
elif user_input.endswith(".pdf"):
    print("application/pdf")
elif user_input.endswith(".txt"):
    print("text/plain")
elif user_input.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
