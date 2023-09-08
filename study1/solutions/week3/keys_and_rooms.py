# https://leetcode.com/problems/keys-and-rooms/description/
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        to_visit = [0]

        while to_visit:
            current_node = to_visit.pop()
            for key in rooms[current_node]:
                if key not in visited:
                    to_visit.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)
