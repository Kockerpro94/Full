text = "P@ssw0rd"
vowels = "aeiouAEIOU"
new_text = ""

for char in text:
    if char in vowels:
        new_text += "*"
    else:
        new_text += char

print(new_text)
