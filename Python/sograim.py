def balanced(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        if str[i] == ')':
            # an empty list is false
            if not stack or stack.pop() != '(':
                print('not balanced')
                return
    # at the end of the string, if we have an empty stack its all good, if not its not balanced
    if not stack:
        print('balanced')
    else:
        print('not balanced')

def balanced2(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            stack.append(str[i])
        if str[i] == ')':
            # an empty list is false
            if not stack or stack.pop() != '(':
                print('not balanced')
                return
        if str[i] == ']':
            if not stack or stack.pop() != '[':
                print('not balanced')
                return
        if str[i] == '}':
            if not stack or stack.pop() != '{':
                print('not balanced')
                return
    # at the end of the string, if we have an empty stack its all good, if not its not balanced
    if not stack:
        print('balanced')
    else:
        print('not balanced')


def balanced3(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[' or str[i] == '{':
            stack.append(str[i])
        if str[i] == ')' or str[i] == ']' or str[i] == '}':
            # an empty list is false
            char = stack.pop()
            if not stack or (char != '(' and char != '[' and char != '{'):
                print('not balanced')
                print(str[i])
                print(i)
                print(char)
                print(stack)
                return
    # at the end of the string, if we have an empty stack its all good, if not its not balanced
    if not stack:
        print('balanced')
    else:
        print('not balanced')


if __name__ == "__main__":
    balanced3("[[{}]]")

