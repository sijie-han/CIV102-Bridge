import numpy as np
import matplotlib.pyplot as plt

# Parameters
bridge_length = 1200  # Length of the bridge in mm
train_length = 856  # Length of the train in mm
train_load = 400  # Total load of the train in N

# Load per mm of the train
load_per_mm = train_load / train_length

# Function to calculate the shear force at a point for a given train position
def shear_force_at_point(x, train_start, load_per_mm, train_length):
    train_end = train_start + train_length
    # If the point is before the train or after the train, shear force is zero
    if x < train_start or x > train_end:
        return 0
    # If the point is under the train, calculate the shear force
    if x <= (train_start + train_end) / 2:
        # Left side of the train
        return load_per_mm * (x - train_start)
    else:
        # Right side of the train
        return load_per_mm * (train_end - x)

# Initialize an array to store the maximum shear force at each point
max_shear_force = np.zeros(bridge_length + 1)

# Calculate the maximum shear force at each point considering all train positions
for train_start in range(-train_length, bridge_length + 1):
    for x in range(bridge_length + 1):
        sf = shear_force_at_point(x, train_start, load_per_mm, train_length)
        max_shear_force[x] = max(max_shear_force[x], sf)

# Plot the shear force envelope
plt.plot(max_shear_force, label='Maximum Shear Force')
plt.xlabel('Position on Bridge (mm)')
plt.ylabel('Shear Force (N)')
plt.title('Shear Force Envelope for Moving Train Load')
plt.legend()
plt.grid(True)
plt.show()
