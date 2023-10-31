def word_count(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts
input_string = input()
result = word_count(input_string)
for word, count in result.items():
    print(word, count)