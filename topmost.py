import wordfreq
import sys
import urllib.request

def main():
    importedStopWords = open(sys.argv[1])
    stopWords = [line.strip() for line in importedStopWords] # convert the text file to a list
    importedStopWords.close() # close the file as soon as possible

    isLocal = False # keeps track if the file is local, so it needs to be closed or not
    global text  # keeping text local so it can be set inside the if statement
    input = sys.argv[2]
    if input[0:7] == "http://" or input[0:8] == "https://":
        response = urllib.request.urlopen(input)
        text = response.read().decode("utf8").splitlines()
    else:
        text = open(sys.argv[2])
        isLocal = True

    n = int(sys.argv[3])

    words = wordfreq.tokenize(text)

    frequencies = wordfreq.countWords(words, stopWords)

    wordfreq.printTopMost(frequencies, n)

    if isLocal:
        text.close()

main()