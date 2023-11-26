import Bridge_geometry
import Buckling
import Stress


# Geomtry 0, Design 0

# Geometry 1 Bentz design


#            <120>
#   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   | 1.27
#   |____________________|   | 1.27      *Two layers at top
#     |  |___|   |__|  |     | 1.27    | 
#     |  |<10>  <10>|  |               |
#     |  |          |  |               | 100
#     |  |          |  |               |
#     |  |          |  |               |
#     |__|          |__|               |
#    <1.27>         <1.27>

beam_list = [   [100 + 2*1.27, 120   ,  1.27],
                [100 + 1.27, 120   ,  1.27],
                [100   ,   10   ,  1.27],
                [100   ,   10   ,  1.27],
                [100   ,   1.27, 100  ],
                [100   ,   1.27, 100  ],
                ]


I = Bridge_geometry.I(beam_list)
yb = Bridge_geometry.y_bar(beam_list)
y_top = Bridge_geometry.y_top(beam_list)

# Have to integrate with Ian's code later
M = 1000 # multiplied by ____ factor p
V = 546 # multuplied by ____ factor p

# Unironically really hard to do the rest of the steps without a good BMD and SFD

print(I, yb)


# Geometry 1 Bentz design


#            <100>
#     |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   | 1.27
#     |_________________|   | 1.27      *One layers at top
#     |  |___|   |__|  |    | 1.27     | 
#     |  |<10>  <10>|  |               |
#     |  |          |  |               | 100
#     |  |          |  |               |
#     |  |          |  |               |
#     |__|__________|__|               |
#     |________________|
#    <1.27>         <1.27>


beam_list = [   [100 + 1.27, 100   ,  1.27],
                [100   ,   10   ,  1.27],
                [100   ,   10   ,  1.27],
                [100   ,   1.27, 100-1.27],
                [100   ,   1.27, 100-1.27],
                [1.27   ,   1.27, 100  ],
                ]

I = Bridge_geometry.I(beam_list)
yb = Bridge_geometry.y_bar(beam_list)
y_top = Bridge_geometry.y_top(beam_list)
M_max = 83851.323
V = 307.145

# Calculating max stresses.
sigma_compression = Stress.sigma_top(beam_list, M_max)
print(f"sigma_compression = {sigma_compression}")
sigma_tension = Stress.sigma_bottom(beam_list, M_max)
print(f"sigma_tension = {sigma_tension}")
tau_g = Stress.tau_glue(beam_list, V, 98.73, 20+2*1.27)  # Convert kN to N
print(f"tau_glue = {tau_g}")
tau_max = Stress.tau_cent(beam_list, V)  # Convert kN to N
print(f"tau_max = {tau_max}")


FOS_tension = 30 / sigma_tension
print(f"FOS_tension = {FOS_tension}")
FOS_compression = 6 / sigma_compression
print(f"FOS_compression = {FOS_compression}")
FOS_shear = 4 / tau_max
print(f"FOS_shear = {FOS_shear}")
FOS_glue = 2 / tau_g
print(f"FOS_glue = {FOS_glue}")

# Buckling
FOS_shear_buckling = tau_cr4() / tau_max
print(f"FOS_shear_buckling = {FOS_shear_buckling}")
FOS_flexural_buckling1 = sigma_cr1() / sigma_compression
print(f"FOS_flexural_buckling1 = {FOS_flexural_buckling1}")
FOS_flexural_buckling2 = sigma_cr2() / sigma_compression
print(f"FOS_flexural_buckling2 = {FOS_flexural_buckling2}")
FOS_flexural_buckling3 = sigma_cr3(beam_list) / sigma_compression
print(f"FOS_flexural_buckling3 = {FOS_flexural_buckling3}")