from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26

        max_count = 0

        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            max_count = max(max_count, freq[ord(task) - ord('A')])
        
        time = (max_count - 1) * (n + 1)

        for i in range(26):
            if freq[i] == max_count:
                time += 1

        return max(time, len(tasks))



            


