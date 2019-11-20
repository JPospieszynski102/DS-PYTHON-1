import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randomGrid(N):
    return np.random.choice([255, 0], N*N, p=[0.1, 0.9]).reshape(N, N)

def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider

#def update():
def neighborsSum(i, j, matrix):
    
    N = matrix.shape[0]
    
    total = int((matrix[i, (j-1)%N]+matrix[i, (j+1)%N] +
    matrix[(i-1)%N, j]+matrix[(i+1)%N, j] +
    matrix[(i-1)%N, (j-1)%N]+matrix[(i+1)%N, (j+1)%N] +
    matrix[(i+1)%N, (j-1)%N]+matrix[(i+1)%N, (j+1)%N])/255)
    
    return total
    
def update(matrix):
    
    N = matrix.shape[0]
  
    newmatrix = np.zeros(N*N).reshape(N,N)
    
    for i in range(0, N):
        for j in range(0, N):
            total = neighborsSum(i, j, matrix)
            
            if matrix[i, j] == 255:
                if (total < 2) or (total > 3):
                    newmatrix[i, j] = 0
            else:
                if total == 3:
                    newmatrix[i, j] = 255
    return newmatrix
    
N = 10
#img = np.zeros(N*N).reshape(N,N) 
img = randomGrid(N)
new_img = update(img)




        


    


