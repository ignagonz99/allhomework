punct = ",!?"

fd = open("text.txt")

for line in fd:

    for char in punct:

        if char in line:

            line = line.replace(char, "")

    word = line.split()

    longest = ""

    for words in word:

        if len(word)> len(longest):
            longest = words

print(longest)