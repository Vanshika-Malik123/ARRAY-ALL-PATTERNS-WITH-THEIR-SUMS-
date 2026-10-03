#so this is a question of stack here in this question what we do is check if stack has element and if stack has element then see if the top of the elemnt is equal to the charavter if it is equal then remove the elemetn and if it is not equal to the elemtn then add in the stack .
#and if the elemnt does not have any item then do si ple add itme in stack 

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return ''.join(stack) 

        