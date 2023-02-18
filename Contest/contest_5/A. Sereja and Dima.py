

n = int(input())

cards = list(map(int, input().split()))

Sereja = 0
Dima = 0

ptr1 = 0
ptr2 = n-1

ser_turn = True
for _ in range(n):
    if cards[ptr1] > cards[ptr2]:
        num = cards[ptr1]
        ptr1 += 1
    else:
        num = cards[ptr2]
        ptr2 -= 1
    
    if ser_turn:
        Sereja += num
    else:
        Dima += num
    
    ser_turn = not ser_turn

print(Sereja, Dima)

