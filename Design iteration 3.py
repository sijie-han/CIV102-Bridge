# Calculates the different stresses so that I can import this file
import Bridge_geometry
import numpy as np
E = 4000 # MPa
mu = 0.2
t = 1.27 # mm
h = 120 # mm
top_width = 100 # mm
# the dimensions of the beam in the format [height, width, thickness]
# A rough sketch of the crkoss section of the beam
#   <--------100--------->
#   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   | 1.27
#   |                    |   | 1.27
#   |____________________|   | 1.27    3 layers at top
#1.27 |___  |    |  ___|  1.27        | 
#        |  |<80>|  |                 | 
#        |  |    |  |                 | 
#        |  |    |  |                 |120 - 3*1.27
#     ___|  |    |  |___              |
#1.27|______|    |______|  1.27       |
#    |<7>|1.27  1.27|<7>|
beam_list = [[h, top_width   ,  t*3],
             [h-3*t   ,  7   ,  t],
             [h-3*t  ,   7   ,  t],
             [h-3*t   ,  t, h-3*t ],
             [h-3*t  ,   t, h-3*t],
             [t  ,   7, t],
             [t, 7, t ] 
             ]
P_max = 300 # N
M_max = 78200  # N-mm
h_glue = beam_list[2][0]
number_layers_on_top = beam_list[0][2] / t
number_of_supports = 2
d_mid = 80 # mm
h = beam_list[0][0] # mm
glue_width = 2*(7) # mm
# distance from support and where the maximum shear is
d_max = 100 # mm
d_side = (top_width-d_mid)/2 - t-7  # mm



def sigma_depth(beam_list, M, dist_from_bottom):
    I = Bridge_geometry.I(beam_list)
    h = dist_from_bottom
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I
# Calculating the compressive stress at the top of the beam
def sigma_top(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    print(f"I = {I}")
    h = Bridge_geometry.y_top(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * (h - yb) / I
# Calculating the tensile stress at the bottom of the beam
def sigma_bottom(beam_list, M):
    I = Bridge_geometry.I(beam_list)
    yb = Bridge_geometry.y_bar(beam_list)
    return M * yb / I
# Calculating the shear stress at the center of the beam, which is the maximum shear stress in our case
def tau_cent(beam_list, V):
    yb = Bridge_geometry.y_bar(beam_list)
    Q = Bridge_geometry.Q(beam_list, yb)
    print(f"Q = {Q}")
    I = Bridge_geometry.I(beam_list)
    b_c = Bridge_geometry.horizontal_thickness(beam_list, yb) # width of the beam at the centroid
    return V * Q / (I * b_c)
# Calculating the shear stress at the glue layer
def tau_glue(beam_list, V, depth_of_interest, glue_width):
    h = depth_of_interest
    Q = Bridge_geometry.Q(beam_list, h)
    I = Bridge_geometry.I(beam_list)
    return V * Q / (I * glue_width)
# Calculating the case 1 thin plate buckling stress at the maximum shear point
def sigma_cr1():
    return (4 * np.pi**2 * E) / (12 * (1 - mu**2)) * (t * number_layers_on_top / (d_mid))**2
# Calculating the case 2 thin plate buckling stress at the maximum shear point
def sigma_cr2():
    return (0.425 * np.pi**2 * E) / (12 * (1 - mu**2)) * (t * number_layers_on_top / d_side)**2
# Calculating the case 3 thin plate buckling stress at the maximum shear point
def sigma_cr3(beam_list):
    y_bar = Bridge_geometry.y_bar(beam_list)
    print(f"y_bar = {y_bar}")
    return (6 * np.pi**2 * E) / (12 * (1 - mu**2) )* (t / (h_glue - y_bar))**2
# Calculating the case 4 thin plate buckling stress at the maximum shear point
def tau_cr4():
    return (5 * np.pi**2 * E) / (12 * (1 - mu**2)) * ((t / (h-t*3))**2 + (t / d_max)**2)

 # N-mm
# Calculating the different stresses
sigma_compression = sigma_top(beam_list, M_max)
print(f"sigma_compression = {sigma_compression}")
sigma_tension = sigma_bottom(beam_list, M_max)
print(f"sigma_tension = {sigma_tension}")
tau_g = tau_glue(beam_list, P_max , h_glue, glue_width)  # Convert kN to N
print(f"tau_glue = {tau_g}")
tau_max = tau_cent(beam_list, P_max )  # Convert kN to N
print(f"tau_max = {tau_max}")
# Calculating the factors of safety
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
# Calculating the maximum forces that the bridge can withstand
V_fail_shear = FOS_shear * P_max
print(f"V_fail_shear = {V_fail_shear}")
V_fail_glue = FOS_glue * P_max
print(f"V_fail_glue = {V_fail_glue}")
V_fail_shear_buckling = FOS_shear_buckling * P_max
print(f"V_fail_shear_buckling = {V_fail_shear_buckling}")
# Calculating the different moments
M_fail_buck123 = min(FOS_flexural_buckling1,FOS_flexural_buckling2,FOS_flexural_buckling3) * M_max
print(f"M_fail_buck123 = {M_fail_buck123}")
M__fail_comp = FOS_compression * M_max
print(f"M__fail_comp = {M__fail_comp}")
M_fail_tens = FOS_tension * M_max
print(f"M_fail_tens = {M_fail_tens}")