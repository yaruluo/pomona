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
    output = dict()
     
    with open( fname, 'r') as file: # opens the fname file in reading mode
        reader = csv.reader( file) # reads the file, returning an iterable reader object
        for row in reader:
            year = row[ 2]
            name = row[ 3]
            count = row[ 4]
            year, count = int( year), int( count) # correctly creates integer entries

            # processes data and inserts into dict:
            if year not in output:
                output[ year] = dict()
            if name in output[ year]:
                output[ year][ name] += count
            else:
                output[ year][ name] = count
                
    return output


def extract_data( name_dict, match_string):
    """
    Takes a name dictionary  { year : {name : count}} and a string to match (strings like abc* are special case)
    and creates a result dictionary { year : count }
    :param name_dict: name dictionary
    :param match_string: string to match
    """
    output = dict()

    if match_string[ -1] == '*': # if the match_string param ends with *
        match_string = match_string[ :(len( match_string)-1)] # then remove the * to search for this

    for year in name_dict: # searches dictionary for match_string
        count = 0 
        for name in name_dict[ year]:
            if match_string == name[ :len( match_string)]:
                # checks if match_string corresponds to the beginning characters of the current name
                count += name_dict[ year][ name]
        output[ year] = count # sets dictionary to the count for that year

    return output
     

def normalize_data( data):
    """
    Normalize data by dividing by average value computed
    over years.  Be careful of /0 bugs !
    :param data: a dictionary with the data
    """
    total_count = 0
    total_years = 0
    for year in data:
        total_count += data[ year]
        total_years += 1 
    if total_years > 0:
        avg_count = total_count / total_years # computes the avg
        # normalizes the data:
        for year in data:
            if avg_count > 0:
                data[ year] /= avg_count


def scatter_plot( data, format, name):
    """
    Create a scatterplot (but don't draw the final plot).  The plotted data will need to be normalized
    :param data:  a dictionary of the form { year : count }
    :param format: format string for matplotlib
    :param name: name of this plot for legend
    """
    normalize_data( data) # normalizes data
    x_axis = []
    y_axis = []
    for year in data:
        x_axis.append( year)
    for count in data.values():
        y_axis.append( count)
    # plots data
    plt.plot(   x_axis
                , y_axis
                , format
                , label = name)
    
    

def close_plot( title):
    """
    This function should add the legend, title, and labels to the graph
    :param title: title for whole plot (a string))
    """
    plt.title( title)
    plt.xlabel( 'year')
    plt.ylabel( 'count')
    plt.legend()
    

def main( filedir):
    """
    Interactive input to specify plot
    Creates plots for the requested pattern for each of the 
    requested states
    :param filedir: the path to directory with data files
    """
    name_to_match = input( 'Enter a pattern to match: ') # asks user for name to plot
    list_of_states = [] # this is a dict of the states to plot, which will be appended to w/user inputs
                      # and used to parse when plotting
    state_to_match = 'CA' # (the default state to match is california)

    inputs = 0 # number of user inputs (three max)
    while inputs < 3 and state_to_match != '':
        # asks user for states to plot
        state_to_match = input( 'Enter the two letter abbreviation for a state (TX,IN,...): ')
        list_of_states.append( state_to_match)
        inputs += 1
    print( 'Plotting') # prints in terminal

    # format is the type of plot markers
    format = [ 'bx'    # blue X's
               , 'g+'  # green +'s
               , 'r*'] # red stars
    format_type = 0 # format_type is used to change the marker for each state when plotting
    
    for state in list_of_states: # parses the data and plots it
        if state != '':
            data = parse_names( filedir + '/' + state + '.TXT')
            data = extract_data( data, name_to_match)
            scatter_plot( data, format[ format_type], state)
            format_type += 1
    close_plot( name_to_match) # adds legend, title, and labels to the graph
    

if __name__ == '__main__':   
    # change the directory path as needed
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('namesbystate')
    # plt.show is here so that we can
    # automate testing do not call it in your code
    plt.show()
