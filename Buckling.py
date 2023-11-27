import math

# Not an amazing python file, just a glorified calculator

# Case 1
# Four sides restrained
# Assumes the member is horizontal
def thin_plate_buckling_c1(clear_distance, t = 1.27):

    b = clear_distance
    POISSONS_RATIO = 0.2
    E = 4000 #[N/mm^2]
    K = 4

    CONSTANT = K * (math.pi)**2 * E / (12 * (1-POISSONS_RATIO**2))
    CALC = (t/b)**2
    return CALC * CONSTANT

# Case 2
# Three sides restrained
# Assumes the member is horizontal
def thin_plate_buckling_c2(clear_distance, t = 1.27):

    b = clear_distance
    POISSONS_RATIO = 0.2
    E = 4000 #[N/mm^2]
    K = 0.425

    CONSTANT = K * (math.pi)**2 * E / (12 * (1-POISSONS_RATIO**2))
    CALC = (t/b)**2
    return CALC * CONSTANT

# Case 3
# Four sides restrained
# Assumes the member is vertical and in compession
def thin_plate_buckling_c3(clear_distance, t = 1.27):

    b = clear_distance
    POISSONS_RATIO = 0.2
    E = 4000 #[N/mm^2]
    K = 6

    CONSTANT = K * (math.pi)**2 * E / (12 * (1-POISSONS_RATIO**2))
    CALC = (t/b)**2
    return CALC * CONSTANT

# Case 4
# Four sides restrained
# Assumes the member is vertical
# Calculates shear buckling
def thin_plate_buckling_shear(clear_distance, diaphram_dist, t = 1.27):

    a = diaphram_dist
    b = clear_distance
    POISSONS_RATIO = 0.2
    E = 4000 #[N/mm^2]
    K = 5
    
    CONSTANT = K * (math.pi)**2 * E / (12 * (1-POISSONS_RATIO**2))
    CALC = (t/b)**2 + (t/a)**2
    return CALC * CONSTANT


if __name__ == "__main__":
    print("Hello")
    print(thin_plate_buckling_c1(80, 2*1.27))
    # Should return 13.8
    print(thin_plate_buckling_c2(20, 2*1.27))
    # Should return 23.5
    print(thin_plate_buckling_c3(60-1.5, 1.5))
    # Should return 13.518
    print(thin_plate_buckling_shear(80, 100))
    # Value not tested but should be correct.
