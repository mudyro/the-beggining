# the game of life

# #mark all places where new life will be born;
# mark all organisms which will die;
# remove all marked organisms;
# fill all marked empty cells with new organisms.
# Input data will contain 5 lines of 7 characters each. They represent a 5 by 7 fragment of the game field.

def convert(initial_state= ('''-------
-------
--XXX--
-------
-------''')): #convert input into a list, so it is easier to operate on

    game_list = []
    row_start = 0 #just to iterate through input
    row_end = 7

    for _ in range(5):
        row_cells = ''

        for i in range(row_start,row_end):
            row_cells += initial_state[i]
        game_list.append(row_cells)
        row_start += 8
        row_end += 8

    return(game_list)

def mark_cell():
    #if cell has 0-1 or 3+ alive neighbours(X) - dies
    #if 2 neighbours - survives
    #if 3 neighbours - it becomes alive
    
    result = '' #life after day 1 (after one neighbour check for all cells)

    game_list = convert()

    for r in range(len(game_list)):
        result += '''
        '''
        for c in range(len(game_list[r])):
            choosen_cell = game_list[r][c]
        
            try:

                neighbours = [game_list[r-1][c-1],game_list[r-1][c],game_list[r-1][c+1],game_list[r][c-1],game_list[r][c+1],game_list[r+1][c-1],game_list[r+1][c],game_list[r+1][c+1]]
                born_count = 0

                if r == 0:
                    neighbours = neighbours[3:]
                elif r == 4:
                    neighbours = neighbours[:5]

                elif c == 0 and r != 0 and r != 4:

                    del neighbours[5]
                    del neighbours[3]
                    del neighbours[0]
                    
                elif c == 6  and r != 0 and r != 4:

                    del neighbours[6]
                    del neighbours[4]
                    del neighbours[2]

                elif r == 0 and c == 0:

                    del neighbours[2]
                    del neighbours[0]

                elif r == 0 and c == 6:

                    del neighbours[4]
                    del neighbours[1]

                elif r == 4 and c == 0:

                    del neighbours[3]
                    del neighbours[0]

                elif r == 4 and c == 6:

                    del neighbours[4]
                    del neighbours[2]

                for num in neighbours:
                    if  num == "X":
                        born_count +=1

            except IndexError:
                pass  

            finally:
                pass

            if born_count < 2 or born_count > 3:
                result += "-"
            elif born_count == 3:
                result += "X"
            else:
                result += choosen_cell
    print (result)
    return result        

mark_cell()