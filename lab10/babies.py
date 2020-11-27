"""
    CS051P Lab Assignments: Babies

    Author: Yaru Luo

    Date: 27 November 2020

    The goal of this assignment is to give you more practice with functions,
    including testing functions.
"""
import matplotlib.pyplot as plt
import sys
import csv

def parse_names( fname):
    """
    parse a name file
    :param fname:  name (full path) of the file to read and parse
    :return d: a name dictionary
    """
    #open the fname file in reading mode:
    with open( fname, 'r') as file:
        # reads the file, returning an iterable reader object:
        reader = csv.reader( file)  
        for row in reader:
            # print( row)
            year = row[ 2]

def extract_data(name_dict,match_string):
    """
    Takes a name dictionary  { year : {name : count}} and a string to match (strings like abc* are special case)
    and creates a result dictionary { year : count }
    :param name_dict: name dictionary
    :param match_string: string to match
    """
    pass

def normalize_data(data):
    """
    Normalize data by dividing by average value computed
    over years.  Be careful of /0 bugs !
    :param data: a dictionary with the data
    """
    pass

def scatter_plot(data,format,name):
    """
    Create a scatterplot (but don't draw the final plot).  The plotted data will need to be normalized
    :param data:  a dictionary of the form { year : count }
    :param format: format string for matplotlib
    :param name: name of this plot for legend
    """
    pass

def close_plot(title):
    """
    This function should add the legend, title, and labels to the graph
    :param title: title for whole plot (a string))
    """
    pass

def main(filedir):
    """
    Interactive input to specify plot
    Creates plots for the requested pattern for each of the 
    requested states
    :param filedir: the path to directory with data files
    """
    pass

if __name__ == '__main__':   
    # change the directory path as needed
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('namesbystate')
    # plt.show is here so that we can
    # automate testing do not call it in your code
    plt.show()
