// https://leetcode.com/problems/keys-and-rooms/
// Time Complexity: O(n^2)
// Space Complexity: O(n), n: rooms.size()
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        List<Integer> keyList = new ArrayList<>(); // key list which I have.
        boolean[] visited = new boolean[rooms.size()]; // if it is open, then true
        int roomIdx = 0;
        keyList.add(0);

        while (true) {
            System.out.println(roomIdx);
            if (!visited[roomIdx]) {
                // visit the room and pick up key
                keyList.addAll(rooms.get(roomIdx));
                // check unlocked room
                visited[roomIdx] = true;
            }
            keyList.remove(Integer.valueOf(roomIdx));
            if (!keyList.isEmpty()) {    // set the roomIdx to the next room which will be visited
                roomIdx = keyList.get(0);
            } else {
                break;
            }
        }

        for (boolean v : visited) {
            if (!v) {    // if there is room which we can not enter
                return false;
            }
        }

        return true;
    }
}