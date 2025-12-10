from collections import defaultdict


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        adj = defaultdict(set)
        for parent, child in edges:
            adj[parent].add(child)
            adj[child].add(parent)

        @cache
        def dp(cur, pre, v):
            if v > 13:
                return 0

            cur_coin = coins[cur] >> v
            op1 = cur_coin - k + sum(dp(child, cur, v) for child in adj[cur] if child != pre)
            if cur_coin >= k + k:
                return op1
            op2 = (cur_coin >> 1) + sum(dp(child, cur, v + 1) for child in adj[cur] if child != pre)
            return max(op1, op2)

        return dp(0, -1, 0)