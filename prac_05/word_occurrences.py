text = input("Text: ")
word_list = {}
for word in text.split():
    if word in word_list:
        word_list[word] += 1
    else:
        word_list[word] = 1
word_width = max(len(word) for word in word_list.keys())
for word, number in sorted(word_list.items()):
    print(f"{word:{word_width}} : {number}")
