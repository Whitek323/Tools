import matplotlib.pyplot as plt

# Vs values
Vs = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]

# Vo for different AV values
Vo_av05 = [5, 4, 3, 2, 1, 0.0025, -1, -2, -3, -4, -5]
Vo_av1  = [10, 8, 6, 4, 2, 0.003, -2, -4, -6, -8, -10]
Vo_av2  = [13.948, 13.952, 12, 8, 4, 0.005, -4, -8, -12, -13.952, -13.948]

# Plot
plt.figure(figsize=(8,6))
plt.plot(Vs, Vo_av05, 'g', label="AV = 0.5")
plt.plot(Vs, Vo_av1, 'r', label="AV = 1")
plt.plot(Vs, Vo_av2, 'b', label="AV = 2")

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

