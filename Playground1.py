import Bridge_geometry
import Flex_stress


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

#I = Bridge_geometry.I(beam_list)
#yb = Bridge_geometry.y_bar(beam_list)
#y_top = Bridge_geometry.y_top(beam_list)

# Have to integrate with Ian's code later
M = 1000 # multiplied by ____ factor p
V = 546 # multuplied by ____ factor p

# Unironically really hard to do the rest of the steps without a good BMD and SFD

#print(I, yb)


# Geometry 2 Square


#            <100>
#    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   | 1.27        |
#    |                  |   | 1.27        |
#    |__________________|   | 1.27        | *three layers at top
#     |  |___|   |__|  |    | 1.27  |     | 
#     |  |<15>  <15>|  |    |       |     |
#     |  |          |  |    |       |     | 100
#     |  |          |  |    |       |     |
#     |  |<15>  <15>|  |    |       |94.92|
#     |  |___    ___|  |    |       |     |
#     |  |___|__|___|  |    |       |     |
#     |__|__________|__|    | 1.27
#    <1.27>  <80>   <1.27>
#            


beam_list = [   [100, 100   ,  1.27],
                [100 - 1.27, 100   ,  1.27],
                [100 - 2 * 1.27, 100,  1.27],
                [100 - 3*1.27,   15   ,  1.27],
                [100 - 3*1.27,   15   ,  1.27],
                [100  - 3*1.27,   1.27, 100-4*1.27],
                [100  - 3*1.27,   1.27, 100-4*1.27],
                [1.27*2 , 15, 1.27],
                [1.27*2 , 15, 1.27],
                [1.27   ,   80, 1.27]
                ]

I = Bridge_geometry.I(beam_list)
yb = Bridge_geometry.y_bar(beam_list)
y_top = Bridge_geometry.y_top(beam_list)
M_max = 0.0782 * 10 ** 6 #[Nmm] times factor P / 446.667 where P is the heaviest load 
V = 296.48 #[N] times factor P / 446.667 where P is the heaviest load 

# I and y_bar
print(I)
print(yb)

# flexurial stresses.

stress_top = Flex_stress.sigma_top(beam_list, M_max)
stress_bot = Flex_stress.sigma_bottom(beam_list, M_max)
tau_cent = Flex_stress.tau_cent(beam_list, V)

print("In tension:")
print(stress_top, stress_bot)
print("strain:")
print(tau_cent)

