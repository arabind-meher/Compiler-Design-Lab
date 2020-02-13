if __name__ == '__main__':
    s = input('Enter Non-Terminals who have left recursion: ')
    n = len(s)
    d = {}
    l = []

    for i in s:
        a = input('\nEnter the production for {0}: '.format(i))
        d[i] = a

    print('\nBefore Left Recursion: ')
    for i in s:
        a = d[i]
        l = a.split()

        p = i + ' -> ' + ' | '.join(l)
        print(p)

    print('\nAfter Left Recursion: ')
    for i in s:
        a = d[i]
        l = a.split()
        for j in range(len(l)):
            if i in l[j]:
                if len(l[j]) == 2:
                    p = i + "' -> " + l[j][1] + l[j][0] + "' | " + u'\u03B5'
                    print(p)
                elif len(l[j]) == 3:
                    p = i + "' -> " + l[j][1] + l[j][2] + l[j][0] + "' | " + u'\u03B5'
                    print(p)
            else:
                p = i + " -> " + l[j][0] + i + "'"
                print(p)
        print()
