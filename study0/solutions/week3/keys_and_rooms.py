class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        to_visit = [0]

        while to_visit:
            current_node = to_visit.pop()
            visited.add(current_node)
            for key in rooms[current_node]:
                if key not in visited:
                    to_visit.append(key)
        return len(visited) == len(rooms)
