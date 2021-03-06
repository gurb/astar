import math

map_data = [
    # 0    1    2    3    4
    [0x1, 0x0, 0xb, 0x0, 0x2], # 0
    [0x0, 0x0, 0xb, 0x0, 0x0], # 1
    [0x0, 0x0, 0xb, 0x0, 0x0], # 2
    [0x0, 0x0, 0x0, 0x0, 0x0], # 3
    [0x0, 0x0, 0x0, 0x0, 0x0]  # 4
]

dirs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

start = (0,0)
end = (0,4)

class Node:
    def __init__(self, pos, parentNode=None):
        self.parent = parentNode
        self.pos = pos

        self.H = 0
        self.G = 0
        self.F = 0

    def __repr__(self):
        return "node: " + str(self.pos)

    def __eq__(self, other):
        if other == None: return False
        return self.pos == other.pos

    def set_h(self, cost):
        self.H = cost
    
    def set_g(self, cost):
        self.G = cost
    
    def set_f(self):
        self.F = self.H + self.G
    
    def get_h(self):
        return self.H
    
    def get_g(self):
        return self.G
    
    def get_f(self):
        return self.F

def in_list(this_node, list):
    for node in list:
        if this_node == node:
            return True 

def find_lowest_node(list):
    min_cost_f = list[0].get_f()
    for node in list:
        if node.get_f() < min_cost_f:
            min_cost_f = node.get_f()
    return min_cost_f

def remove_node(this_node, list):
    for node in list:
        if node == this_node:
            list.remove(node)
    return list

def find_path(start_pos, target_pos):
    startNode = Node(start_pos)
    targetNode = Node(target_pos)
    
    not_visited = []
    visited = []

    not_visited.append(startNode)

    while len(not_visited) > 0:
        
        currentNode = not_visited[0]
        for i, n in enumerate(not_visited):
            if n.get_f() < currentNode.get_f() or n.get_f() == currentNode.get_f() and n.get_h() < currentNode.get_h():
                currentNode = n
        
        not_visited.remove(currentNode)
        visited.append(currentNode)
        
        if currentNode == targetNode:
            return get_path(startNode, currentNode)
            
        neighbours_of_current_node = find_neighbours(currentNode, targetNode)
        
        for neighbour in neighbours_of_current_node:
            if in_list(neighbour, visited):
                continue
                
            new_cost_of_neighbour = currentNode.get_g() + get_distance(currentNode, neighbour)
            if new_cost_of_neighbour < neighbour.get_g() or not in_list(neighbour, not_visited):
                neighbour.set_g(new_cost_of_neighbour)
                neighbour.set_h(get_distance(neighbour, targetNode))
                neighbour.set_f()
                neighbour.parent = currentNode

                if not in_list(neighbour, not_visited):
                    not_visited.append(neighbour)

def get_path(startNode, targetNode):
    path_list = []
    currentNode = targetNode

    while currentNode != startNode.parent:
        path_list.append(currentNode)
        currentNode = currentNode.parent

    path_list.reverse()

    return path_list

def get_distance(node1, node2):
    # manhattan
    return abs(node1.pos[0]-node2.pos[0]) + abs(node1.pos[1]-node2.pos[1])

    # return math.sqrt((node1.pos[0]-node2.pos[0])**2 + (node1.pos[1]-node2.pos[1])**2)
                    
def sum_coords(a,b):
    return (a.pos[0]+b[0], a.pos[1]+b[1])

def find_neighbours(this_node, target_node):
    neighbours = []
    for dir_ in dirs:
        # n_pos = this_node(x,y) + dir(x,y)
        n_pos = sum_coords(this_node, dir_)

        
        is_well = [ n_pos[0] >= 0, 
                    n_pos[1] >= 0, 
                    n_pos[0] <= len(map_data)-1,
                    n_pos[1] <= len(map_data[0])-1, ]
                    
        if all(is_well):        
            if map_data[n_pos[0]][n_pos[1]] != 0xb:
                n = Node(n_pos)
                n.set_g(get_distance(n, this_node))
                n.set_h(get_distance(n, target_node))
                n.set_f()
                n.parent = this_node
                neighbours.append(n)
    return neighbours

def main():
    print("path :: " + str(find_path(start, end)))

if __name__ == "__main__":
    main()