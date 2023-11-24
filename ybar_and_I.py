def y_bar(beam_list):
    # Accepts a 2D list of arguements,
    # Each element in the list should be of the form:
    # [y, width, height]
    # Where y is the vertical distance from an axis 
    # defined as 0 to the top of the beam
    # Where width is the width of the beam
    # Where height is the height of the beam
    # Outputs y_bar
    y_sum = 0
    a_tot = 0
    for beam in beam_list:
        y_sum += (beam[0] - beam[2] / 2) * beam[1] * beam[2]
        a_tot += beam[1] * beam[2]
    return y_sum / a_tot

def I(beam_list):
    # y_bar must be a number
    # beam_list must be a 2D list of arguements,
    # Each element in the list should be of the form:
    # [y, width, height]
    # Where y is the vertical distance from an axis 
    # defined as 0
    # Where width is the width of the beam
    # Where height is the height of the beam
    # Outputs I
    i_o_sum = 0
    vert_sum = 0
    y_b = y_bar(beam_list)
    for beam in beam_list:
        i_o_sum += beam[2]**3 * beam[1] / 12
        vert_sum += (y_b - beam[0] + beam[2] / 2) ** 2 * beam[1] * beam[2]
    return i_o_sum + vert_sum

def Q(beam_list):
    pass

if __name__ == "__main__":
    beam_list = [[76.27, 100   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   1.27, 75  ],
                 [75   ,   1.27, 75  ],
                 [ 1.27,  77.46,  1.27]
                 ]
    
    y = y_bar(beam_list)
    print(y)
    print(I(beam_list))
    