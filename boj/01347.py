# 1347. 미로 만들기
# Link: https://www.acmicpc.net/problem/1347
# Difficulty: Silver 3
# Category: 구현
# Category: 문자열
# Category: 시뮬레이션


# Soltion 1: implementation
# Time: 44 ms
# Memory: 31256 KB
move_by_direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class maze_map:
    def __init__(self):
        self.maze = [['.']]
        self.size = (1, 1)
        self.position = (0, 0)
        self.direction = 0

    def rotation_left(self):
        self.direction = (self.direction - 1) % 4

    def rotation_right(self):
        self.direction = (self.direction + 1) % 4

    def move(self):
        x, y = self.position
        dx, dy = move_by_direction[self.direction]
        size_x, size_y = self.size

        if x + dx < 0:
            self.maze = [['#' for _ in range(size_y)], *self.maze]
            self.size = (size_x + 1, size_y)
            x, y = (x + 1, y)
        if x + dx >= size_x:
            self.maze = [*self.maze, ['#' for _ in range(size_y)]]
            self.size = (size_x + 1, size_y)
        if y + dy < 0:
            self.maze = [['#', *row] for row in self.maze]
            self.size = (size_x, size_y + 1)
            x, y = (x, y + 1)
        if y + dy >= size_y:
            self.maze = [[*row, '#'] for row in self.maze]
            self.size = (size_x, size_y + 1)

        self.position = (x + dx, y + dy)
        self.maze[x + dx][y + dy] = '.'

    def __repr__(self):
        return '\n'.join(''.join(row) for row in self.maze)


_ = int(input())
contents = list(input())

maze = maze_map()
for content in contents:
    if content == 'L':
        maze.rotation_left()
    elif content == 'R':
        maze.rotation_right()
    else:
        maze.move()

print(maze)
