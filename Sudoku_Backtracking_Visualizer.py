#This program requires the user to manually enter a valig Sudoku Grid in the program code itself
#The program then only visualizes the backtracking algorithm used to solve the puzzle
#If the entered sudoku gris in the code in invalid, the program just runs indefintely, so therfore a Valid grid must be entered

#Author: Jared Dominic Fernandez

import pygame
pygame.font.init()

surface = pygame.display.set_mode((500,600))

pygame.display.set_caption("SUDOKU SOLVER VISUALIZER") 
img = pygame.image.load('icon.png') 
pygame.display.set_icon(img)


sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

x=0
y=0
size=500/9
val=0

font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20)



def highlight_cell():
    for i in range(2):
        pygame.draw.line(surface, (255, 255, 0), (y * size-3, (x + i)*size), (y * size + size + 3, (x + i)*size), 7) 
        pygame.draw.line(surface, (255, 255, 0), ( (y + i)* size, x * size ), ((y + i) * size, x * size + size), 7)    
  
def draw_grid(): 
    for i in range (9): 
        for j in range (9): 
            if sudoku[i][j]!= 0: 
  
                pygame.draw.rect(surface, (153, 153, 153), (j * size, i * size, size + 1, size + 1)) 
  
                text1 = font1.render(str(sudoku[i][j]), 1, (0, 0, 0)) 
                surface.blit(text1, (j * size + 15, i * size + 15)) 
    # Draw lines horizontally and verticallyto form grid            
    for i in range(10): 
        if i % 3 == 0 : 
            thick = 7
        else: 
            thick = 1
        pygame.draw.line(surface, (123, 123, 0), (0, i * size), (500, i * size), thick) 
        pygame.draw.line(surface, (123, 123, 0), (i * size, 0), (i * size, 500), thick)       

    
def first_empty(b):
    for i in range(len(b)):
        for j in range (len(b[0])):
            if(b[i][j]== 0):
                return (i,j)
    return None

def solve_board(sudoku):
    emp = first_empty(sudoku)
    if not emp:
        return True
    else:
        row,col = emp
    pygame.event.pump()  
    for i in range(1,10):
        if is_valid(sudoku,(row, col),i):
            sudoku[row][col] = i
            global x, y 
            x = row 
            y = col
            # white color background\ 
            surface.fill((255, 255, 255)) 
            draw_grid() 
            highlight_cell()
            pygame.display.update() 
            pygame.time.delay(40)
            if(solve_board(sudoku)):
                return True
            sudoku[row][col]=0
            surface.fill((255, 255, 255)) 
            draw_grid() 
            highlight_cell() 
            pygame.display.update() 
            pygame.time.delay(100)  
    return False

def is_valid (sudoku, position, num):
    for i in range(len(sudoku[0])):
        if(sudoku[position[0]][i]==num and position[1]!=i):
            return False
    for i in range(len(sudoku)):
        if(sudoku[i][position[1]]==num and position[0]!=i):
            return False
    x =position[1]//3
    y=position[0]//3
    for i in range(y*3,y*3 +3):
        for j in range(x*3,x*3 +3):
            if((i,j)!=position and sudoku[i][j]==num):
                return False
    return True


def instruction(): 
    text = font2.render("PRESS ENTER TO VISUALIZE", 1, (0, 0, 0)) 
    surface.blit(text, (20, 540)) 
  
def result(): 
    text1 = font1.render("FINISHED", 1, (0, 0, 0)) 
    surface.blit(text1, (20, 570))     
run = True
flag = 0
error = 0
# loop
while run: 
    surface.fill((255, 255, 255)) 
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False  
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RETURN: 
                flag = 1   
             
    if flag == 1: 
        if(solve_board(sudoku)==True):
            result()
    draw_grid()
    if(flag==0):
        instruction()
      
    # Update window 
    pygame.display.update()   
  
# Quit pygame window     
pygame.quit()      
