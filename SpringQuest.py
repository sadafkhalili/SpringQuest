import random
from collections import deque

MAX_N = 100
grid = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]
visited = [[False] * (MAX_N + 1) for _ in range(MAX_N + 1)]
n = 0
start = (1, 1)
goal = (0, 0)
spring = (-1, -1)
spring_steps = 0
spring_direction = 0
path = [(0, 0)] * (MAX_N * MAX_N)
path_length = 0

# جهت‌های حرکت (۸ جهت شامل جهات قطری)
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def random_int(min_val, max_val):
    return random.randint(min_val, max_val)

def generate_grid():
    global goal, spring, spring_steps, spring_direction
    
    # تولید موقعیت هدف
    goal = (random_int(1, n), random_int(1, n))
    
    # تولید موانع
    p = random_int(1, n)  # تعداد موانع
    for _ in range(p):
        x = random_int(1, n)
        y = random_int(1, n)
        if (x != start[0] or y != start[1]) and (x != goal[0] or y != goal[1]):
            grid[x][y] = -1  # علامتگذاری مانع
    
    # تولید فنر
    if random_int(1, 100) <= 30:  # با احتمال 30 درصد
        spring = (random_int(1, n), random_int(1, n))
        spring_steps = random_int(1, n // 2)  # تعداد گامها
        spring_direction = random_int(0, 7)  # جهت حرکت (۸ جهت)
        if spring != start and spring != goal:
            grid[spring[0]][spring[1]] = 4  # علامت فنر
    
    # تولید تونل
    tunnel = (random_int(1, n), random_int(1, n))
    if tunnel != start and tunnel != goal:
        grid[tunnel[0]][tunnel[1]] = 5  # علامت تونل

def is_valid(x, y):
    return (1 <= x <= n and 
            1 <= y <= n and 
            grid[x][y] != -1 and 
            not visited[x][y])

def find_path():
    global path_length
    
    s = deque()
    s.append(start)
    
    while s:
        x, y = s.pop()
        
        # ثبت موقعیت فعلی در مسیر
        path[path_length] = (x, y)
        path_length += 1
        
        if x == goal[0] and y == goal[1]:
            return True  # مسیر پیدا شد
        
        visited[x][y] = True
        
        # spring
        if spring[0] == x and spring[1] == y:
            for i in range(spring_steps):
                x += dx[spring_direction]
                y += dy[spring_direction]
                if not is_valid(x, y):
                    break
        
        # Tunnel
        if grid[x][y] == 5:
            for i in range(3):
                if path_length > 0:
                    path_length -= 1
            if path_length > 0:
                x, y = path[path_length - 1]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_valid(nx, ny):
                s.append((nx, ny))
    
    return False

def print_grid():
    print("Grid: ")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == start[0] and j == start[1]:
                print("S", end="")
            elif i == goal[0] and j == goal[1]:
                print("G", end="")
            elif grid[i][j] == 4:
                print("F", end="")
            elif grid[i][j] == 5:
                print("T", end="")
            else:
                print("*", end="")
        print()

def print_path():
    print(" [", end="")
    for i in range(path_length):
        print(f"({path[i][0]}, {path[i][1]})", end="")
        if i != path_length - 1:
            print(" --> ", end="")
    print("]")

def main():
    global n
    
    n = int(input("Enter n: "))
    if n < 6:
        print("It must be at least 6.")
        return
    
    generate_grid()
    print_grid()
    
    if find_path():
        print("Path Found!")
        print_path()

if __name__ == "__main__":
    main()


