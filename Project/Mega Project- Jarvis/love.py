import matplotlib.pyplot as plt
import numpy as np

# Create a heart shape using parametric equations
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(8, 6))
plt.ion()  # Turn on interactive mode

step_size = 16  # Increase step size for faster drawing

for i in range(1, len(t) + 1, step_size):
    plt.plot(x[:i], y[:i], color='red', linewidth=2)
    plt.fill(x[:i], y[:i], color='#f51707', alpha=0.3)
    plt.axis('off')
    plt.pause(0.01)  # Pause to create the animation effect

# Add text inside the heart after it's fully drawn
plt.text(0, 0, 'Bacchu', fontsize=20, fontweight='bold', color='white', ha='center', va='center')

# Turn off interactive mode and display the final plot
plt.ioff()
plt.show()
