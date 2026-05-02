import matplotlib.pyplot as plt

# Vs values
Vs = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

# Vo for different AV values
Vo_av05 = [-13.97, -12, -9, -6, -3, 0.0025, 3, 6, 9, 12, 13.97]
Vo_av1  = [-13.95, -13.95, -12, -8, -4, 0.003, 4, 8, 12, 13.95, 13.95]
Vo_av2  = [-13.97, -13.97, -13.97, -12, -6, 0.005, 6, 12, 13.97, 13.97, 13.97]

# Plot
plt.figure(figsize=(8,6))
plt.plot(Vs, Vo_av05, 'g', label="AV = 1.5")
plt.plot(Vs, Vo_av1, 'r', label="AV = 2")
plt.plot(Vs, Vo_av2, 'b', label="AV = 3")

# Axis
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# Labels
plt.xlabel("Vo (V)")
plt.ylabel("Vs (V)")
plt.title("")


# Grid and legend
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()

plt.show()

