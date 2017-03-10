import nltk
import twitter
from collections import Counter


def phrase_processing(person, inputs):

    final_phrase = ""
    final_phrase += person + " is "

    adjectives = []

    for phrase in inputs:

        text = nltk.word_tokenize(phrase)

        processed_text = nltk.pos_tag(text)

        for word in processed_text:
            if word[1] == "JJ":
                print(word)
                adjectives.insert(0, word[0])

    print(adjectives)

    count = Counter(adjectives)

    for adjective in count.most_common(5):
        final_phrase += adjective[0] + " "

    return final_phrase


if __name__ == '__main__':

    person = "Obama"

    api = twitter.Api([CREDENTIALS])

    twitterResponseJSON = api.GetSearch(term=person,result_type="tweet",count=1000,lang="EN")

    inputs = []

    for tweet in twitterResponseJSON:
        inputs.insert(0,tweet.text)

    print(phrase_processing(person,inputs))
