class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_mapping = dict(knowledge)

        construct_string = ''
        intermediate = ''
        for char in s:
            if char == '(':
                construct_string += intermediate
                intermediate = ''
                continue

            if char == ')':
                construct_string += knowledge_mapping.get(intermediate, '?')
                intermediate = ''
                continue
            
            intermediate += char
        construct_string += intermediate

        return construct_string
