from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        q = deque()
        max_count = 0
        max_count_freq = 0
        for key, val in c.items():
            if val > max_count:
                max_count = val
                max_count_freq = 1
            elif val == max_count:
                max_count_freq += 1

        ans = (max_count - 1) * (n + 1) + max_count_freq
        return max(ans, len(tasks))
