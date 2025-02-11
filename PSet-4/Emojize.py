#problem : To convert :cat_face: to 😺, like in discord or whatsapp
# pretty simple solution :
'''
• import the emoji module and accepting the i/p from user
• then use the emojize function in the package and pass the input string to it, with an alias
• then it returns the desired emoji for given string which is then displayed

Why language='alias' is being used?
so that it returns the specific emoji for that alias rather than returning the same string,
if alias isnt used some emojis wont get displayed, just their text alone
In the code you provided, the `language='alias'` argument is being used in the `emoji.emojize()` function to specify how the emoji shortcodes are interpreted. The `emoji` module supports different types of input for emoji shortcodes, and the `language='alias'` argument tells the function to use **alias names** for the emoji codes.

Here’s a breakdown:

- The **alias** is a simpler, user-friendly name for emojis (like `:smile:` or `:thumbs_up:`). These names are part of the `emoji` library's alias system and can be used as input to convert text representations into emoji.
  
For example, if you input:

```
x = ":smile: :thumbs_up:"
```

And then run the `emoji.emojize(x, language='alias')`, the result will be the corresponding emojis:

```
😄 👍
```

Without `language='alias'`, the function would try to find emojis using Unicode characters or other representations, and the result might not work as expected. By specifying `language='alias'`, the input is interpreted as a series of alias names for emojis, ensuring that the function properly converts the shorthand codes into the correct emoji characters.

In short, `language='alias'` tells the `emoji.emojize()` function to process input as emoji shortcodes or aliases (like `:smile:`) and convert them to the corresponding emoji characters.
'''
import emoji
x=input("Input: ")
new=emoji.emojize(x,language='alias')
print(f"Output: {new}")
