class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name, _ in sorted(zip(names, heights), key=lambda person: person[1], reverse=True)]
