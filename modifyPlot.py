import pygame

# append x to list; needs to be updated to see where x is being imported from
# limit items to 5 by removing earliest entry

def modifyPlot(growth_data): # parameter expects a list
                             # is there supposed to be a second parameter to obtain the growth data? (x variable)

    while len(growth_data) < 6:
        if len(growth_data) == 5: # if the list is 5 items max, pop first item in list and add newest item
            growth_data.pop(0)
            growth_data.append(x)
            return growth_data
        else:
            growth_data.append(x) # x represents the growth data
