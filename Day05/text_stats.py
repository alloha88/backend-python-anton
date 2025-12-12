text = "Python is awesome and python is powerfull"
text = text.lower()
words = text.split()
count= 0 
for word in words:
    if word == "python":
        count += 1
print("Слово 'python' встречается раз:", count)