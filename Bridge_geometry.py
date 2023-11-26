# y_bar, I and Q functions are solid

def y_bar(beam_list):
    # Accepts a 2D list of arguements,
    # Each element in the list should be of the form:
    # [y, width, height]
    # Where y is the vertical distance from an axis |^|
    # defined as 0 to the top of the beam
    # Where width is the width of the beam ____>
    # Where height is the height of the beam |^|
    # Outputs y_bar in mm
    y_sum = 0
    a_tot = 0
    for beam in beam_list:
        y_sum += (beam[0] - beam[2] / 2) * beam[1] * beam[2]
        a_tot += beam[1] * beam[2]
    return y_sum / a_tot

# Stupid function. Returns y_top
def y_top(beam_list):
    return max([beam[0] for beam in beam_list])

def I(beam_list):
    # y_bar must be a number
    # beam_list must be a 2D list of arguements,
    # Each element in the list should be of the form:
    # [y, width, height]
    # Where y is the vertical distance from an axis 
    # defined as 0
    # Where width is the width of the beam
    # Where height is the height of the beam
    # Outputs I in mm4
    i_o_sum = 0
    vert_sum = 0
    y_b = y_bar(beam_list)
    for beam in beam_list:
        i_o_sum += beam[2]**3 * beam[1] / 12
        vert_sum += ((beam[0] - beam[2] / 2 - y_b)**2) * beam[1] * beam[2]
    return i_o_sum + vert_sum

def Q(beam_list, h):
    # Accepts a 2D list of arguments,
    # Each element in the list should be of the form:
    # [y, width, height]
    # Where y is the vertical distance from an axis 
    # defined as 0 to the top of the beam
    # Where width is the width of the beam
    # Where height is the height of the beam
    # Outputs Q in mm3
    aug_b_list = []
    area = 0
    for beam in beam_list:
        if beam[0] < h:
            aug_b_list.append(beam.copy())
            area += beam[1] * beam[2]
        elif beam[0] - beam[2] < h:
            aug_b_list.append(beam.copy())
            aug_b_list[-1][0] = h
            aug_b_list[-1][2] = h - (beam[0] - beam[2])
            area += aug_b_list[-1][1] * aug_b_list[-1][2]
    
    d = abs(y_bar(beam_list) - y_bar(aug_b_list))
    return d * area

def horizontal_thickness(beam_list, depth):
    # Not great at boundaries
    h = depth
    thickness = 0
    unknown_thickness = 10000
    for beam in beam_list:
        if beam[0] >= h and ((beam[0] - beam[2]) <= h):
            thickness += beam[1]

    return thickness

if __name__ == "__main__":
    beam_list = [[76.27, 100   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   1.27, 75  ],
                 [75   ,   1.27, 75  ],
                 [ 1.27,  77.46,  1.27]
                 ]
    #print(y_top(beam_list))
    y = y_bar(beam_list)
    #print(y)
    #print(I(beam_list))
    print(horizontal_thickness(beam_list, 74))

    beam_list = [[241, 241, 241]]
    print(Q(beam_list, 120.5))

    beam_list = [[100+1.27*2, 120, 1.27],
                 [100+1.27*1, 120, 1.27],
                 [100, 20 + 2*1.27, 1.27],
                 [100-1.27, 1.27, 100-1.27],
                 [100-1.27, 1.27, 100-1.27],]
    print(y_bar(beam_list))

    beam_list = [[100+1.27*4, 120, 1.27],
                 [100+1.27*3, 120, 1.27],
                 [100+1.27*2, 120, 1.27],
                 [100+1.27*1, 120, 1.27],
                 [100, 20 + 2*1.27, 1.27],
                 [100-1.27, 1.27, 100-1.27],
                 [100-1.27, 1.27, 100-1.27],]
    fg = y_bar(beam_list)
    print(fg/(100+1.27*4 - fg))
    
beam_list = [[120, 120   ,  1.27],
                [120 - 1.27   ,   1.27   ,  120-2*1.27],
                [120 - 1.27   ,   1.27   ,  120-2*1.27],
                [0   ,   120, 1.27  ],
                ]