// https://leetcode.com/problems/keys-and-rooms/
// Time Complexity: O(n^2)
// Space Complexity: O(n), n: rooms.size()
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Stack<Integer> keyList = new Stack<>();
        List<Boolean> visited = new ArrayList<Boolean>(Collections.nCopies(rooms.size(), false));
        int totalVisited = 0;
        keyList.push(0);
        visited.set(0, true);

        while (!keyList.isEmpty()) {
            int roomIdx = keyList.pop();
            ++totalVisited;
            for (Integer room : rooms.get(roomIdx)) {
                if (!visited.get(room)){
                    keyList.push(room);
                    visited.set(room, true);
                }
            }
        }
        return totalVisited == rooms.size();
    }
}