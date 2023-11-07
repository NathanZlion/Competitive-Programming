numOfCities, numOfTowers = map(int, input().split())
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))

def closestTower(city, towers):
    left = -1
    right = len(towers)

    while right > left +1:
        mid = left + ((right-left)//2)
        # tower to the right of city
        if towers[mid] > city:
            right = mid
        elif towers[mid] < city:
            left = mid
        else:
            return 0

    closest = abs(towers[0] - city)
    if left > -1:
        closest = min(closest, abs(city-towers[left]))

    if right < len(towers):
        closest = min(closest, abs(towers[right]-city))

    return closest

res = 0
for city in cities:
    res = max(closestTower(city, towers), res)

print(res)