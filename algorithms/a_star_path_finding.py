import heapq

class Cell(object):
  def __init__(self, x, y, reachable):
    """
    Initialize new cell

    @param x cell x coordinate
    @param y cell y coordinate
    @param reachable is cell reachable? not a wall?
    """
    self.reachable = reachable
    self.x = x
    self.y = y
    self.parent = None
    self.g = 0
    self.h = 0
    self.f = 0

class AStar(object):
  def __init__(self):
    self.op = []
    heapq.heapify(self.op)
    self.cl = set()
    self.cells = []
    self.gridHeight = 6
    self.gridWidth = 6

  def init_grid(self):
    walls = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3), 
             (3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1))
    for x in range(self.gridWidth):
      for y in range(self.gridHeight):
        if (x, y) in walls:
          reachable = False
        else:
          reachable = True
        self.cells.append(Cell(x, y, reachable))
    self.start = self.get_cell(0, 0)
    self.end = self.get_cell(5, 5)

  def get_heuristic(self, cell):
    """
    Compute the heuristic value H for a cell: distance between
    this cell and the ending cell multiply by 10.

    @param cell
    @returns heuristic value H
    """
    return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

  def get_cell(self, x, y):
    """
    Returns a cell from the cells list

    @param x cell x coordinate
    @param y cell y coordinate
    @returns cell
    """
    return self.cells[x * self.gridHeight + y]

  def get_adjacent_cells(self, cell):
    """
    Returns adjacent cells to a cell. Clockwise starting
    from the one on the right.

    @param cell get adjacent cells for this cell
    @returns adjacent cells list 
    """
    cells = []
    if cell.x < self.gridWidth-1:
      cells.append(self.get_cell(cell.x+1, cell.y))
    if cell.y > 0:
      cells.append(self.get_cell(cell.x, cell.y-1))
    if cell.x > 0:
      cells.append(self.get_cell(cell.x-1, cell.y))
    if cell.y < self.gridHeight-1:
      cells.append(self.get_cell(cell.x, cell.y+1))
    return cells

  def display_path(self):
    cell = self.end
    while cell.parent is not self.start:
      cell = cell.parent
      print 'path: cell: %d,%d' % (cell.x, cell.y)

  def compare(self, cell1, cell2):
    """
    Compare 2 cells F values

    @param cell1 1st cell
    @param cell2 2nd cell
    @returns -1, 0 or 1 if lower, equal or greater
    """
    if cell1.f < cell2.f:
      return -1
    elif cell1.f > cell2.f:
      return 1
    return 0
  
  def update_cell(self, adj, cell):
    """
    Update adjacent cell

    @param adj adjacent cell to current cell
    @param cell current cell being processed
    """
    adj.g = cell.g + 10
    adj.h = self.get_heuristic(adj)
    adj.parent = cell
    adj.f = adj.h + adj.g

  def process(self):
    # add starting cell to open heap queue
    heapq.heappush(self.op, (self.start.f, self.start))
    while len(self.op):
      # pop cell from heap queue 
      h, cell = heapq.heappop(self.op)
      # add cell to closed list so we don't process it twice
      self.cl.add(cell)
      # if ending cell, display found path
      if cell is self.end:
        self.display_path()
        break
      # get adjacent cells for cell
      adj_cells = self.get_adjacent_cells(cell)
      for c in adj_cells:
        if c.reachable and c not in self.cl:
          if c in self.op:
            # if adj cell in open list, check if current path is
            # better than the one previously found for this adj cell.
            if c.g > cell.g + 10:
              self.update_cell(c, cell)
          else:
            self.update_cell(c, cell)
            # add adj cell to open list
            heapq.heappush(self.op, (c.f, c))

a = AStar()
a.init_grid()
a.process()

