class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        spots = 1
        nodes = preorder.split(",")

        for node in nodes:
            spots -= 1
            if spots < 0:
                return False
            if node != "#":
                spots += 2
        # print(spots)
        return spots == 0