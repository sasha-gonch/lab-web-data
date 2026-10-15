#!/usr/bin/python3
import json
import matplotlib
matplotlib.use('Agg')   # saves files without opening a window
import matplotlib.pyplot as plt

# required five plus your three picks (replace the last three with yours)
PHRASES = ['obama', 'trump', 'mexico', 'russia', 'fake news',
           'wall', 'jobs', 'freedom']


def load_tweets():
    tweets = []
    for year in range(2009, 2019):
        with open(f'master_{year}.json', encoding='utf-8') as f:
            tweets.extend(json.load(f))
    return tweets


def message(tweet):
    return tweet.get('full_text') or tweet['text']


def count_phrases(tweets, phrases):
    counts = {p: 0 for p in phrases}
    for tweet in tweets:
        text = message(tweet).lower()
        for p in phrases:
            if p.lower() in text:     # once per tweet per phrase
                counts[p] += 1
    return counts


def main():
    tweets = load_tweets()
    total = len(tweets)
    print(total)

    counts = count_phrases(tweets, PHRASES)
    for p in sorted(counts):
        print(p, counts[p])

    # percent = 100 * count / total, computed from the input, never hardcoded
    percents = {p: (100 * counts[p] / total if total else 0.0) for p in counts}

    width = max(17, max(len(p) for p in PHRASES))
    print(f'| {"phrase":<{width}} | {"percent of tweets":<17} |')
    print(f'| {"-" * width} | {"-" * 17} |')
    for p in sorted(percents):
        pct = f'{percents[p]:05.2f}'
        print(f'| {p:>{width}} | {pct:<17} |')

    ordered = sorted(percents)
    plt.figure(figsize=(8, 5))
    plt.barh(ordered, [percents[p] for p in ordered])
    plt.gca().invert_yaxis()
    plt.xlabel('percent of tweets')
    plt.title('Phrase frequency in tweets')
    plt.tight_layout()
    plt.savefig('tweets.png')


if __name__ == '__main__':
    main()