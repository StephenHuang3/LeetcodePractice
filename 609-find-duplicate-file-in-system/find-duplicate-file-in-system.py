from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content2paths = defaultdict(list)

        for path in paths:
            files = path.split(" ")
            path = files[0]
            
            for file in files[1:]:
                name_content = file.split("(")
                file_name = name_content[0]
                contents = name_content[1][:-1]
                file_output = path + '/' + file_name
                content2paths[contents].append(file_output)

        ret = []

        for content, paths in content2paths.items():
            if len(paths) >= 2:
                ret.append(paths)

        return ret