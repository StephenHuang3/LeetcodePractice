class Solution:
    def validPalindrome(self, s: str) -> bool:
        breakpoint = -1
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                breakpoint = i
                break
        
        if breakpoint == -1:
            return True

        print("breakpoint")
        print(breakpoint)

        found_left = True
        found_right = True

        for i in range(breakpoint, len(s) // 2):
            if s[i + 1] != s[-i - 1]:
                found_left = False
                break

        for i in range(breakpoint, len(s) // 2):
            if s[i] != s[-i - 2]:
                found_right = False
                print("i")
                print(i)
                print(s[-i - 2]) 
                break
        
        return found_left or found_right
