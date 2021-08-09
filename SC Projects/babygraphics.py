"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # create interval between every 2 lines
    line_interval = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    n = YEARS.index(year_index)
    x_coordinate = GRAPH_MARGIN_SIZE + n * line_interval
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # create horizontal lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # create vertical lines
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, YEARS[i])
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        # len of year minus 1 since 2 points/years considered at the same time
        for j in range(len(YEARS)-1):
            name = lookup_names[i]
            # repeat the color list if all used
            color = COLORS[lookup_names.index(name) % len(COLORS)]
            year = YEARS[j]
            year_1 = YEARS[j+1]
            # check if the year exists in dict, if no the rank will be shown as *
            rank = name_data[name].get(year, "*")
            rank_1 = name_data[name].get(year_1, "*")
            # create x-coordinates
            x = get_x_coordinate(CANVAS_WIDTH, year) + TEXT_DX
            x_1 = get_x_coordinate(CANVAS_WIDTH, year_1) + TEXT_DX
            # if the rank exists, y-coordinate will be set according to the ranking;
            # if no y-coordinate will be at the bottom
            if rank is "*":
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(rank) + GRAPH_MARGIN_SIZE
            if rank_1 is "*":
                y_1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                y_1 = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(rank_1) + GRAPH_MARGIN_SIZE
            print(rank, (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) // 1000, y)
            canvas.create_line(x, y, x_1, y_1, width=LINE_WIDTH, fill=color)
            canvas.create_text(x, y, text=f'{name}, {rank}', fill=color, anchor=tkinter.SW)
            canvas.create_text(x_1, y_1, text=f'{name}, {rank_1}', fill=color, anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
