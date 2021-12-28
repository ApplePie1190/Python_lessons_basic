import random


def get_jokes(n, flag=False):
    """generator jokes with repeat flag"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    for i in range(n):
        if flag:
            index_nouns = random.randrange(len(nouns))
            index_adverbs = random.randrange(len(adverbs))
            index_adjectives = random.randrange(len(adjectives))
            joke_list.append(f'{nouns[index_nouns]} {adverbs[index_adverbs]} {adjectives[index_adjectives]}')
            nouns.pop(index_nouns)
            adverbs.pop(index_adverbs)
            adjectives.pop(index_adjectives)
        else:
            joke_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')

    print(joke_list)


get_jokes(3)
get_jokes(3, True)
