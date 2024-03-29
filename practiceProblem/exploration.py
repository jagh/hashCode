###########################################################
### Hash Code 2019                                      ###
### Pizza Practice Problem                              ###
### Team: SuicideSquad                                  ###
###########################################################


import sys
import itertools
from collections import deque
from collections import OrderedDict


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
        self.max_area = max_area

        ## Exploration
        self.cells_used = []
        self.node_count = 0
        self.nodes = {}

        ## Extend Slice
        self.slices_to_file = []
        self.cell_slice_used = []

        self.num_ings = 2 ### T and M



    def groupingNodes(self):
        """
        Nodes group by each cell_end duplicated.

        Input format: [(num_node[0], (cell_beg, cell_end)), ...
        Output format: [(cell_end[0], [cell_beg[0], cell_beg[1], cell_beg[2]]), ...
        """
        group_nodes = OrderedDict()
        # group_nodes = SortedDict()

        ## Gruped node as FIFO order
        for key, val in self.nodes.iteritems():
            if val[1] in group_nodes: group_nodes[val[1]].append(val[0])
            else: group_nodes[val[1]] = [val[0]]

        ## Debbug
        # print("{}".format('-'*50))
        # print("Extend slice:")
        # print("Nodes: {}".format(self.nodes))
        # print("Cells used: {}".format(self.cells_used))
        # print("Fifo order: {}".format(group_nodes))
        return group_nodes

    def sliceComposition(self):
        """
        This method build the slides from group_nodes dict.
        Input format: [(cell_end[0], [cell_beg[0], cell_beg[1], cell_beg[2]]), ...
        """

        ## Buil Groups of Nodes
        group_nodes = self.groupingNodes()

        ## Build Slice in n-dimension
        ## From the FIFO Groups of Nodes
        for key, val in group_nodes.iteritems():
            min_row = max_row = key[0]
            min_col = max_col = key[1]

            ## Check the rule max_are
            #################################################################
            if (len(val)*self.num_ings)%2 == 0 and len(val)*self.num_ings <= self.max_area:

                ## Find the min and max row and cols
                for cell in val:
                    ## Check if the cell is used in another slice
                    try:
                        self.cell_slice_used.index(cell)
                        # print("val: {}".format(cell))
                    except ValueError:
                        if cell[0] < key[0]: min_row = cell[0]
                        if cell[0] > key[0]: max_row = cell[0]
                        if cell[1] < key[1]: min_col = cell[1]
                        if cell[1] > key[1]: max_col = cell[1]

                        ## Added to used cells by slice
                        self.cell_slice_used.append(cell)

                ############################################################
                ## Check the minimum number of ingredients per slice
                # new_slice = list(itertools.islice(self.grid[row], col, col+1+(self.min_ings*2)))c
                # print(self.grid[min_row])

                ## Added to used cells by slice
                self.cell_slice_used.append(key)

                ## Added the last slices
                self.slices_to_file.append(((min_row, min_col), (max_row, max_col)))

            else:
                row_cells = []
                col_cells = []
                for cell in val:
                    ## Check if the cell is used in another slice
                    try:
                        self.cell_slice_used.index(cell)
                    except ValueError:
                        if key[0] == cell[0]:
                            row_cells.append(cell)
                        elif key[1] == cell[1]:
                            col_cells.append(cell)

                ## Find the cells position
                ## For Columns
                if len(col_cells) >= len(row_cells):
                    cells_to_use = col_cells
                    min_col = max_col = key[1]
                    min_row = max_row = key[0]

                    ## Find the min and max rows
                    for cell in val:
                        if cell[0] < key[0]: min_row = cell[0]
                        if cell[0] > key[0]: max_row = cell[0]
                        self.cell_slice_used.append(cell)

                    ## Added to used cells by slice
                    self.cell_slice_used.append(key)

                    ## Added the last slices
                    self.slices_to_file.append(((min_row, min_col), (max_row, max_col)))

                ## Find the cells position
                ## For Rows
                else:
                    min_col = max_col = key[1]
                    min_row = max_row = key[0]

                    ## Find the min and max rows
                    for cell in val:
                        if cell[1] < key[1]: min_col = cell[1]
                        if cell[1] > key[1]: max_col = cell[1]
                        self.cell_slice_used.append(cell)

                    ## Added to used cells by slice
                    self.cell_slice_used.append(key)

                    ## Added the last slices
                    self.slices_to_file.append(((min_row, min_col), (max_row, max_col)))

                    cells_to_use = row_cells

                ## Debbug
                # print("{}".format('-'*50))
                # print("key: {}".format(key))
                # print("rows: {}".format(row_cells))
                # print("cols: {}".format(col_cells))
                # print("cells to used {}".format(cells_to_use))

        print("Num Slices: {}".format(len(self.slices_to_file)))
        print("slices_to_file: {}".format(self.slices_to_file))

        return self.slices_to_file
        ### Missing
        ### Add Checker for max number of cell by slice rule


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

        ## Right Node 1-dim
        #######################################################################$
        ## n-dim blocks
        if self.min_ings > 1:
            new_slice = list(itertools.islice(self.grid[row], col, col+1+(self.min_ings*2)))


        ## 1-dim blocks
        else:
            new_slice = list(itertools.islice(self.grid[row], col, col+1+1 ))

        # print("new_slice: {}".format(new_slice))
        right_node = self.sliceValidation(new_slice)
        ## If Slice is True save the slice cells
        if right_node:
            ## memory for used cells
            self.cells_used.append((row, col))
            self.cells_used.append((row, col+1))

            ## Add dict nodes with format: node_count = (cell_beg, cell_end)
            self.node_count += 1
            self.nodes[self.node_count] = ((row, col), (row, col+1))

            ## Debbug
            # print("right_slice: {}".format(new_slice))
            # print("cell_beg: {}, {}".format(row, col))
            # print("cell_end: {}, {}".format(row, col+1))


        ## Bottom Node 1-dim
        #######################################################################
        try:
            cell_beg = list(itertools.islice(self.grid[row], col, col+1))
            ## n-dim blocks
            if self.min_ings > 1:
                cell_end = list(itertools.islice(self.grid[row+(self.min_ings*2)], col, col+1))
            else:
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

                # Debbug
                # print("bottom_slice: {}".format(new_slice2))
                # print("cell_beg: {}, {}".format(row, col))
                # print("cell_end: {}, {}".format(row+1, col))
        except IndexError:
            ## Check if not are the last row
            pass


        ## Left Node 1-dim
        #######################################################################
        try:
            ## n-dim blocks
            if self.min_ings > 1:
                new_slice = list(itertools.islice(self.grid[row], col-(self.min_ings*2), col+1))
            else:
                new_slice = list(itertools.islice(self.grid[row], col-1, col+1))
            # new_slice2 = self.grid[row][col-1: col+1]
            left_node = self.sliceValidation(new_slice)

            ## If Slice is True save the slice cells
            if left_node:
                ## memory for used cells
                self.cells_used.append((row, col))
                self.cells_used.append((row, col-1))

                ## Node dict with format: node_count = (cell_beg, cell_end)
                self.node_count += 1
                self.nodes[self.node_count] = ((row, col), (row, col-1))

                ## Debbug
                # print("left_slice: {}".format(new_slice))
                # print("cell_beg: {}, {}".format(row, col))
                # print("cell_end: {}, {}".format(row, col-1))
        except ValueError:
            ## Check if there is not a left cell
            pass

        ## Up Node 1-dim
        #######################################################################
        try:
            if row-1 > 0:
                cell_beg = list(itertools.islice(self.grid[row], col, col+1))
                ## n-dim blocks
                if self.min_ings > 1:
                    cell_end = list(itertools.islice(self.grid[row-(self.min_ings*2)], col, col+1))
                else:
                    cell_end = list(itertools.islice(self.grid[row-1], col, col+1))

                new_slice2=(cell_beg[0], cell_end[0])
                up_node = self.sliceValidation(new_slice2)
                if up_node == True:
                    ## memory for used cells
                    self.cells_used.append((row, col))
                    self.cells_used.append((row-1, col))

                    ## Node dict with format: node_count = (cell_beg, cell_end)
                    self.node_count += 1
                    self.nodes[self.node_count] = ((row, col), (row-1, col))


                    # Debbug
                    # print("up_slice: {}".format(new_slice2))
                    # print("cell_beg: {}, {}".format(row, col))
                    # print("cell_end: {}, {}".format(row-1, col))
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

    # Debuug
    # print("grid: {}".format(grid))
    # print("max_area: {}".format(max_area))
    # print("min_ingredient: {}".format(min_ingredient))
    return first_line, grid


def output(list_output, file_name):
    len_slice = len(list_output)
    with open(file_name+'.out', 'w') as output_final:
        outline = []
        outline.append(str(len_slice))
        output_final.write("".join(outline) + "\n")
        for i in range(len_slice):
            outline = []
            len_couple = list_output[i].__len__()
            for j in range(len_couple):
                len_cels = list_output[i][j].__len__()
                for z in range(len_cels):
                    cel = list_output[i][j][z]
                    outline.append(str(cel) + " ")
            output_final.write("".join(outline) + "\n")




def main():
    file_name='a_example'   #'b_small'  #'c_medium'
    first_line, grid = read_file('dataset/'+file_name+'.in') #b_small.in')  # #b_small.in')

    gc = GridCutter(grid, first_line)
    gc.explorer()

    ### Write
    out_slices = gc.sliceComposition()
    output(out_slices, file_name)

if __name__ == "__main__":
    main()
