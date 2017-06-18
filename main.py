# -*- coding: utf-8 -*-
import pygame
import sys
import math
import copy

width = 800
height = 800
size = 10
pygame.init()
window = pygame.display.set_mode([width, height])
filled = []
clock = pygame.time.Clock()
playing = False
currentState = [[] for _ in range(int(height / size))]


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # check to see if user hits the x
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = math.floor(pos[0] / size)
            y = math.floor(pos[1] / size)
            if not playing:
                if [x, y] not in filled:
                    filled.append([x, y])
                else:
                    filled.remove([x, y])

            if x == 0 and y == 0:

                if playing:
                    playing = False
                    filled.remove([x, y])
                    currentState = [[] for _ in range(int(height / size))]
                else:
                    playing = True

                    for r in range(int(width / size)):
                        for c in range(int(height / size)):
                            if [r, c] in filled:
                                currentState[r].append(1)
                            else:
                                currentState[r].append(0)

                    # print (currentState)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = 1
            y = 1

    window.fill([255, 255, 255])
    #for x in range(0, width, size):
        #pygame.draw.line(window, (0, 0, 0), (x, 0), (x, height))
    #for x in range(0, height, size):
        #pygame.draw.line(window, (0, 0, 0), (0, x), (width, x))
    if not playing:
        for x in filled:
            pygame.draw.rect(window, (255, 0, 0), (x[0] * size, x[1] * size,
                            size, size), 0)
    for x in range(len(currentState)):
        for y in range(len(currentState[x])):
            if currentState[x][y] == 1:
                pygame.draw.rect(window, (0, 0, 255), (x * size, y * size, size,
                            size), 0)
    pygame.display.update()
    # game of life happens here
    nextState = [[] for _ in range(int(width / size))]
    '''Any live cell with fewer than two live neighbours dies, as if caused by
    underpopulation.
    # Any live cell with two or three live neighbours lives on to the next
    generation.
    # Any live cell with more than three live neighbours dies, as if by
    overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell,
    as if by reproduction.'''
    if playing:
        nextState = copy.deepcopy(currentState)
        # print (nextState)
        for x in range(1, int(width / size) - 1):
            for y in range(1, int(height / size) - 1):
                neighbours = 0

                if currentState[x - 1][y - 1] == 1:
                    neighbours += 1
                if currentState[x - 1][y] == 1:
                    neighbours += 1
                if currentState[x - 1][y + 1] == 1:
                    neighbours += 1
                if currentState[x + 1][y - 1] == 1:
                    neighbours += 1
                if currentState[x + 1][y] == 1:
                    neighbours += 1
                if currentState[x + 1][y + 1] == 1:
                    neighbours += 1
                if currentState[x][y - 1] == 1:
                    neighbours += 1
                if currentState[x][y + 1] == 1:
                    neighbours += 1
                if currentState[x][y] == 1 and neighbours < 2:
                    nextState[x][y] = 0
                if currentState[x][y] == 1 and neighbours > 3:
                    nextState[x][y] = 0
                if currentState[x][y] == 0 and neighbours == 3:
                    nextState[x][y] = 1

        currentState = copy.deepcopy(nextState)
    clock.tick(10)  # make this global lastery