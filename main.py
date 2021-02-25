from pydraw import *
import time
import random
screen = Screen(800,600,"Sorty-sort") # creating screen for use
screen.color(Color("black"))


class ___column(): # just for grouping shapes to their respective lengths
    def __init__(self,i,length_list):
        # This will make a rectangle shape centered in the screen, each proportionally sized to have regular shape sizes
        self.rect = Rectangle(screen,100+600/len(length_list)*i,500-400/len(length_list)*(length_list[i]),600/len(length_list),400/len(length_list)*length_list[i],Color("red"),Color("black"))
        self.length = length_list[i]

def list_of_random(number): # creates random numbers from 1 to the number, in order to make lengths for different sized
                            # rectangles n stuff
    temp = []
    for i in range(1,number+1):
        temp.append(i)
    # this initializes a list with all those numbers


    temp_2 = []
    while len(temp)>0:
        length = random.choice(temp)
        temp_2.append(length)
        temp.remove(length) # we can use .remove() reliably because they are all unique values
    # this randomizes those numbers


    return temp_2


def create_columns(length_list): # creates an array containing all of the shapes as a part of the __column class
    return_list = []
    for i in range(len(length_list)):
        rectangle = ___column(i,length_list)
        return_list.append(rectangle)
        screen.update()
    return return_list



def bruting(amount_of_things):
    random_len_list = list_of_random(amount_of_things)
    objects_to_brutalize = create_columns(random_len_list)
    del random_len_list # i think this helps with memory consumption? maybe?

    sorting = True
    while sorting:
        sorting = False
        for i in range(len(objects_to_brutalize)-1):
            if objects_to_brutalize[i].length > objects_to_brutalize[i+1].length: # is this one longer than the next
                sorting = True
                # Here, we let the while loop know we probably need to keep sorting,
                # so we keep going after this for loop finishes


                x_2 = objects_to_brutalize[i+1].rect.x()
                # this establishes the initial x position of the next rectangle

                # THEORY: because both rectangles will move at the same rate, and the same distance, you only need to
                #         calculate using one of the initial positions, and it will coordinate equally in the opposite
                #         direction

                while objects_to_brutalize[i].rect.x() < x_2:
                    objects_to_brutalize[i].rect.move(1,0)     # We move by one pixel for each in order to create
                    objects_to_brutalize[i+1].rect.move(-1,0)  # a smooth visual representation of switching places
                    time.sleep(1/240) # just for consistency
                    screen.update()

                objects_to_brutalize.insert(i,objects_to_brutalize[i+1])
                objects_to_brutalize.pop(i+2)
                # This reorders the array, in the same way the visuals were just changed, so the visuals actually are
                # representative of the data




# bruting(int(input("YOOOO. How many bro?\n")))
bruting(20)


screen.stop()