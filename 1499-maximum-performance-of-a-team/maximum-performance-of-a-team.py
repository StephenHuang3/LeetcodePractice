import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        hp = []
        total_speed = 0
        max_score = 0
        MOD = 10**9 + 7

        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heapq.heappush(hp, s)
            total_speed += s
            if len(hp) > k:
                total_speed -= heapq.heappop(hp)

            max_score = max(max_score, total_speed * e)

        return max_score % MOD