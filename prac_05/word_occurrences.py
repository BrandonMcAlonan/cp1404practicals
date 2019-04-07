word_to_length = {}
length_words = 0

string = str(input("Please enter some text: "))
words = string.split()
words.sort()

for word in words:
    amount = word_to_length.get(word, 0)
    word_to_length[word] = amount + 1

for word_length in word_to_length.keys():
    if len(word_length) > length_words:
        length_words = len(word_length)

words = list(word_to_length.keys())


print("Text: {}".format(string))
for strings, lengths in word_to_length.items():
    print("{:{}} : {}".format(strings, length_words, lengths))
