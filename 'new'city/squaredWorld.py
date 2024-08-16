from random import randint as ri
import numpy as np
from PIL import Image, ImageDraw
np.set_printoptions(threshold=10000)
size = 1024

m = np.zeros(shape=(size,size))

#disp[0][size-1] = 5

def build():
    start = ri(1,size-1)
    #   y        x
    m[start-1][start-1] += 1
    m[start-1][start  ] += 1
    m[start  ][start-1] += 1
    m[start  ][start  ] += 1
    # should be size squared (size*size)
    # ** = exponent
    total_blocks = size**2+size**2+size**2
    # pos is [4,4]
    pos = [start,start]
    #print(pos)
    choice_log = []
    while total_blocks:
        direction = ri(1,4)
        #print(pos)
        match direction:
            case 1:
                if pos[0]-1 < 0:
                    pos[0] = size-1
                #print('U '+str(pos))
                # Up
                #  y         x               [x,y]
                m[pos[0]-1][pos[1]  ] += 1 # [4,3]
                m[pos[0]-2][pos[1]  ] += 1 # [4,2]
                m[pos[0]-2][pos[1]-1] += 1 # [3,2]
                m[pos[0]-1][pos[1]-1] += 1 # [3,3]
                pos[0] -= 1
                choice_log += ['U '+str(pos)]
            case 2:
                if pos[1]+1 >= size-1:
                    pos[1] = 0
                #print('R '+str(pos))
                # Right
                #  y         x               [x,y]
                m[pos[0]-1][pos[1]  ] += 1 # [4,3]
                m[pos[0]  ][pos[1]  ] += 1 # [4,4]
                m[pos[0]-1][pos[1]+1] += 1 # [5,3]
                m[pos[0]  ][pos[1]+1] += 1 # [5,4]
                pos[1] += 1
                choice_log += ['R '+str(pos)]
            case 3:
                if pos[0]+1 >= size-1:
                    pos[0] = 0
                #print('D '+str(pos))
                # Down
                #  y         x               [x,y]
                m[pos[0]-1][pos[1]  ] += 1 # [4,3]
                m[pos[0]  ][pos[1]-1] += 1 # [3,4]
                m[pos[0]+1][pos[1]-1] += 1 # [3,5]
                m[pos[0]  ][pos[1]+1] += 1 # [4,5]
                pos[0] += 1
                choice_log += ['D '+str(pos)]
            case 4:
                if pos[1]-1 < 0:
                    pos[1] = size-1
                #print('L '+str(pos))
                # Left
                #  y         x               [x,y]
                m[pos[0]-1][pos[1]-1] += 1 # [3,3]
                m[pos[0]  ][pos[1]-1] += 1 # [3,4]
                m[pos[0]-1][pos[1]-2] += 1 # [2,3]
                m[pos[0]  ][pos[1]-2] += 1 # [2,4]
                pos[1] -= 1
                choice_log += ['L '+str(pos)]
        total_blocks -= 1
    #print(choice_log)
def draw():
    pixel = 1
    img = Image.new("RGBA", (size * pixel, size * pixel), (100, 100, 100, 100))
    draw = ImageDraw.Draw(img, "RGBA")
    for i in range(size):
        for j in range(size):
            capture = int(m[j][i])
            clr = (capture,capture,capture)
            draw.rectangle((i,j,i+1,j+1),fill=clr,width=pixel)
    img.save('.\world.png')
build()
draw()
#m = np.array2string(m,max_line_width=1000,separator='')
#print(m)
print()
print('done')