# Calculates the different stresses so that I can import this file
import Bridge_geometry
import numpy as np
E = 4000 # MPa
mu = 0.2
t = 1.27 # mm
h = 120 # mm
top_width = 100 # mm
beam_list = [[h, top_width   ,  t*2],
             [h-2*t   ,  15   ,  t],
             [h-2*t  ,   15   ,  t],
             [h-2*t   ,  t, h-2*t ],
             [h-2*t  ,   t, h-2*t] 
             ]
P_max = 300 # N
h_glue = beam_list[2][0]
number_layers_on_top = beam_list[0][2] / t
number_of_supports = 2
d_mid = 80 # mm
h = beam_list[0][0] # mm
glue_width = 2*(15+1.27) # mm
# distance from support where the maximum shear is
d_max = 150 # mm
d_side = (top_width-d_mid)/2 - t  # mm




def sigma_depth(beam_list, M, dist_from_bottom):
    I = Bridge_geometry.I(beam_list)
    h = dist_from_bottom
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I

def sigma_top(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    print(f"I = {I}")
    h = Bridge_geometry.y_top(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I

def sigma_bottom(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * yb / I

def tau_cent(beam_list, V):
    yb = Bridge_geometry.y_bar(beam_list)
    Q = Bridge_geometry.Q(beam_list, yb)
    print(f"Q = {Q}")
    I = Bridge_geometry.I(beam_list)
    b_c = Bridge_geometry.horizontal_thickness(beam_list, yb)
    return V * Q / (I * b_c)

def tau_glue(beam_list, V, depth_of_interest, glue_width):
    h = depth_of_interest
    Q = Bridge_geometry.Q(beam_list, h)
    print(f"Q_glue = {Q}")

    I = Bridge_geometry.I(beam_list)
    return V * Q / (I * glue_width)

def sigma_cr1():
    return (4 * np.pi**2 * E) / (12 * (1 - mu**2)) * (t * number_layers_on_top / (d_mid-glue_width+t*2))**2

def sigma_cr2():
    return (0.425 * np.pi**2 * E) / (12 * (1 - mu**2)) * (t * number_layers_on_top / d_side)**2

def sigma_cr3(beam_list):
    y_bar = Bridge_geometry.y_bar(beam_list)
    print(f"y_bar = {y_bar}")
    return (6 * np.pi**2 * E) / (12 * (1 - mu**2) )* (t / (h_glue - y_bar))**2

def tau_cr4():
    return (5 * np.pi**2 * E) / (12 * (1 - mu**2)) * ((t / h)**2 + (t / d_max)**2)

M_max = 83851.323 # N-mm

sigma_compression = sigma_top(beam_list, M_max)
print(f"sigma_compression = {sigma_compression}")
sigma_tension = sigma_bottom(beam_list, M_max)
print(f"sigma_tension = {sigma_tension}")
tau_g = tau_glue(beam_list, P_max , h_glue, glue_width)  # Convert kN to N
print(f"tau_glue = {tau_g}")
tau_max = tau_cent(beam_list, P_max )  # Convert kN to N
print(f"tau_max = {tau_max}")

FOS_tension = 30 / sigma_tension
print(f"FOS_tension = {FOS_tension}")
FOS_compression = 6 / sigma_compression
print(f"FOS_compression = {FOS_compression}")
FOS_shear = 4 / tau_max
print(f"FOS_shear = {FOS_shear}")
FOS_glue = 2 / tau_g
print(f"FOS_glue = {FOS_glue}")
FOS_shear_buckling = tau_cr4() / tau_max
print(f"tau_cr4 = {tau_cr4()}")
print(f"FOS_shear_buckling = {FOS_shear_buckling}")
FOS_flexural_buckling1 = sigma_cr1() / sigma_compression
print(f"sigma_cr1 = {sigma_cr1()}")
print(f"FOS_flexural_buckling1 = {FOS_flexural_buckling1}")
FOS_flexural_buckling2 = sigma_cr2() / sigma_compression
print(f"sigma_cr2 = {sigma_cr2()}")
print(f"FOS_flexural_buckling2 = {FOS_flexural_buckling2}")
FOS_flexural_buckling3 = sigma_cr3(beam_list) / sigma_compression
print(f"sigma_cr3 = {sigma_cr3(beam_list)}")
print(f"FOS_flexural_buckling3 = {FOS_flexural_buckling3}")

if __name__ == "__main__":
    print(tau_cent(beam_list, 100))
    print(tau_glue(beam_list, 100, 50, 2.54))

    print(sigma_depth(beam_list, 100, 50))
    print(tau_glue(beam_list, 100, 50, 2.54))