def same(s1, s2):

    if s1 == s2:
        return True

    if len(s1) % 2:
        return False

    n = (int) (len(s1) / 2)
    a1 = s1[0:n]
    a2 = s1[n:len(s1)]

    b1 = s2[0:n]
    b2 = s2[n:len(s1)]

    return (same(a1, b2) and same(a2, b1)) or (same(a1, b1) and same(a2, b2))

if __name__ == '__main__':
    a = input()
    b = input()

    print ("YES" if same(a, b) else "NO")

