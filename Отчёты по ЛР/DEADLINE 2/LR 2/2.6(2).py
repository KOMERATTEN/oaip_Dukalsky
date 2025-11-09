n = int(input())

spiral = [[0] * n for _ in range(n)]

x = n // 2
y = n // 2

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0

step_length = 1
step_count = 0
segment_count = 0

for i in range(1, n * n + 1):
    spiral[x][y] = i
    
    dx, dy = directions[direction]
    x += dx
    y += dy
    step_count += 1
    
    if step_count == step_length:
        step_count = 0
        segment_count += 1
        direction = (direction + 1) % 4
        
        if segment_count == 2:
            segment_count = 0
            step_length += 1

for row in spiral:
    for num in row:
        print(num, end=" ")
    print()