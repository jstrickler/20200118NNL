
word_data = {}

with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        word = raw_line.rstrip()
        word_length = len(word)
        if word_length > 23:
            print(word)

        if word_length not in word_data:  # is word_length a key?
            word_data[word_length] = 0  # if not, add it

        word_data[word_length] += 1
        # word_data[word_length] = word_data[word_length] + 1

for length, count in sorted(word_data.items(), reverse=True):
    print(length, count)

print(word_data)
