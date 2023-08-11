
def tokenize(lines):
    words = []
    for line in lines:
        line = line.lower()
        start = 0
        while start < len(line):

            if line[start].isspace():
                    start += 1

            elif line[start].isalpha():
                end = start
                while line[end].isalpha():
                    end += 1
                    if end == len(line):
                        break
                words.append(line[start:end])
                start = end

            elif line[start].isdigit():
                end = start
                while line[end].isdigit():
                    end += 1
                    if end == len(line):
                        break
                words.append(line[start:end])
                start = end

            else:
                end = start
                end += 1
                words.append(line[start:end])
                start = end

    return words

def countWords(words, stopWords):
    frequencies = {}
    for word in words:

        if word in stopWords:
            pass

        elif word not in frequencies:
            frequencies[word] = 1

        else:
            count = frequencies[word]
            frequencies[word] = count + 1

    return frequencies

def printTopMost(frequencies,n):
    i = 0 # used to stop the loop at n values
    for word, freq in dict(sorted(frequencies.items(), key=lambda x: -x[1])).items():
        i += 1
        if i > n:
            break
        print(word.ljust(20)+str(freq).rjust(5))
