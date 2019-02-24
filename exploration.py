###########################################################
### Hash Code 2019                                      ###
### Pizza Practice Problem                              ###
### Team: SuicideSquad                                  ###
###########################################################


import sys
import itertools
from collections import deque


class GridCutter:
    """
    Cutting slices from a given grid
    """

    def __init__(self, grid, first_line):
        self.grid = grid
        self.first_line = first_line

        ## setting the input variables
        row_count, col_count, min_ings, max_area = tuple(map(int, first_line.split(' ')))
        self.row_count = row_count
        self.col_count = col_count
        self.min_ings = min_ings
        self.max_area = 4 #max_area

        ## Scoring
        self.slices = deque()


    def sliceValidation(self, new_slice):
        """
        Check if the slice can be accepted:

        1 Rule) If the slice have the min_ingredients (mushrooms and tomatoes)
        2 Rule) Total area of each slice must be at most max_area
        3 Rule) Each cell of the pizza must be in one slice
        """
        mroom_count = 0
        tomato_count = 0
        cell = 0

        while cell < len(new_slice):
            if new_slice[cell] == 'M':
                mroom_count += 1
            elif new_slice[cell] == 'T':
                tomato_count += 1
            cell += 1

        ## Check the Rule 1
        if mroom_count >= self.min_ings and tomato_count >= self.min_ings:
            self.slices.append(new_slice)
            print("Accepted Slices: {}".format(self.slices))


    def slicer(self, row, col):
        """
        Slice propositon:

        1) Build 1-dim rectangles
        2) Build n-dim rectangles
        """
        # print("cell: {},{}".format(row, col))
        # print("grid: {}".format(self.grid[row]))

        ## Build 1-dim rectangles
        new_slice = list(itertools.islice(self.grid[row],col, self.max_area))
        if len(new_slice) >= 2:
            self.sliceValidation(new_slice)


    def explorer(self):
        """
        Grid exploration cell by cell
        """
        slices_list = []
        for row in range(self.row_count):
            c_beg = 0
            c_end = 0
            while c_end < self.col_count:
                self.slicer(row, c_end)
                c_end += 1


def read_file(filename):
    """
    Read the file.
    Return the first_line and the grid.
    """
    ## load the file
    f = open(filename, 'r')
    first_line = f.readline()

    ## setting the input variables
    row_count, column_count, min_ingredient, max_area = tuple(map(int, first_line.split(' ')))

    ## Creating the pizza grid and populating it
    grid = []
    for i in range(row_count):
        grid.append(f.readline().rstrip())

    ## closing the file
    f.close()

    # print("grid: {}".format(grid))
    # print("max_area: {}".format(max_area))
    # print("min_ingredient: {}".format(min_ingredient))
    return first_line, grid


def main():
    first_line, grid = read_file('dataset/a_example.in') #b_small.in')
    gc = GridCutter(grid, first_line)
    gc.explorer()


if __name__ == "__main__":
    main()



# def exploration_OLD(first_line, grid):
    # ## setting the input variables
    # row_count, column_count, min_ingredient, max_area = tuple(map(int, first_line.split(' ')))
    # max_area = 1
    #
    # ## For each row, I reset the counters
    # results = []
    # slices_list = []
    # ingredients = []
    #
    # for r in range(row_count):
    #     beg = 0
    #     end = 0
    #
    #     mushroom_count = 0
    #     tomato_count = 0
    #
    #     ## scoring cells by slice
    #     max_area_count = 0
    #     # cell_ben = 0
    #     # cell_end = 0
    #
    #     ## While I'm not at the end of the row,
    #     ## I count if I have a tomato or a mushroom
    #     while end < column_count:
    #         #print("r: {}, c: {}".format(r, end))
    #         # print("beg: {}" )
    #
    #         ## Save the slice_begin
    #         if beg == end:
    #             cell_ben = (r, beg)
    #
    #         if grid[r][end] == 'M':
    #             mushroom_count += 1
    #             # print("grip[{},{}]={}".format(r, end, grid[r][end]))
    #         elif grid[r][end] == 'T':
    #             tomato_count += 1
    #
    #         ## Save the silce_end
    #         if end == max_area:
    #             #print("r: {}, c: {}".format(r, end))
    #             #print("end: {}".format(end))
    #             cell_end = (r, end)
    #             slices_list.append((cell_ben,cell_end))
    #             ingredients.append((tomato_count, mushroom_count))
    #             beg = end+1
    #
    #         end += 1
    #
    # print("slices: {}".format(slices_list))

# ## While I'm not at the end of the row,
# ## I count if I have a tomato or a mushroom
# while end < column_count:
#     print("r: {}, c: {}".format(r, end))
#     if grid[r][end] == 'M':
#         mushroom_count += 1
#         # print("grip[{},{}]={}".format(r, end, grid[r][end]))
#     elif grid[r][end] == 'T':
#         tomato_count += 1
#     end += 1

# # If the slice is too big, I must remove an ingredient
# def remove_ingredient():
#     if end - beg > max_area:
#         print("area is too big")
#         if grid[r][beg] == 'M':
#             mushroom_count -=1
#         elif grid[r][beg] == 'T':
#             tomato_count -= 1
#         beg += 1
