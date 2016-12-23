import heapq


class Cell(object):
    def __init__(self, x, y, reachable):
        """Initialize new cell.

        @param reachable is cell reachable? not a wall?
        @param x cell x coordinate
        @param y cell y coordinate
        @param g cost to move from the starting cell to this cell.
        @param h estimation of the cost to move from this cell
                 to the ending cell.
        @param f f = g + h
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


class AStar(object):
    allow_diagonal_transition = False
    allow_closest_cell_for_unreachable_end = False

    def __init__(self):
        # open list
        self.opened = []
        heapq.heapify(self.opened)
        # visited cells list
        self.closed = set()
        # grid cells
        self.cells = []
        self.grid_height = None
        self.grid_width = None
        self.start = None
        self.end = None

    def init_grid(self, width, height, walls, start, end):
        """Prepare grid cells, walls.

        @param width grid's width.
        @param height grid's height.
        @param walls list of wall x,y tuples.
        @param start grid starting point x,y tuple.
        @param end grid ending point x,y tuple.
        """
        self.grid_height = height
        self.grid_width = width
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x, y, reachable))
        self.start = self.get_cell(*start)
        self.end = self.get_cell(*end)

    def get_heuristic(self, cell):
        """Compute the heuristic value H for a cell.

        Distance between this cell and the ending cell multiply by 10.

        @returns heuristic value H
        """
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x, y):
        """Returns a cell from the cells list.

        @param x cell x coordinate
        @param y cell y coordinate
        @returns cell
        """
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell, r=1):
        """Returns adjacent cells to a cell.

        Clockwise starting from the one on the right.

        @param cell get adjacent cells for this cell
        @param r selection radius
        @returns adjacent cells list.
        """
        cells = []
        if cell.x < self.grid_width - r:
            for y in range(max(0, cell.y - r + 1), min(self.grid_height, cell.y + r)):
                cells.append(self.get_cell(cell.x + r, y))
        if (self.allow_diagonal_transition or r > 1) and cell.x < self.grid_width - r and cell.y > 0:
            cells.append(self.get_cell(cell.x + r, cell.y - r))
        if cell.y > 0:
            for x in range(max(0, cell.x - r + 1), min(self.grid_width, cell.x + r)):
                cells.append(self.get_cell(x, cell.y - r))
        if (self.allow_diagonal_transition or r > 1) and cell.x > 0 and cell.y > 0:
            cells.append(self.get_cell(cell.x - r, cell.y - r))
        if cell.x > 0:
            for y in range(max(0, cell.y - r + 1), min(self.grid_height, cell.y + r)):
                cells.append(self.get_cell(cell.x - r, y))
        if (self.allow_diagonal_transition or r > 1) and cell.x > 0 and cell.y < self.grid_height - r:
            cells.append(self.get_cell(cell.x - r, cell.y + r))
        if cell.y < self.grid_height - r:
            for x in range(max(0, cell.x - r + 1), min(self.grid_width, cell.x + r)):
                cells.append(self.get_cell(x, cell.y + r))
        if (self.allow_diagonal_transition or r > 1) and cell.x < self.grid_width - r and cell.y < self.grid_height - r:
            cells.append(self.get_cell(cell.x + r, cell.y + r))

        return cells

    def get_path(self):
        path, cell = [], None
        if not self.end.reachable or self.end.parent is None:
            if self.allow_closest_cell_for_unreachable_end:
                r, max_r = 1, max(abs(self.start.x - self.end.x), abs(self.start.y - self.end.y))
                while r < max_r:
                    adj_cells = list(filter(lambda c: c.parent is not None, self.get_adjacent_cells(self.end, r)))
                    if len(adj_cells) > 0:
                        cell = min(adj_cells, key=lambda c: c.f)
                        break
                    r += 1
        else:
            cell = self.end

        while cell is not None and cell.parent is not None or cell is self.start:
            path = [(cell.x, cell.y)] + path
            cell = cell.parent

        return path

    def update_cell(self, adj, cell, is_diagonal):
        """Update adjacent cell.

        @param adj adjacent cell to current cell
        @param cell current cell being processed
        @param is_diagonal bool true for diagonal transition
        """
        adj.g = cell.g + (14 if is_diagonal else 10)
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self, allow_diagonal_transition=False, allow_closest_cell_for_unreachable_end=False):
        """Solve maze, find path to ending cell.
        @returns path.
        """
        self.allow_diagonal_transition = allow_diagonal_transition
        self.allow_closest_cell_for_unreachable_end = allow_closest_cell_for_unreachable_end

        if self.start is self.end:
            return [(self.start.x, self.start.y)]

        # add starting cell to open heap queue
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            # pop cell from heap queue
            f, cell = heapq.heappop(self.opened)
            # add cell to closed list so we don't process it twice
            self.closed.add(cell)
            # if ending cell, return found path
            if cell is self.end:
                return self.get_path()
            # get adjacent cells for cell
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    is_diagonal = cell.x != adj_cell.x and cell.y != adj_cell.y
                    # for diagonal transition, check availability of cells around diagonal
                    if is_diagonal:
                        h_cell = self.get_cell(cell.x + (adj_cell.x - cell.x), cell.y)
                        v_cell = self.get_cell(cell.x, cell.y + (adj_cell.y - cell.y))
                        if not h_cell.reachable or not v_cell.reachable:
                            continue

                    if (adj_cell.f, adj_cell) in self.opened:
                        # if adj cell in open list, check if current path is
                        # better than the one previously found
                        # for this adj cell.
                        if adj_cell.g > cell.g + (14 if is_diagonal else 10):
                            self.update_cell(adj_cell, cell, is_diagonal)
                    else:
                        self.update_cell(adj_cell, cell, is_diagonal)
                        # add adj cell to open list
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))

        return self.get_path()