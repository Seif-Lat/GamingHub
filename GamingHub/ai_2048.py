def set_direction(grid, dic_values):
    dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
    moves = dic_values["moves"]
    ai_timer = dic_values["round"] % 3
    if dic_move[ai_timer+1] in dic_values["moves"]:
        return dic_move[ai_timer+1]
    elif 'g' in dic_values["moves"]:
        return 'g'
    else:
        return dic_values["moves"][0]

def set_size_grid(grid, dic_values):
    return 4

def set_theme_grid(grid, dic_values):
    return 0
