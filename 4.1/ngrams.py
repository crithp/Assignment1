import re

# Change target article here
ARTICLE = 'article1.txt'


if __name__ == "__main__":
    article_text = None

    with open(ARTICLE, 'r+') as infile:
        article_text = infile.read()

    # Remove punctuation except spaces and convert line breaks to spaces
    cleaned = re.sub(r".\n", ' ', article_text)
    cleaned = re.sub(r"[^A-z ]", '', cleaned)
    # Split words and make all lowercase
    words = [x.lower() for x in cleaned.split()]
    total_words = len(words)

    # Get unigrams with counts
    unigrams = {}

    for word in words:
        if word not in unigrams:
            unigrams[word] = 0

        unigrams[word] += 1

    # Sort so we can better understand valuable unigrams
    unigrams = {w: unigrams[w] for w in sorted(unigrams, key=unigrams.get, reverse=True)}

    # Get bigrams with counts
    bigrams = {}

    for i in range(0, total_words - 1):
        bigram = (words[i], words[i + 1])

        if bigram not in bigrams:
            bigrams[bigram] = 0

        bigrams[bigram] += 1

    # Sort so we can better understand valuable unigrams
    bigrams = {w: bigrams[w] for w in sorted(bigrams, key=bigrams.get, reverse=True)}

    print("Unigrams: ")
    print(unigrams)
    print("\n\n\n")
    print("Bigrams: ")
    print(bigrams)
