# Calculates the different stresses so that I can import this file
import Bridge_geometry
import numpy as np
E = 4000 #MPa
mu = 0.2
t = 1.27 #mm
number_layers_on_top = 3
number_of_supports = 2
d_mid = 80 #mm
h = 100 #mm
# distance from support where the maxixum shear is
d_max = 200 #mm

d_side = 10 #mm
h_glue = 75 #mm

def sigma_depth(beam_list, M, dist_from_bottom):
    I = Bridge_geometry.I(beam_list)
    h = dist_from_bottom
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I

def sigma_top(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    h = Bridge_geometry.y_top(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I

def sigma_bottom(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (yb) / I

def tau_cent(beam_list, V):
    yb = Bridge_geometry.y_bar(beam_list)
    Q = Bridge_geometry.Q(beam_list, yb)
    I = Bridge_geometry.I(beam_list)
    b_c = Bridge_geometry.horizontal_thickness(beam_list, yb)
    return V * Q/(I*b_c)

def tau_glue(beam_list, V, depth_of_interest, glue_width):
    h = depth_of_interest
    Q = Bridge_geometry.Q(beam_list, h)
    I = Bridge_geometry.I(beam_list)

def sigma_cr1():
    return (4*np.pi**2 * E ) / (12*(1-mu)**2) * (t*number_layers_on_top/d_mid)**2
def sigma_cr2():
    return (0.425*np.pi**2 * E ) / (12*(1-mu)**2) * (t*number_layers_on_top/d_side)**2
def sigma_cr3(beam_list):
    y_bar = Bridge_geometry.y_bar(beam_list)
    return (6*np.pi**2 * E ) / (12*(1-mu)**2) * (t/(h_glue-y_bar))**2
def tau_cr4():
    return (5*np.pi**2 * E ) / (12*(1-mu)**2) * ((t*number_of_supports/h)**2+(t*number_of_supports/d_max)**2)

if __name__ == "__main__":
    beam_list = [[76.27, 100   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   5   ,  1.27],
                 [75   ,   1.27, 75  ],
                 [75   ,   1.27, 75  ],
                 [ 1.27,  77.46,  1.27]
                 ]
    print(tau_cent(beam_list, 100))
    print(tau_glue(beam_list, 100, 50, 2.54))

    print(sigma_depth(beam_list, 100, 50))
    print(tau_glue(beam_list, 100, 50, 2.54))