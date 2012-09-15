def next_step(pairs):
    if len(pairs) <= 2:
        return set()

def get_adjacent(cell):
    x, y = cell
    
    offsets = [-1, 0, 1]
    adjacent_cells = []
    for i in offsets:
        for j in offsets:
            adjacent_cell = (x + i, y + j)
            
            if adjacent_cell == cell:
                continue
            
            adjacent_cells.append(adjacent_cell)
    
    return set(adjacent_cells)
