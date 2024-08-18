height = 4000
width = 4000
import numpy as np
m = np.zeros(shape=(height,width,4))
print(m)

#            U R D L
#m[i][j] == [0,0,0,0]
def winds():
    import squaredWorld

    terrain = squaredWorld.build()
    for i in terrain:
        for j in terrain[i]:
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