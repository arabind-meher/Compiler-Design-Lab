def re_to_postfix(re):
    postfix = []
    stack = []

    for i in re:
        if i == 'a' or i == 'b':
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    postfix.append(stack.pop())
        elif i == '*':
            while True:
                if len(stack) == 0:
                    stack.append(i)
                    break
                elif stack[-1] == '*':
                    postfix.append(stack.pop())
                else:
                    stack.append(i)
                    break
        elif i == '+':
            while True:
                if len(stack) == 0:
                    stack.append(i)
                    break
                elif stack[-1] == '*' or stack[-1] == '+':
                    postfix.append(stack.pop())
                else:
                    stack.append(i)
                    break
        elif i == '.':
            while True:
                if len(stack) == 0:
                    stack.append(i)
                    break
                elif stack[-1] == '*' or stack[-1] == '+' or stack[-1] == '.':
                    postfix.append(stack.pop())
                else:
                    stack.append(i)
                    break
        else:
            continue

    while len(stack):
        postfix.append(stack.pop())

    print(''.join(postfix))
    return ''.join(postfix)


def display(q0, x, q1):
    print(str(q0) + '-->' + x + '-->' + str(q1))


def to_nfa(re):
    start = []
    last = []
    for _ in range(10):
        start.append(0)
        last.append(0)
    x = 0
    i = -1
    s = 0
    l = 0

    for _ in re:
        if _ == 'a':
            i = i + 1
            start[i] = x
            x = x + 1
            last[i] = x
            x = x + 1
            display(start[i], _, last[i])

        elif _ == 'b':
            i = i + 1
            start[i] = x
            x = x + 1
            last[i] = x
            x = x + 1
            display(start[i], _, last[i])

        elif _ == '+':
            s = x
            x = x + 1
            l = x
            x = x + 1

            display(s, 'e', start[i])
            display(s, 'e', start[i - 1])
            display(last[i], 'e', l)
            display(last[i - 1], 'e', l)

            i = i - 1
            start[i] = s
            last[i] = l

        elif _ == '.':
            display(last[i - 1], 'e', start[i])
            last[i - 1] = last[i]
            i = i - 1

        elif _ == '*':
            s = x
            x = x + 1
            l = x
            x = x + 1

            display(s, 'e', start[i])
            display(s, 'e', l)
            display(last[i], 'e', start[i])
            display(last[i], 'e', l)

            start[i] = s
            last[i] = l

        else:
            continue

    print(i, start[i], last[i])


if __name__ == '__main__':
    re_expression = input('Enter the regular expression: ')
    re_postfix = re_to_postfix(re_expression)
    to_nfa(re_postfix)
