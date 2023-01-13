class Solution(object):
    def findDuplicate(self, paths):
        same = defaultdict(list)

        for path_list in paths:
            path_list = path_list.split()
            root = path_list[0]
            for file_index in range(1, len(path_list)):
                curr_file = path_list[file_index]
                curr_file = curr_file.split("(")

                curr_file_name = curr_file[0]
                curr_file_content = curr_file[1][:-1]

                same[curr_file_content].append(root +"/" +curr_file_name)
        
        res = []

        for content in same.keys():
            if len(same[content]) > 1:
                res.append(same[content])
            
        return res
