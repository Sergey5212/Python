from string import ascii_lowercase
def is_pangram(text):
    text = text.replace(' ','')
    text = text.lower()
    for i in ascii_lowercase:
        if i not in text:
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))