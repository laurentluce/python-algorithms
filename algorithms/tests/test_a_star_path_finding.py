import algorithms.a_star_path_finding as pf

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        pass

    @staticmethod
    def draw(sketch):
        for r in sketch:
            print(r)
        print()

    @staticmethod
    def to_sketch(walls, path):
        w = 0
        h = 0
        for c in walls + path:
            if c[0] + 1 > w:
                w = c[0] + 1
            if c[1] + 1 > h:
                h = c[1] + 1
        world = [[" "] * w for _ in range(h)]
        for c in walls:
            world[c[1]][c[0]] = '#'
        for p in path:
            world[p[1]][p[0]] = '.'
        return map(lambda r: "".join(r), world)

    @staticmethod
    def from_sketch(sketch):
        walls = []
        path = []
        start = None
        end = None
        y = 0
        for r in sketch:
            x = 0
            for c in r:
                if c == '.':
                    path.append((x, y))
                if c == '#':
                    walls.append((x, y))
                if c == '[':
                    start = (x, y)
                    path.append((x, y))
                if c == ']':
                    end = (x, y)
                    path.append((x, y))
                if c == '(':
                    start = (x, y)
                if c == ')':
                    end = (x, y)
                x += 1
            y += 1
        return walls, path, start, end

    def assertPathEquals(self, walls, expected_path, path):
        try:
            self.assertEqual(sorted(path), sorted(expected_path))
        except AssertionError:
            print("expected")
            self.draw(self.to_sketch(walls, expected_path))
            print("given")
            self.draw(self.to_sketch(walls, path))
            self.fail()

    def test_maze(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[#    ",
            ".# ###",
            ".. #  ",
            " .#...",
            " ...#.",
            "## # ]",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve())

    def test_maze_diagonal(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[#    ",
            ".# ###",
            ". #...",
            " .#.#.",
            " ...#.",
            "## # ]",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve(True))

    def test_maze_no_walls(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[...  ",
            "   .  ",
            "   .. ",
            "    . ",
            "    . ",
            "    .]",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve())

    def test_maze_no_walls_diagonal(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[     ",
            " .    ",
            "  .   ",
            "   .  ",
            "    . ",
            "     ]",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve(True))

    def test_start_eq_end(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            ".     ",
            "      ",
            "      ",
            "      ",
            "      ",
            "      ",
        ])
        a.init_grid(6, 6, walls, (0,0), (0,0))
        self.assertPathEquals(walls, expected_path, a.solve())

    def test_maze_no_solution(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "(#    ",
            " # ###",
            " # #  ",
            " ##   ",
            "    ##",
            "##  #)",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve())

    def test_maze_closest_solution(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[#    ",
            ".# ###",
            ".# #  ",
            ".##   ",
            "... ##",
            "## .#)",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve(True, True))

    def test_maze_closest_solution2(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[#    ",
            ".# ###",
            " # #  ",
            " #)# #",
            " # ## ",
            "##### ",
        ])
        a.init_grid(6, 6, walls, start, end)
        self.assertPathEquals(walls, expected_path, a.solve(True, True))

    def test_maze_closest_solution3(self):
        a = pf.AStar()
        walls, expected_path, start, end = self.from_sketch([
            "[#    ",
            ".# ###",
            ".# #  ",
            ".##   ",
            "....##",
            "## ###",
        ])
        a.init_grid(6, 6, walls, start, (5, 5))
        self.assertPathEquals(walls, expected_path, a.solve(True, True))

if __name__ == '__main__':
    unittest.main()