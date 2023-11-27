import Bridge_geometry
import Flex_stress
import Buckling


# Geomtry 0, Design 0
beam_list = [[76.27, 100   ,  1.27],
                [75   ,   5   ,  1.27],
                [75   ,   5   ,  1.27],
                [75   ,   1.27, 75  ],
                [75   ,   1.27, 75  ],
                [ 1.27,  77.46,  1.27]
                ]

I = Bridge_geometry.I(beam_list)
yb = Bridge_geometry.y_bar(beam_list)
y_top = Bridge_geometry.y_top(beam_list)
M_max = 69800 #[Nmm] times factor P / 446.667 where P is the heaviest load 
V = 257 #[N] times factor P / 446.667 where P is the heaviest load 
Diaphragm_distribution = 200
# I and y_bar
print(f"I value: {I} mm4")
print(f"y_bar : {yb}mm")

# flexurial stresses and shear stresses
stress_top = Flex_stress.sigma_top(beam_list, M_max)
stress_bot = Flex_stress.sigma_bottom(beam_list, M_max)
tau_cent = Flex_stress.tau_cent(beam_list, V)
tau_glue = Flex_stress.tau_glue(beam_list, V, 75, 5*2 + 1.27*2)

print(f"Compressive stress: {stress_top}")
print(f"Tensile stress: {stress_bot}")
print(f"Shear stress: {tau_cent}")
glue_stress = tau_glue
print(f"strain on glue: {tau_glue}")

# Tension FOS
min_FOS = 100
print(f"FOS tension: {30/stress_bot}")
min_FOS = min(min_FOS, 30/stress_bot)
print(f"FOS compression: {6/stress_top}")
min_FOS = min(min_FOS, 6/stress_top)
print(f"FOS sheer: {4/tau_cent}")
min_FOS = min(min_FOS, 4/tau_cent)
print(f"FOS glue: {2/glue_stress}")
min_FOS = min(min_FOS, 2/glue_stress)

# Thin plate buckling
# Bottom member case 1
stress = stress_top
print("Thin plate buckling:")
buck_c1 = Buckling.thin_plate_buckling_c1(77.46, t = 1.27)
print(f"Buck1: {buck_c1}")
print(f"FOS Thin plate buckling for c1: {buck_c1/stress}")


# Side flanges case 2
buck_c2 = Buckling.thin_plate_buckling_c2(10, t = 1.27)
print(f"Buck2 {buck_c2}")
#print(stress)
print(f"FOS Thin plate buckling for c2: {buck_c2/stress}")

min_FOS = min(min_FOS, buck_c2/stress)

# Vertical members case 3
buck_c3 = Buckling.thin_plate_buckling_c3(75 - yb)
print(f"Buck3: {buck_c3}")
print(f"FOS: Thin plate buckling for c3: {buck_c3/stress}")
min_FOS = min(min_FOS, buck_c3/stress)

# Shear buckling case 4
buck_c4 = Buckling.thin_plate_buckling_shear(75, Diaphragm_distribution)
print(f"Buck Shear {buck_c4}")
print(f"FOS: Thin plate buckling for Shear: {buck_c4/tau_cent}")
min_FOS = min(min_FOS, buck_c4/stress)

print(f"Max force is it can resist: {min_FOS*466.667}")