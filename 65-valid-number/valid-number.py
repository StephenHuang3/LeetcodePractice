import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # check valid decimal
        x = re.search("^[+-]?\d+\.?\d*?([eE][+-]?\d+)?$", s)
        y = re.search("^[+-]?\d*\.?\d+?([eE][+-]?\d+)?$", s)

        # z = re.search("^[+-]?(\d+\.?\d*)|(\d*\.?\d+)([eE]\d+\.?\d*?)|([eE]\d*\.?\d+?)?$", s)
        return x or y

        # "^[+-]?(\d+\.?\d*)|(\d*\.?\d+)([eE]\d+\.?\d*?)|([eE]\d*\.?\d+?)?$"