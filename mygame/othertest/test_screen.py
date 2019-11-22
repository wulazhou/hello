
import sys
import pygame

def paint_screen():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.K_q)
                # if event.type == pygame.K_q
                #     print("pygame.k_q"+str(event.key))
                # print(pygame.key.name())
        pygame.display.flip()


paint_screen()
