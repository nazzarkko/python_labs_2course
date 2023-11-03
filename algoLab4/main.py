


def min_knight_moves(SIZE, start, destination):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]

    visited = [[0] * SIZE for _ in range(SIZE)]

    queue = [(start[0], start[1], 0)]
    visited[start[0]][start[1]] = 1

    while queue:
        x, y, dist = queue.pop(0)

        if (x, y) == destination:
            return dist

        for i in range(SIZE):
            next_x = x + row[i]
            next_y = y + col[i]

            if 0 <= next_x < SIZE and 0 <= next_y < SIZE and not visited[next_x][next_y]:
                queue.append((next_x, next_y, dist + 1))
                visited[next_x][next_y] = 1

    return -1


def reading_file():
    with open("input.txt", "r") as file:
        size_line = file.readline().strip()
        SIZE = int(size_line.split(',')[0])
        start = tuple(map(int, file.readline().strip().split(", ")))
        destination = tuple(map(int, file.readline().strip().split(", ")))
    return SIZE, start, destination


def write_result(result):
    with open("output.txt", "w") as file:
        file.write(f"The minimal number of moves is {str(result)}")


if __name__ == "__main__":
    SIZE, start, destination = reading_file()
    result = min_knight_moves(SIZE, start, destination)
    write_result(result)
