# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:18:37 2017

@author: yugon
"""

maze_file = 'maze_input.txt'
U, R, D, L = 'UP', 'RIGHT', 'DOWN', 'LEFT'
S, G = 's', 'g'
direction_move = {
        U: (0, -1),
        R: (1, 0),
        D: (0, 1),
        L: (-1, 0),
        }

def read_maze(maze_file):
    maze = []
    with open(maze_file) as f:
        for row in f:
            maze.append(list(row.rstrip()))
    return maze

def get_symbol(maze, symbol):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == symbol:
                return point(x, y)
    raise ValueError
    
    
class point:
    visited = set()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = []
    
    def position(self):
        return (self.x, self.y)
    
    def symbol(self):
        return maze[self.y][self.x]
        
    def move(self, direction):
        dx, dy = direction_move[direction]
        x, y = self.x + dx, self.y + dy
        next_point = point(x, y)
        if next_point.symbol() == 'w' or next_point.position() in self.visited:
            return None
        
        next_point.history = list(self.history)
        next_point.history.append(self.position())
        self.visited.add(next_point.position())
        if next_point.is_goal():
            next_point.history.append(next_point.position())
        return next_point
    
    def is_goal(self):
        if self.symbol() == G:
            return True
        return False


def explore(candidate):
    result = []
    while candidate:
        current = list(candidate)
        candidate = []
        for p in current:
            for d in direction_move.keys():
                next_p = p.move(d)
                if next_p is not None:
                    if next_p.is_goal():
                        result.append(next_p)
                    else:
                        candidate.append(next_p)
    return result

def print_route(result):
    if not result:
        print('cannot find route...')
    else:
        print(f'start: {start.position()}')
        print(f'goal: {goal.position()}')
        print(f'route_count: {len(result)}')
        for i, p in enumerate(result):
            print(f'---route [{i}]--- ')
            for step, h in enumerate(p.history):
                print(f' [{step}]: {h}')


maze = read_maze(maze_file)
start, goal = get_symbol(maze, S), get_symbol(maze, G)

def main():    
    result = explore([start])
    print_route(result)

if __name__ == '__main__':
    main()
    