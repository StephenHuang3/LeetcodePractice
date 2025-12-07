from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        q.append([0,0,0,0,0])
        target_lis = [int(target[0]), int(target[1]), int(target[2]), int(target[3])]
        seen = set()
        seen.add((0,0,0,0))

        for deadend in deadends:
            seen.add((int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])))
            if (int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])) == (0,0,0,0):
                return -1

        while q:
            popped = q.popleft()
            comb = popped[1:]
            print("comparing")
            print(comb)
            print(target_lis)
            if comb == target_lis:
                return popped[0]
            
            for i in range(4):
                new_comb1 = comb.copy()
                new_comb2 = comb.copy()
                nc1 = (comb[i] + 1) % 10
                nc2 = (comb[i] - 1) % 10
                new_comb1[i] = nc1
                new_comb2[i] = nc2
                if (new_comb1[0], new_comb1[1], new_comb1[2], new_comb1[3]) not in seen:
                    seen.add((new_comb1[0], new_comb1[1], new_comb1[2], new_comb1[3]))
                    q.append([popped[0] + 1, new_comb1[0], new_comb1[1], new_comb1[2], new_comb1[3]])

                if (new_comb2[0], new_comb2[1], new_comb2[2], new_comb2[3]) not in seen:
                    seen.add((new_comb2[0], new_comb2[1], new_comb2[2], new_comb2[3]))
                    q.append([popped[0] + 1, new_comb2[0], new_comb2[1], new_comb2[2], new_comb2[3]])

        return -1
                
