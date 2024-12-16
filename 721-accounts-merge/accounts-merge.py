from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, num):
        while num != self.par[num]:
            self.par[num] = self.par[self.par[num]]
            num = self.par[num]
        return num

    def union(self, n1, n2):
        n1 = self.find(n1)
        n2 = self.find(n2)

        if n1 == n2:
            return False

        if self.rank[n1] > self.rank[n2]:
            self.rank[n1] += self.rank[n2]
            self.par[n2] = self.par[n1]
        else:
            self.rank[n2] += self.rank[n1]
            self.par[n1] = self.par[n2]

        return True



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}

        for i, emails in enumerate(accounts):
            for em in emails[1:]:
                if em in email_to_account:
                    uf.union(i, email_to_account[em])
                else:
                    email_to_account[em] = i

        email_group = defaultdict(list)
        for em, acc in email_to_account.items():
           email_group[uf.find(acc)].append(em)

        res = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))
        return res