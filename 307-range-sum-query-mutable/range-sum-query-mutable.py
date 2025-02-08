class Node:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        def createTree(start, end) -> Node:
            if start > end:
                return None
            elif start == end:
                new = Node(start, end)
                new.total = nums[start]
                return new
            
            mid = (start + end) // 2
            new = Node(start, end)
            new.left = createTree(start, mid)
            new.right = createTree(mid + 1, end)
            new.total = new.left.total + new.right.total

            return new

        self.root = createTree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:

        def recursively_update(node, index, val):
            if node.left == node.right:
                node.total = val
                return val

            mid = (node.start + node.end) // 2

            if index <= mid:
                recursively_update(node.left, index, val)
            else:
                recursively_update(node.right, index, val)

            node.total = node.left.total + node.right.total

        return recursively_update(self.root, index, val)



    def sumRange(self, left: int, right: int) -> int:
        def findRange(node, l, r):
            if node.start == l and node.end == r:
                return node.total

            mid = (node.start + node.end) // 2

            if r <= mid:
                return findRange(node.left, l, r)
            elif l > mid:
                return findRange(node.right, l, r)
            else:
                return findRange(node.left, l, mid) + findRange(node.right, mid + 1, r)

        return findRange(self.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)