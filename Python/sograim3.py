import sys
if __name__ == "__main__":
    str = input()
    openers = ['(', '[', '{']
    closers = [')', ']', '}']
    flag = False
    stack = []
    for c in str:
        if c in openers:
            stack.append(c)
        if c in closers:
            if stack: # stack not empty
                ch = stack.pop()
                if c != closers[openers.index(ch)]:
                    print('not balanced')
                    sys.exit(0)
    if not stack:
        print('stack is empty, so string IS balanced')
    else:
        print('stack is not empty, so string IS NOT balanced')


