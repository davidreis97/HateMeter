import twitter
import credentials
import urllib.parse
from textblob import TextBlob

query = "merkel"

api = twitter.Api(consumer_key=credentials.consumer_key,
                  consumer_secret=credentials.consumer_secret,
                  access_token_key=credentials.access_token_key,
                  access_token_secret=credentials.access_token_secret)

results = api.GetSearch(raw_query=f"q={urllib.parse.quote(query)}&result_type=recent&count=100&lang=en")

total = 0

occurrences = {}

tagsOfInterest = ["JJ", "JJR", "JJS", "RBR", "RBS", "NN", "NNS", "NP", "NPS", "RP"]
spam = ["https","amp"]

for result in results:
    blob = TextBlob(result.text)
    total += blob.sentiment.polarity * blob.sentiment.subjectivity

    for piece in blob.tags:
        if len(piece[0]) >= 3 and piece[1] in tagsOfInterest and piece[1] not in spam:
            if piece[0] in occurrences:
                occurrences[piece[0]] += 1
            else:
                occurrences[piece[0]] = 1

occurrences = {k: v for k, v in sorted(occurrences.items(), key=lambda item: item[1], reverse=True)}

print(occurrences)