class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set(["startGene"])
        def oneChange(old, new) -> bool:
            changes = 0
            for i in range(len(old)):
                if old[i] != new[i]:
                    changes += 1
            
            return changes == 1

        q = collections.deque()
        q.append(startGene)
        steps = 0
        while q:
            length = len(q)
            # print(q)
            for i in range(length):
                checkgene = q.popleft()
                if checkgene in bank:
                    bank.remove(checkgene)
                if checkgene == endGene:
                    return steps
                # c = 0
                # while c < len(bank):
                #     if bank[c] in visited:
                #         bank.pop(c)
                #     else:
                #         if oneChange(checkgene, bank[c]):
                #             q.append(bank[c])
                #             visited.add(bank[c])
                #             c += 1
                for c in range(len(bank)):
                    if oneChange(checkgene, bank[c]):
                        q.append(bank[c])
                        visited.add(bank[c])
                
            steps += 1

        return -1


        