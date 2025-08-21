import numpy as np
import pandas as pd

mu = [2.2, 2.4, 3.1, 3.5] # friction coefficient (race tires)
g = 9.81 # gravity
a_acc = 23 # max acceleration (m/s^2)
a_brake = [curr_mu * g for curr_mu in mu] # max braking decel (m/s^2)
ds = 50.0 # segment length (m)

curvatures = [0.0, 0.01, 0.0, 0.05, 0.0]

# v_max
v_max = [np.sqrt(a_brake[i] / curvatures[i]) if curvatures[i] > 1e-6 else 1e6 for i in range(len(curvatures))]

# forward pass (accel-limited)
v_forward = [0.0] * len(v_max)
for i in range(len(v_max) - 1):
    v_possible = np.sqrt(v_forward[i] ** 2 + 2 * a_acc * ds)
    v_forward[i + 1] = min(v_max[i + 1], v_possible)

# backward pass (brake-limited)
v_final = v_forward[:]
for i in reversed(range(len(v_max) - 1)):
    v_possible = np.sqrt(v_final[i + 1] ** 2 + 2 * a_brake[i] * ds)
    v_final[i] = min(v_final[i], v_possible)

df = pd.DataFrame({
    "Segment": np.arange(len(curvatures)),
    "Curvature": curvatures,
    "v_max_curve": np.round(v_max, 2),
    "v_forward": np.round(v_forward, 2),
    "v_final": np.round(v_final, 2)
})

print(df)