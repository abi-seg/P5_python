words = ["openclassrooms", "developpeur", "algorithme"]
voyells = "aeiouy"
result = []
for word in words:
    count = 0
    for letter in word:
        if letter in voyells:
            count += 1
    result.append((word,count))
print (result)
