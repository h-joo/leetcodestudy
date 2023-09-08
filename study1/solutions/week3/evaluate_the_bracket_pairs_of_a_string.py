# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/description/
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge_mapping = dict(knowledge)

        words = []
        start = 0
        for i, char in enumerate(s):
            if char == '(':
                words.append(s[start:i])
                start = i + 1
                continue

            if char == ')':
                words.append(knowledge_mapping.get(s[start:i], '?'))
                start = i + 1
                continue
            

        words.append(s[start:i + 1])

        return "".join(words)