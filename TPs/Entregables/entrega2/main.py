class Building:
    def __init__(self, index, height, width):
        self.index = index
        self.height = height
        self.width = width

class Node:
    def __init__(self, building):
        self.building = building
        self.upper_width = 0
        self.lower_width = building.width
        self.childs = None
        self.lowest_child_height = -1

    def insert(self, building):

        if self.building.height >= building.height:
            return

        if self.lowest_child_height >= building.height:
            child = Node(building)
            child.upper_width = self.upper_width + child.building.width
            self.lower_width = max(self.lower_width, self.upper_width + child.building.width)
            self.lowest_child_height = building.height
            self.childs.append(child)
            return

        if self.childs is None:
            child = Node(building)
            child.upper_width = self.upper_width + child.building.width
            self.childs = [child]
            self.lowest_child_height = building.height
            return

        for c in self.childs:
            c.insert(building)

def longest_subsequence_with_tail(buildings, index, cache):

    if index == 0:
        cache = { index : buildings[index][1] }
    else:
        cache[index] = buildings[index][1]

    for k in range(index):
        if buildings[k][0] >= buildings[index][0]:
            continue
        cache[index] = max(cache[k] + buildings[index][1], cache[index])

    return cache

def solve(buildings):
    cache = None

    for k in range(len(buildings)):
        cache = longest_subsequence_with_tail(buildings, k, cache)

    return max(cache.values())

if __name__ == '__main__':
    n_cases = int(input())
    test_cases = []

    for j in range(n_cases):
        buildings = []
        test_cases.append(buildings)

        n_buildings = int(input())

        buildings_heights = input().split()
        buildings_widths = input().split()

        for i in range(n_buildings):
            buildings.append((int(buildings_heights[i]), int(buildings_widths[i])))

    for i in range(n_cases):
        print("Case " + str(i + 1) + ". ", end="")
        inc, dec = solve(test_cases[i])

        if inc >= dec:
            print("Increasing (" + str(inc) + "). ", end="")
            print("Decreasing (" + str(dec) + ").")
        else:
            print("Decreasing (" + str(dec) + "). ", end="")
            print("Increasing (" + str(inc) + ").")


#
#
#def solve2(buildings):
#
#    nodes = Node(Building(-1, -1, 0))
#
#    for k in range(len(buildings)):
#        nodes.insert(buildings[k])
#
#    print(nodes.upper_width)
#    print(nodes.childs[0].building.height)
#    print(nodes.childs[0].childs[0].building.height)
#    print(nodes.childs[0].childs[0].childs[0].building.height)
#    print(nodes.childs[0].childs[0].childs[1].building.height)
#    print(nodes.childs[0].childs[0].childs[0].childs[0].building.height)
#    print(nodes.childs[0].childs[0].childs[1].childs[0].building.height)
#
#buildings = [
#        Building(0, 1, 1),
#        Building(0, 4, 1),
#        Building(0, 10, 1),
#        Building(0, 5, 1),
#        Building(0, 20, 1),
#]
#
#solve2(buildings)

# def solve(buildings):
#     n_buildings = len(buildings)
# 
#     cache_increasing = [-1] * n_buildings
#     cache_decreasing = [-1] * n_buildings
# 
#     for j in range(n_buildings):
#         max_increasing = 0
#         max_decreasing = 0
# 
#         for i in range(n_buildings - 1 - j, n_buildings):
#             if (buildings[i][0] < buildings[n_buildings - 1 - j][0]):
#                 max_decreasing = max_decreasing if cache_decreasing[i] < max_decreasing else cache_decreasing[i]
# 
#             if (buildings[i][0] > buildings[n_buildings - 1 - j][0]):
#                 max_increasing = max_increasing if cache_increasing[i] < max_increasing else cache_increasing[i]
# 
#         cache_increasing[n_buildings - 1 - j] = buildings[n_buildings - 1 - j][1] + max_increasing
#         cache_decreasing[n_buildings - 1 - j] = buildings[n_buildings - 1 - j][1] + max_decreasing
# 
#     return (max(cache_increasing), max(cache_decreasing))
# 
# if __name__ == '__main__':
#     n_cases = int(input())
#     test_cases = []
# 
#     for j in range(n_cases):
#         buildings = []
#         test_cases.append(buildings)
# 
#         n_buildings = int(input())
# 
#         buildings_heights = input().split()
#         buildings_widths = input().split()
# 
#         for i in range(n_buildings):
#             buildings.append((int(buildings_heights[i]), int(buildings_widths[i])))
# 
#     for i in range(n_cases):
#         print("Case " + str(i + 1) + ". ", end="")
#         inc, dec = solve(test_cases[i])
# 
#         if inc >= dec:
#             print("Increasing (" + str(inc) + "). ", end="")
#             print("Decreasing (" + str(dec) + ").")
#         else:
#             print("Decreasing (" + str(dec) + "). ", end="")
#             print("Increasing (" + str(inc) + ").")

