import math

map_data = [
    # 0    1    2    3    4
    [0x1, 0x0, 0x0, 0x0, 0x0], # 0
    [0x0, 0x0, 0xb, 0x0, 0x0], # 1
    [0x0, 0x0, 0xb, 0x0, 0x0], # 2
    [0x0, 0x0, 0x0, 0x0, 0x2], # 3
    [0x0, 0x0, 0x0, 0x0, 0x0]  # 4
]

class Node:
    def __init__(self, pos):
        self.pos = pos
        self.data = data
        self.H = 0
        self.G = 0
        self.F = 0

    def calc_distance(self, pos1, pos2):
        # euclidean distance
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

    def set_h(self, target):
        self.H = self.calc_distance(target, self.pos)
    
    def set_g(self, current)
        self.G = self.calc_distance(current, self.pos)
    
    def set_f(self):
        self.F = self.H + self.G
    
    def get_h(self):
        return self.H
    
    def get_g(self):
        return self.G
    
    def get_f(self):
        return self.F
    

dirs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

start = (0,0)
end = (3,4)

def sum_coords(a,b):
    return (a[0]+b[0], a[1]+b[1])

def find_neighbours(this_node):
    neighbours = []
    for dir_ in dirs:
        # n_pos = this_node(x,y) + dir(x,y)
        n_pos = sum_coords(this_node, dir_)
        print(n_pos)
        
        is_well = [ n_pos[0] >= 0, 
                    n_pos[1] >= 0, 
                    n_pos[0] <= len(map_data)-1,
                    n_pos[1] <= len(map_data[0])-1, ]
                    
        if all(is_well):        
            if map_data[n_pos[0]][n_pos[1]] != 0xb: 
                neighbours.append(hex(map_data[n_pos[0]][n_pos[1]]))
    return neighbours

def main():
    print(find_neighbours(start))

visited_nodes = []

def find_path():
    pass
main()