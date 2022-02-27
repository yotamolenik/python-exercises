if __name__ == "__main__":
    str = input()
    openers = ['(', '[', '{']
    closers = [')', ']', '}']
    stack = []
    flag = True
    for c in str:
        if c in openers:
            stack.append(c)
        if c in closers:
            if not stack:
                print('not balanced')
                flag = False
            else:
                ch = stack.pop()
                if ch not in openers or closers[openers.index(ch)] != c:
                    print('not balanced')
                    flag = False
    if (flag):
        print('balanced')
    else:
        print('not a balamced string')