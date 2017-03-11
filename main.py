import nltk
import twitter
from collections import Counter
from os.path import expanduser
from nltk.tag.stanford import StanfordPOSTagger


def phrase_processing(person, inputs):

    home = expanduser("~")

    _path_to_model = home + "/PycharmProjects/Hatemeter/stanford-postagger/models/english-left3words-distsim.tagger" #You need to download and set this up before running
    _path_to_jar = home + "/PycharmProjects/Hatemeter/stanford-postagger/stanford-postagger.jar" #You need to download and set this up before running

    st = StanfordPOSTagger(model_filename=_path_to_model, path_to_jar=_path_to_jar)

    final_phrase = ""
    final_phrase += person + " is "

    adjectives = []

    phrases = []

    for phrase in inputs:
        phrases.insert(0, nltk.word_tokenize(phrase))

    processed_text = st.tag(inputs)

    print(processed_text)

    for word in processed_text:
        if word[1] == "JJ" and len(word[0]) > 2:
            adjectives.insert(0, word[0])

    count = Counter(adjectives)

    for adjective in count.most_common(5):
        final_phrase += adjective[0] + " "

    return final_phrase


if __name__ == '__main__':

    person = "Trump"

    api = twitter.Api([CONFIDENTIAL])

    twitterResponseJSON = api.GetSearch(term=person, count=100)

    inputs = []

    for tweet in twitterResponseJSON:
        if tweet.text not in inputs:
            inputs.insert(0, tweet.text)

    print(phrase_processing(person, inputs))
