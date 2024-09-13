
def solve(test_case):

    sorted_list = sorted(test_case, key=lambda x: (-x[1], x[2], x[0]))
    sorted_attackers = []
    sorted_defenders = []
    for i in range(5):
        sorted_attackers.append(sorted_list[i][0])
        sorted_defenders.append(sorted_list[5+i][0])

    sorted_attackers = sorted(sorted_attackers)
    sorted_defenders = sorted(sorted_defenders)

    print("(", end="")
    print(', '.join(sorted_attackers), end="")
    print(")")

    print("(", end="")
    print(', '.join(sorted_defenders), end="")
    print(")")

if __name__ == '__main__':
    n_cases = int(input())
    test_cases = []

    for j in range(n_cases):
        players = []
        test_cases.append(players)
        for i in range(10):
            player = input().split()
            players.append((player[0], int(player[1]), int(player[2])))

    for i in range(n_cases):
        print("Case " + str(i + 1) + ":")
        solve(test_cases[i])
