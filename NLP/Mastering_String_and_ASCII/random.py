def convert(text):
    string = ''
    for char in text:
        if(ord(char) >= 97 and ord(char) <= 122):
            string += chr(ord(char) - 32)
        else:
            string += char
    return string

print(convert("hello how are you ?"))
