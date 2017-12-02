import pprint
pp = pprint.PrettyPrinter(indent=4)


def get_square(grid, x, y):
    return next(
        (s for s in grid if s['x'] == x and s['y'] == y),
        None
    )


def get_walkable(squares):
    return [x for x in squares if x["walkable"]]


def compact(y):
    return [x for x in y if x is not None]


def get_adjacent_walkable(grid, square):
    x = square['x']
    y = square['y']

    up = get_square(grid, x, y + 1)
    down = get_square(grid, x, y - 1)
    left = get_square(grid, x - 1, y)
    right = get_square(grid, x + 1, y)

    return get_walkable(compact([up, down, left, right]))


def build_empty_grid(n):
    grid = []
    for y in range(0, n):
        for x in range(0, n):
            grid.append(
                {
                    "cat": False,
                    "walkable": True,
                    "x": x,
                    "y": y,
                    "tuna": False,
                }
            )
    return grid


def get_distance(a, b):
    return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])


def get_closest_fdist_square(square_list):
    lowest_square = square_list[-1]
    lowest_f = lowest_square["f"]

    for square in square_list:
        if square["f"] < lowest_f:
            lowest_f = square["f"]
            lowest_square = square

    return lowest_square


def remove_square(square_list, square):
    return [x for x in square_list if not (
        x["x"] == square["x"] and x["y"] == square["y"]
    )]


open_list = []
closed_list = []
path = []

# Build the empty grid.
grid = build_empty_grid(6)

# Set unwalkable tiles.
get_square(grid, 1, 1)["walkable"] = False
get_square(grid, 3, 1)["walkable"] = False
get_square(grid, 3, 2)["walkable"] = False
get_square(grid, 3, 3)["walkable"] = False
get_square(grid, 3, 4)["walkable"] = False

# Insert the tuna
tuna_square = get_square(grid, 5, 1)
tuna_square["tuna"] = True

# Insert the cat
cat_square = get_square(grid, 1, 2)
cat_square["cat"] = True
cat_square["g"] = 0
cat_square["h"] = get_distance(cat_square, tuna_square)
cat_square["f"] = cat_square["g"] + cat_square["h"]

iteration = 0
current_square = cat_square

while current_square is not tuna_square:
    iteration = iteration + 1
    closed_list.append(current_square)
    adjacent_walkable = get_adjacent_walkable(grid, current_square)

    for square in adjacent_walkable:
        if square not in open_list:
            open_list.append(square)

    for square in closed_list:
        if square in open_list:
            open_list = remove_square(open_list, square)

    for square in open_list:
        square["g"] = get_distance(cat_square, square)
        square["h"] = get_distance(square, tuna_square)
        square["f"] = square["g"] + square["h"]

    current_square = get_closest_fdist_square(open_list)

closed_list.append(tuna_square)
print("Yay! The cat got the tuna! Path: ")
pp.pprint(closed_list)
