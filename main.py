words = [
        "Aardvark", "Bison", "Cheetah", "Dolphin", "Elephant",
        "Flamingo", "Giraffe", "Hedgehog", "Iguana", "Jaguar",
        "Kangaroo", "Lemur", "Mongoose", "Numbat", "Ostrich",
        "Pangolin", "Quail", "Rhinoceros", "Snake", "Toucan",
        "Uakari", "Vulture", "Wallaby", "Xenopus", "Yak",
        "Zebra"
    ]


dic = {name[0]:name for name in words}

user_input = list(input("Please type a word:").upper())
result = []
for letter in user_input:
    word = dic[letter]
    result.append(word)

print(result)