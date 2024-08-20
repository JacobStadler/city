from random import randint as ri
import numpy as np
from PIL import Image, ImageDraw
np.set_printoptions(threshold=100000)
#size = 4000
height = 1080
width = 1920

m = np.zeros(shape=(height,width))

#disp[0][size-1] = 5

def build():
    #start_width = ri(1,width-1)
    #start_height = ri(1,height-1)
    #       y               x
    #m[start_height-1][start_width-1] += 1
    #m[start_height-1][start_width  ] += 1
    #m[start_height  ][start_width-1] += 1
    #m[start_height  ][start_width  ] += 1
    # should be size squared (size*size)
    # ** = exponent
    #total_blocks = (height*width)**2+(height*width)**2+(height*width)**2
    total_blocks = 10000000
    # pos is [4,4]
    pos = []
    pos += [[ri(1,height-1),ri(1,width-1)]]
    pos += [[ri(1,height-1),ri(1,width-1)]]
    pos += [[ri(1,height-1),ri(1,width-1)]]
    pos += [[ri(1,height-1),ri(1,width-1)]]
    pos += [[ri(1,height-1),ri(1,width-1)]]
    
    print(pos)
    print(range(len(pos)-1))
    choice_log = []
    progress = 1
    complete = 10000000
    while total_blocks:
        #print(pos)
        for i in range(len(pos)):
            #print(f'{progress}\t\t{i}\t{pos[i]}')
            direction = ri(1,4)
            match direction:
                case 1:
                    if pos[i][0]-1 <= 0:
                        pos[i][0] = height-1
                    #print('U '+str(pos))
                    # Up
                    #  y            x                  [x,y]
                    m[pos[i][0]-1][pos[i][1]  ] += 1 # [4,3]
                    m[pos[i][0]-2][pos[i][1]  ] += 1 # [4,2]
                    m[pos[i][0]-2][pos[i][1]-1] += 1 # [3,2]
                    m[pos[i][0]-1][pos[i][1]-1] += 1 # [3,3]
                    pos[i][0] -= 1
                    #choice_log += ['U '+str(pos)]
                case 2:
                    if pos[i][1]+1 >= width-1:
                        pos[i][1] = 0
                    #print('R '+str(pos))
                    # Right
                    #  y            x                  [x,y]
                    m[pos[i][0]-1][pos[i][1]  ] += 1 # [4,3]
                    m[pos[i][0]  ][pos[i][1]  ] += 1 # [4,4]
                    m[pos[i][0]-1][pos[i][1]+1] += 1 # [5,3]
                    m[pos[i][0]  ][pos[i][1]+1] += 1 # [5,4]
                    pos[i][1] += 1
                    #choice_log += ['R '+str(pos)]
                case 3:
                    if pos[i][0]+1 >= height-1:
                        pos[i][0] = 0
                    #print('D '+str(pos))
                    # Down
                    #  y            x                  [x,y]
                    m[pos[i][0]-1][pos[i][1]  ] += 1 # [4,3]
                    m[pos[i][0]  ][pos[i][1]-1] += 1 # [3,4]
                    m[pos[i][0]+1][pos[i][1]-1] += 1 # [3,5]
                    m[pos[i][0]  ][pos[i][1]+1] += 1 # [4,5]
                    pos[i][0] += 1
                    #choice_log += ['D '+str(pos)]
                case 4:
                    if pos[i][1]-1 <= 0:
                        pos[i][1] = width-1
                    #print('L '+str(pos))
                    # Left
                    #  y            x                  [x,y]
                    m[pos[i][0]-1][pos[i][1]-1] += 1 # [3,3]
                    m[pos[i][0]  ][pos[i][1]-1] += 1 # [3,4]
                    m[pos[i][0]-1][pos[i][1]-2] += 1 # [2,3]
                    m[pos[i][0]  ][pos[i][1]-2] += 1 # [2,4]
                    pos[i][1] -= 1
                    #choice_log += ['L '+str(pos)]
            progress += 1
            total_blocks -= 1
        #print(f'{progress}/{complete}')
    #print(choice_log)
    print('done')
    return list(m)

def draw():
    pixel = 1
    img = Image.new("RGBA", (width * pixel, height * pixel), (100, 100, 100, 100))
    draw = ImageDraw.Draw(img, "RGBA")
    for i in range(width):
        for j in range(height):
            capture = int(m[j][i])
            clr = (capture,capture,capture)
            draw.rectangle((i,j,i+1,j+1),fill=clr,width=pixel)
    img.save('world.png')
    print('picture done')

if __name__ == '__main__':
    build()
    draw()

#draw()
#m = np.array2string(m,max_line_width=1000,separator='')
#print(m)
#print()
#print('done')