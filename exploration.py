###########################################################
### Hash Code: Pizza a_example.in                       ###
### Team: SuicideSquad                                  ###
###########################################################

import sys

def get_pizza(name):
    ## load the file
    f = open(name, 'r')
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
    print("max_area: {}".format(max_area))
    print("min_ingredient: {}".format(min_ingredient))

    return first_line, grid


def right_exploration(first_line, grid):
    ## setting the input variables
    row_count, column_count, min_ingredient, max_area = tuple(map(int, first_line.split(' ')))
    # max_area = 2

    ## For each row, I reset the counters
    results = []
    slices_list = []
    ingredients = []
    for r in range(row_count):
        beg = 0
        end = 0
        mushroom_count = 0
        tomato_count = 0

        ## scoring cells by slice
        max_area_count = 0
        # cell_ben = 0
        # cell_end = 0

        ## While I'm not at the end of the row,
        ## I count if I have a tomato or a mushroom
        while end < column_count:
            #print("r: {}, c: {}".format(r, end))
            ## Save the slice_begin
            if end == 0:
                cell_ben = (r, end)

            if grid[r][end] == 'M':
                mushroom_count += 1
                # print("grip[{},{}]={}".format(r, end, grid[r][end]))
            elif grid[r][end] == 'T':
                tomato_count += 1

            ## Check if column is end
            if end == max_area:
                #print("r: {}, c: {}".format(r, end))
                #print("end: {}".format(end))
                cell_end = (r, end)
                slices_list.append((cell_ben,cell_end))
                ingredients.append((tomato_count, mushroom_count))

            end += 1

    print("slices: {}".format(slices_list))




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

def main():
    first_line, grid = get_pizza('a_example.in')
    right_exploration(first_line, grid)


if __name__ == "__main__":
    main()
