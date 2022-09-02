#EDITED 02-09-2022

# the game of life

# #mark all places where new life will be born;
# mark all organisms which will die;
# remove all marked organisms;
# fill all marked empty cells with new organisms.
# Input data will contain 5 lines of 7 characters each. They represent a 5 by 7 fragment of the game field.

def convert(initial_state= ('''-------
-------
--X-X-X
--X-X-X
--X-X-X''')): #convert input into a list, so it is easier to operate on

    game_list = initial_state.split('\n')

    return(game_list)

def mark_cell():
    #if cell has 0-1 or 3+ alive neighbours(X) - dies
    #if 2 neighbours - survives
    #if 3 neighbours - it becomes alive
    
    result = '' #life after day 1 (after one neighbour check for all cells)

    game_list = convert()
    # print(game_list)

    for r in range(len(game_list)):
        result += '''
        '''
        for c in range(len(game_list[r])):
            choosen_cell = game_list[r][c]
        
            try:
                born_count = 0

                if r == 0 and c != 0 and c!= 6:

                    neighbours = [game_list[r][c-1],game_list[r][c+1],game_list[r+1][c-1],game_list[r+1][c],game_list[r+1][c+1]]

                elif r == 4 and c != 0 and c!= 6:

                    neighbours = [game_list[r-1][c-1],game_list[r-1][c],game_list[r-1][c+1],game_list[r][c-1],game_list[r][c+1]]

                elif c == 0 and r != 0 and r != 4:

                    neighbours = [game_list[r-1][c],game_list[r-1][c+1],game_list[r][c+1],game_list[r+1][c],game_list[r+1][c+1]]
 
                elif c == 6  and r != 0 and r != 4:

                    neighbours = [game_list[r-1][c-1],game_list[r-1][c],game_list[r][c-1],game_list[r+1][c-1],game_list[r+1][c]]

                elif r == 0 and c == 0:

                    neighbours = [game_list[r][c+1],game_list[r+1][c],game_list[r+1][c+1]]

                elif r == 0 and c == 6:

                    neighbours = [game_list[r][c-1],game_list[r+1][c-1],game_list[r+1][c]]

                elif r == 4 and c == 0:

                    neighbours = [game_list[r-1][c],game_list[r-1][c+1],game_list[r][c+1]]

                elif r == 4 and c == 6:

                    neighbours = [game_list[r-1][c-1],game_list[r-1][c],game_list[r][c-1]]

                else: 
                    neighbours = [game_list[r-1][c-1],game_list[r-1][c],game_list[r-1][c+1],game_list[r][c-1],game_list[r][c+1],game_list[r+1][c-1],game_list[r+1][c],game_list[r+1][c+1]]

                for num in neighbours:
                    if  num == "X":
                        born_count +=1

            except IndexError as ex:
                print(ex)  

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
