import time

import cv2 as cv
import numpy as np

import gridworld


class Visualiser:
    def __init__(self):
        # defining the colors of the world object
        self.colors = {'blue': (255, 255, 1), 'green': (0, 255, 1), 'light_blue': (
            243, 225, 207), 'grey': (153, 153, 153), 'white': (255, 255, 255), 'black': (0, 0, 0)}
        self.template = gridworld.GridWorld()

    def fill(self, grid, y, x, color):
        grid[y*100:y*100+100, x*100:x*100+100] = color

    def fillrow(seld, grid, y, color):
        grid[y*100:y*100+100, :] = color

    def draw(self):
        grid = np.full((self.template.WORLD_HEIGHT*100,
                       self.template.WORLD_WIDTH*100, 3), 255, dtype=np.uint8)

        for obstacle in self.template.obstacles:
            self.fill(grid, obstacle[0], obstacle[1], self.colors['grey'])

        for i, s in enumerate(self.template.WIND):
            if (s != 0):
                self.fillrow(grid, i, self.colors['light_blue'])

        for i, s in enumerate(self.template.WIND):
            if (s == 1):
                cv.arrowedLine(
                    grid, (self.template.WORLD_WIDTH*100-30, i*100+50), (self.template.WORLD_WIDTH*100-70, i*100+50), self.colors['black'], 2)
            if (s == 2):
                cv.arrowedLine(grid, (self.template.WORLD_WIDTH*100-30, i*100+50),
                               (self.template.WORLD_WIDTH*100-70, i*100+50), self.colors['black'], 2)
                cv.arrowedLine(grid, (self.template.WORLD_WIDTH*100-130, i*100+50),
                               (self.template.WORLD_WIDTH*100-170, i*100+50), self.colors['black'], 2)

        self.fill(
            grid, self.template.START[0], self.template.START[1], self.colors['blue'])
        self.fill(
            grid, self.template.GOAL[0], self.template.GOAL[1], self.colors['green'])

        for i in range(0, self.template.WORLD_WIDTH*100, 100):
            cv.line(grid, (i, 0), (i, self.template.WORLD_HEIGHT*100),
                    self.colors['black'])
        for j in range(0, self.template.WORLD_HEIGHT*100, 100):
            cv.line(grid, (0, j), (self.template.WORLD_WIDTH*100, j),
                    self.colors['black'])

        return grid

    def show(self, grid, path):
        for i in range(len(path)):
            if path[i] != self.template.START:
                self.fill(grid, path[i][0], path[i][1], self.colors['black'])
                cv.putText(grid, str(
                    i), (path[i][1]*100+20, path[i][0]*100+20), cv.FONT_HERSHEY_PLAIN, 1.5, self.colors['white'], 1)
                cv.imshow('GRID', grid)
                cv.waitKey(0)
