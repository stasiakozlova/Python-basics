import itertools
import random

import pymorphy2
from tqdm import tqdm

morph = pymorphy2.MorphAnalyzer()


def get_pairs(number_of_words_to_take: int = 10000):
    with open("rus_shuffled.txt", 'r', encoding="utf-8") as file:
        lines = file.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    nouns = []
    adjectives = []

    def categorize_by_parts_of_speech(word: str):
        match = morph.parse(word)[0]

        if match.tag.POS == "NOUN":
            nouns.append(match.normal_form)

        elif match.tag.POS == "ADJF":
            adjectives.append(match.normal_form)

    list(map(categorize_by_parts_of_speech, tqdm(lines[:number_of_words_to_take])))

    return itertools.product(adjectives, nouns)


def print_corrected_pairs(pairs, number_of_pairs_to_print: int):
    pairs = list(pairs)
    random.shuffle(pairs)

    for adjective, noun in pairs[:number_of_pairs_to_print]:
        noun = morph.parse(noun)[0]
        adjective = morph.parse(adjective)[0]

        if noun is not None and adjective is not None:
            if noun.tag.gender is not None:
                adjective = adjective.inflect({noun.tag.gender})
                print(adjective.word, noun.word)


def main():
    pairs = get_pairs(number_of_words_to_take=1000)
    print_corrected_pairs(pairs, number_of_pairs_to_print=1000)


if __name__ == '__main__':
    main()
