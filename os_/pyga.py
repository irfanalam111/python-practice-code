import pygame

a=dir(pygame)
for i in a:
    with open("pygame.txt",'w') as file:
        file.write(str(i))