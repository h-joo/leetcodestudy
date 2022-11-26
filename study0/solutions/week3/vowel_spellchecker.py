VOWEL_SET = set(['a', 'e', 'i', 'o', 'u'])

def return_a_if_vowel(char):
    if char in VOWEL_SET:
        return 'a'
    return char

def flatten_vowel(word):
    return ''.join([return_a_if_vowel(char) for char in word])


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        lookup_table = {}
        for original_word in wordlist:
            lower_case = original_word.lower()
            vowel_flattened = flatten_vowel(lower_case)

            if vowel_flattened not in lookup_table:
                lookup_table[vowel_flattened] = ({}, [])

            if lower_case not in lookup_table[vowel_flattened][0]:
                lookup_table[vowel_flattened][0][lower_case] = (set(), [])

            lookup_table[vowel_flattened][0][lower_case][0].add(original_word)
            lookup_table[vowel_flattened][0][lower_case][1].append(original_word)
            lookup_table[vowel_flattened][1].append(original_word)

        query_results = []
        for query in queries:
            lower_case = query.lower()
            vowel_flattened = flatten_vowel(lower_case)

            if vowel_flattened not in lookup_table:
                query_results.append("")
                continue
            
            if lower_case not in lookup_table[vowel_flattened][0]:
                query_results.append(lookup_table[vowel_flattened][1][0])
                continue
            
            if query not in lookup_table[vowel_flattened][0][lower_case][0]:
                query_results.append(lookup_table[vowel_flattened][0][lower_case][1][0])
                continue

            query_results.append(query)
        return query_results
