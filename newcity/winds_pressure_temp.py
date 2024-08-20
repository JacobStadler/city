height = 1080
width = 1920
import numpy as np
m = np.zeros(shape=(height,width,4))
#print(m)

#            U R D L
#m[i][j] == [0,0,0,0]
def winds():
    import squaredWorld

    terrain = squaredWorld.build()
    #print(terrain)
    for i in range(len(terrain)):
        for j in range(len(terrain[i])):
            if i != 0:
                if terrain[i][j] < terrain[i-1][j]:
                    m[i][j][2] += 1
                else:
                    m[i][j][2] -= 1
            if j != 0:
                if terrain[i][j] < terrain[i][j-1]:
                    m[i][j][1] += 1
                else:
                    m[i][j][1] -= 1
            if i != height-1:
                if terrain[i][j] < terrain[i+1][j]:
                    m[i][j][0] += 1
                else:
                    m[i][j][0] -= 1
            if j != width-1:
                if terrain[i][j] < terrain[i][j+1]:
                    m[i][j][3] += 1
                else:
                    m[i][j][3] -= 1

winds()
# https://wumbo.net/
def map_winds():
    arrows = [['' for i in range(width)] for y in range(height)]
    #print(len(arrows))
    #print(len(arrows[0]))
    # UL - UU - UR 
    # LL - NN - RR
    # DL - LL - DR
    # ↖ - ↑ - ↗
    # ← -   - →
    # ↙ - ↓ - ↘
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j][0] > m[i][j][1] and m[i][j][0] >= m[i][j][2] and m[i][j][0] >= m[i][j][3]:
                arrows[i][j] = '↑'
            elif m[i][j][1] > m[i][j][0] and m[i][j][1] >= m[i][j][2] and m[i][j][1] >= m[i][j][3]:
                arrows[i][j] = '→'
            elif m[i][j][2] > m[i][j][0] and m[i][j][2] >= m[i][j][1] and m[i][j][2] >= m[i][j][3]:
                arrows[i][j] = '↓'
            elif m[i][j][3] > m[i][j][0] and m[i][j][3] >= m[i][j][1] and m[i][j][3] >= m[i][j][2]:
                arrows[i][j] = '←'
            else:
                arrows[i][j] = ' '
    #print('before')
    #for i in range(len(arrows)):
    #    print(arrows[i])
map_winds()


#print(m)