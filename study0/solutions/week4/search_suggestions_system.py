import queue

def keep_first_three(word_list):
    word_list.sort()
    if len(word_list) > 3:
        del word_list[3:]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        lists_to_sort = []
        trie = {}
        for product in products:
            current_sub_trie = trie
            for char in product:
                if char not in current_sub_trie:
                    current_sub_trie[char] = {'words':[]}
                    lists_to_sort.append(current_sub_trie[char]['words'])
                current_sub_trie[char]['words'].append(product)
                current_sub_trie = current_sub_trie[char]
        
        for one_list in lists_to_sort:
            keep_first_three(one_list)
                    
        
        current_sub_trie = trie
        suggested_products_after_char = []

        for i, char in enumerate(searchWord):
            if char not in current_sub_trie:
                suggested_products_after_char.extend([[] for remaining_char in range(i, len(searchWord))])
                break
            current_sub_trie = current_sub_trie[char]
            suggested_products_after_char.append(current_sub_trie['words'])

        return suggested_products_after_char
