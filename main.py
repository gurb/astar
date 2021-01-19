map_data = [
    # 0    1    2    3    4
    [0x0, 0x0, 0x0, 0x0, 0x0], # 0
    [0x0, 0x0, 0xb, 0x0, 0x0], # 1
    [0x0, 0x0, 0xb, 0x0, 0x0], # 2
    [0x0, 0x0, 0x0, 0x0, 0x2], # 3
    [0x0, 0x0, 0x0, 0x0, 0x1]  # 4
]

dirs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

start = (4,4)
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