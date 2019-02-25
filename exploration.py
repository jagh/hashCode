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
        self.cells_used = []
        self.node_count = 0
        self.nodes = {}


    def extendSlice(self):
        """
        From nodes pick one node an extend their slice.

        node format: num_node = (cell_beg, cell_end)
        grid format: ['TTTTT', 'TMMMT', 'TTTTT']]
        cells_used: List((row, col), ...)
        """

        print("{}".format('-'*50))
        print("Extend slice:")
        print("Nodes: {}".format(self.nodes))
        print("Cells used: {}".format(self.cells_used))

        ## Here we can create the code to expand slices
        ##



    def sliceValidation(self, new_slice):
        """
        Check if the slice can be accepted:

        1 Rule) Each cell of the pizza must be in one slice
        2 Rule) If the slice have the min_ingredients (mushrooms and tomatoes)
        3 Rule) Total area of each slice must be at most max_area
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

        ## Check the Rule 2
        if mroom_count >= self.min_ings and tomato_count >= self.min_ings:
            return True
            # self.slices.append(new_slice)
            # print("Accepted Slices: {}".format(self.slices))

        return False


    def slicer(self, row, col):
        """
        Slice proposition:
        1) Build nodes

        1) Build 1-dim rectangles
        2) Build n-dim rectangles
        """

        ## Right Node
        new_slice = list(itertools.islice(self.grid[row], col, col+2))
        right_node = self.sliceValidation(new_slice)
        ## If Slice is True save the slice cells
        if right_node:
            ## memory for used cells
            self.cells_used.append((row, col))
            self.cells_used.append((row, col+1))

            ## Node dict with format: node_count = (cell_beg, cell_end)
            self.node_count += 1
            self.nodes[self.node_count] = ((row, col), (row, col+1))

            ## Debbug
            print("right_slice: {}".format(new_slice))
            # print("cell_beg: {}, {}".format(row, col))
            # print("cell_end: {}, {}".format(row, col+1))


        ## Bottom Node
        try:
            cell_beg = list(itertools.islice(self.grid[row], col, col+1))
            cell_end = list(itertools.islice(self.grid[row+1], col, col+1))
            new_slice2=(cell_beg[0], cell_end[0])
            bottom_node = self.sliceValidation(new_slice2)
            if bottom_node == True:
                ## memory for used cells
                self.cells_used.append((row, col))
                self.cells_used.append((row+1, col))

                ## Node dict with format: node_count = (cell_beg, cell_end)
                self.node_count += 1
                self.nodes[self.node_count] = ((row, col), (row+1, col))

                print("bottom_slice: {}".format(new_slice2))
                # print("cell_beg: {}, {}".format(row, col))
                # print("cell_end: {}, {}".format(row+1, col))
        except IndexError:
            ## Check if not are the last row
            pass

        ## end slicer


    def explorer(self):
        """
        Grid exploration cell by cell
        """
        slices_list = []
        for row in range(self.row_count):
            c_beg = 0
            c_end = 0
            while c_end < self.col_count:
                try:
                    self.cells_used.index((row, c_end))
                except ValueError:
                    ## The cell is not used
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

    print("grid: {}".format(grid))
    # print("max_area: {}".format(max_area))
    # print("min_ingredient: {}".format(min_ingredient))
    return first_line, grid


def main():
    first_line, grid = read_file('dataset/a_example.in') # b_small.in') #b_small.in')
    gc = GridCutter(grid, first_line)
    gc.explorer()
    gc.extendSlice()


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
