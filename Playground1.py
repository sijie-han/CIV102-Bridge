import Bridge_geometry
import Buckling


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
M = 120 # multiplied by ____ factor p
V = 30000 # multuplied by ____ factor p

# Unironically really hard to do the rest of the steps without a good BMD and SFD

print(I, yb)

