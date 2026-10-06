#Approach
# Create an empty stack.
# Go through the string character by character.
# If it is an opening bracket (, {, or [, push it into the stack.
# If it is a closing bracket:
# Return false if the stack is empty.
# Take the top bracket from the stack.
# Check if it matches the current closing bracket.
# If it does not match, return false.
# After checking all characters:
# If the stack is empty, return true.
# Otherwise, return false because some opening brackets are still unmatched.
# Direct Comparison
# Method	Syntax	Best Used For
# not stack	if not stack:	Standard Python lists ([]) and deque objects. This is the fastest and most readable method.
# len(stack) == 0	if len(stack) == 0:	Custom class definitions or situations where you want to be completely explicit about size checks.
# .empty()	if stack.empty():	Thread
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '({[':
                st.append(c)
            else:
                if not st:
                    return False
                top = st.pop()
                if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                    return False
        if not st:
            return True
        else:
            return False


        