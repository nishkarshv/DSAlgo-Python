'''
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return path
        stack=[]
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p=="." or not p:
                continue
            else:
                stack.append(p)
        res = "/"+"/".join(stack)
        return res
path = "/home/"
print(Solution().simplifyPath(path))