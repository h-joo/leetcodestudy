# https://leetcode.com/problems/vowel-spellchecker/description/
from string import ascii_lowercase 
from itertools import chain

VOWELS = set(["a", "e", "i", "o", "u"])
vowel_transform_dict = {ch: (ch if ch not in VOWELS else "a") for ch in chain(ascii_lowercase) }
def transform_vowel(string):
    return "".join([vowel_transform_dict[ch] for ch in string])

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        query_results = []

        exact = set(wordlist)
        capital_transformed = {}
        vowel_transformed = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in capital_transformed:
                capital_transformed[lower] = word

            vowel_normalized = transform_vowel(lower)
            if vowel_normalized not in vowel_transformed:
                vowel_transformed[vowel_normalized] = word

        for query in queries:
            if query in exact:
                query_results.append(query)
                continue
            lower = query.lower()
            capital = capital_transformed.get(lower)
            if capital is not None:
                query_results.append(capital)
                continue

            vowel = vowel_transformed.get(transform_vowel(lower))
            if vowel is not None:
                query_results.append(vowel)
                continue

            query_results.append("")            

        return query_results
