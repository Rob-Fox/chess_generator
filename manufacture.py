import random
import sys
import math
import datetime
import numpy as np
from PIL import Image

# class ChessPiece:
#     def __init__(self, color, piece, *args, **kwargs):
#         self.color = color
#         self.piece = piece

# white_rook = ChessPiece(
#     color='white', piece='rook')

# print(white_rook.color, white_rook.piece)

piece_arr = ['R', 'P', 'N', 'K', 'Q', 'B', 'E']
piece_weight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0]

def weighted_random(piece_weight):
    #multiply the difference between 1 and the piece_weight selected by random, if it exceeds a certain number re-roll
    #each time a piece is selected it should be decreased by .2 and all other pieces should be increased by .1
    pick = random.randint(0,6)
    if piece_weight[pick] < 1:
        change = 1-piece_weight[pick]
        if random.random() / change > 1:
            return weighted_random(piece_weight)
        else:
            piece_weight[pick] = piece_weight[pick] - .2
            for num in range(0, pick):
                piece_weight[num] += .1
            for num in range(pick+1, len(piece_weight)):
                piece_weight[num] += .1
            return pick
    else:
        piece_weight[pick] = piece_weight[pick] -.2
        return pick

# pick 100000 weighted random integers, put them in an array
# i = 0
# final_arr = []
# for i in range(100000):
#     picked = weighted_random(piece_weight)
#     final_arr.append(picked)
# count_arr = [final_arr.count(0), final_arr.count(1), final_arr.count(2), final_arr.count(3), final_arr.count(4), final_arr.count(5), final_arr.count(6)]

# print('highest: ', count_arr[np.argmax(count_arr)])
# print('lowest: ', count_arr[np.argmin(count_arr)])

def pick_color():
    picks = []
    for num in range(0,5):
        picks.append(random.random())
    pick = 0.0
    for num in range(0,5):
        pick += picks[num]
    pick = pick / 5
    if round(pick) == 1:
        return 'W'
    else:
        return 'B'

# color_picked = []
# for num in range(100000):
#     color_picked.append(pick_color())
# print(color_picked.count(0))
# print(color_picked.count(1))

def create_pieces(number):
    pieces = []
    for num in range(number):
        piece_type = piece_arr[weighted_random(piece_weight)]
        if piece_type == 'E':
            piece_color = 'E'
        else:
            piece_color = pick_color()
        piece_bg = pick_color()
        
        pieces.append((piece_color + piece_type + piece_bg + '.png'))
    return pieces

# print(create_pieces(100))


def create_set(name, quantity):
    # print(name)
    print(datetime.datetime.now())
    pic_list = create_pieces(quantity)
    root = math.sqrt(quantity)

    background_dimension = int(root * 32)
    picture = Image.new('RGB',(background_dimension, background_dimension))
    offset = [0, 0]
    for i in range(0, len(pic_list), int(root)):
        images = [Image.open(j) for j in pic_list[i:i+int(root)]]

        for item in images:
            # print(datetime.datetime.now())
            if offset[0] < background_dimension:
                picture.paste(item, (offset[0], offset[1]))
                offset[0] += 32
            else:
                offset[1] += 32
                offset[0] = 0
                picture.paste(item, (offset[0], offset[1]))
    
    picture.save(name)
    print(datetime.datetime.now())

create_set('test1.png', 100)

