
def my_pandas(filename):
    """
    Takes the iris.data file and creates a list of list from the contents
    PARAM: filename -> Name of iris.data file
    RETURNS: List[list[]] -> List of list of contents of iris.data
    """
    
    iris = []                            # 
    f_obj = open(filename)               # 
    # Loops through every line of f_obj
    for line in f_obj:
        temp_line = line[:-1]            # Removes '/n' from species
        temp_line = temp_line.split(" ") # 
        final_line = []                  # New list to store converted values
        # 
        for val in temp_line:
            #  
            if val == temp_line[-1]:
                final_line.append(val)
            else:
                final_line.append(float(val))
        iris.append(final_line)
    f_obj.close()
    
    iris = iris[:-1]                     # Strip last empty line from list
    
    return iris

def my_pandas_idx(list_of_list,c_idx):
    """
    Indexes a list of list and returns a list of the specified columm
    PARAMS: 
        list_of_list -> List of Lists created by cpandas
        c_idx -> The columm index of list that is to be returned
    RETURNS: list[] -> List at the column specified by c_idx
    """
    
    iris_col = []                       # New list to store column values
    # 
    for line in list_of_list:
        iris_col.append(line[c_idx])
    
    return iris_col
