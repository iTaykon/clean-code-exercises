# The `RasterGrid` represents a structured, rectangular grid in 2d space.
# Each cell of the grid is identified by its column/row index pair:
#
#  ________ ________ ________
# |        |        |        |
# | (0, 1) | (1, 1) | (2, 2) |
# |________|________|________|
# |        |        |        |
# | (0, 0) | (1, 0) | (2, 0) |
# |________|________|________|
#
#
# One can construct a `RasterGrid` by specifying the lower left and upper right
# corners of a domain and the number of cells one wants to use in x- and y-directions.
# Then, `RasterGrid` allows to iterate over all cells and retrieve the center point
# of that cell.
#
# This class can be significantly cleaned up, though. Give it a try, and if you need
# help you may look into the file `raster_grid_hints.py`.
# Make sure to make small changes, verifying that the test still passes, and put
# each small change into a separate commit.
from typing import Tuple
from math import isclose
from dataclasses import dataclass


class RasterGrid:
    def __init__(self,
                 lower_left_corner,
                 upper_right_corner,
                 number_cells_x: int,
                 number_cells_y: int) -> None:
        self._lower_left_corner = lower_left_corner
        self._upper_right_corner = upper_right_corner
        self._number_cells_x = number_cells_x
        self._number_cells_y = number_cells_y
        self.number_cells = number_cells_x*number_cells_y
        self.cells = [
            Cell(self, i, j) for i in range(number_cells_x) for j in range(number_cells_y)
        ]

    def get_lower_left_coordinates(self) -> Tuple[float, float]:
        return self._lower_left_corner.get_coordinates()
    
    def get_upper_right_coordinates(self) -> Tuple[float, float]:
        return self._upper_right_corner.get_coordinates()

@dataclass
class Cell:
    _grid: RasterGrid
    _ix: int
    _iy: int

    def get_cell_center(self) -> Tuple[float, float]:
        lower_left_x, lower_left_y = self._grid.get_lower_left_coordinates()
        upper_right_x, upper_right_y = self._grid.get_upper_right_coordinates()
        return (
            lower_left_x + (float(self._ix) + 0.5)*(upper_right_x - lower_left_x)/self._grid._number_cells_x,
            lower_left_y + (float(self._iy) + 0.5)*(upper_right_y - lower_left_y)/self._grid._number_cells_y
        )

@dataclass
class Point:
    x: float
    y: float

    def get_coordinates(self) -> Tuple[float, float]:
        return self.x, self.y


def test_number_of_cells():
    p0 = Point(0.0, 0.0)
    p1 = Point(1.0, 1.0)
    assert RasterGrid(p0, p1, 10, 10).number_cells == 100
    assert RasterGrid(p0, p1, 10, 20).number_cells == 200
    assert RasterGrid(p0, p1, 20, 10).number_cells == 200
    assert RasterGrid(p0, p1, 20, 20).number_cells == 400


def test_cell_center():
    grid = RasterGrid(Point(0.0, 0.0), Point(2.0, 2.0), 2, 2)
    expected_centers = [
        (0.5, 0.5),
        (1.5, 0.5),
        (0.5, 1.5),
        (1.5, 1.5)
    ]

    for cell in grid.cells:
        for center in expected_centers:
            if isclose(cell.get_cell_center()[0], center[0]) and isclose(cell.get_cell_center()[1], center[1]):
                expected_centers.remove(center)

    assert len(expected_centers) == 0


if __name__ == "__main__":
    test_number_of_cells()
    test_cell_center()
    print("All tests passed")
