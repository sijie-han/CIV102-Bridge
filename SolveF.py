import numpy as np
import matplotlib.pyplot as plt

# Parameters
Fc = 133.3
Fl = 180
L = 1260  # Bridge Length in mm
E = 4000  # Elastic Modulus in MPa
u = 0.2   # Poisson's Coefficient
t = 1.27  # Plate thickness in mm
w = 100   # Top plate width in mm
b = 75    # Side Plate Width in mm
bw = 80   # Width of something (not specified in the provided code)

# Material Properties (Not used in SFD and BMD calculations)
t1 = 30  # Tensile Strength
t2 = 6   # Compressive Strength
s1 = 4   # Shear Strength
sc = 2   # Contact Cement Strength

# Initialize SFD and BMD arrays
SFD_Max = np.zeros((L + 857, L + 1))
BMD_Max = np.zeros((L + 857, L + 1))

# Integrate the train position
for x in range(L + 857):
    Load = np.array([Fc/2, Fc/2, Fc/2, Fc/2, Fl/2, Fl/2])
    Wheel_pos = np.array([x-856, x-680, x-516, x-340, x-176, x])
    valid = (Wheel_pos > 0) & (Wheel_pos < L)
    Load = Load[valid]
    Wheel_pos = Wheel_pos[valid]

    # Find reaction force
    By = sum(Load * (Wheel_pos / 1000)) / (L / 1000)
    Ay = sum(Load) - By

    # Find SFD for each location
    SFD = [Ay] + [0] * len(Load)
    for i in range(1, len(SFD)):
        SFD[i] = SFD[i - 1] - Load[i - 1]
    SFD.append(SFD[-1] + By)
    
    # Find the SFD at each location
    for d in range(L + 1):
        index = np.where(Wheel_pos <= d)[0]
        SFD_at_d = Ay if index.size == 0 else SFD[index[-1] + 1]
        SFD_Max[x, d] = SFD_at_d

    # Calculate the BMD at each point
    BMD = np.zeros(L + 1)
    for d in range(1, L + 1):
        BMD[d] = BMD[d - 1] + SFD_Max[x, d - 1]
    BMD_Max[x, :] = BMD

# Find maximum SFD and BMD
SFD_max_index = np.max(np.abs(SFD_Max), axis=0)
BMD_max_index = np.max(np.abs(BMD_Max), axis=0)
print('Maximum SFD: {} N'.format(SFD_max_index.max()))
print('Maximum BMD: {} N-mm'.format(BMD_max_index.max()))
# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(range(L + 1), SFD_max_index, label='Max SFD')
plt.title('Maximum Shear Force Diagram')
plt.xlabel('Position on Bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(range(L + 1), BMD_max_index, label='Max BMD')
plt.title('Maximum Bending Moment Diagram')
plt.xlabel('Position on Bridge (mm)')
plt.ylabel('Bending Moment (N-mm)')
plt.legend()

plt.tight_layout()
plt.show()
