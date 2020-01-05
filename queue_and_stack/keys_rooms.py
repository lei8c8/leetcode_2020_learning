class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False for _ in range(len(rooms))]
        seen[0], stack = True, [0]
        while stack:
            room_num = stack.pop()
            for room in rooms[room_num]:
                if not seen[room]:
                    stack.append(room)
                    seen[room] = True 
        return all(seen)

