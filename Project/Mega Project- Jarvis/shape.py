import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image
import time

# Measure start time
start_time = time.time()

# Define step size
step_size = 0.01

# Create a heart shape using parametric equations
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

plt.figure(figsize=(8, 6))
plt.ion()  # Turn on interactive mode

# Create the heart shape incrementally
for i in range(1, len(t) + 1, 16):  # Adjust step size here
    plt.plot(x[:i], y[:i], color='red', linewidth=2)
    plt.fill(x[:i], y[:i], color='#f51707', alpha=0.3)
    plt.axis('off')
    plt.pause(0.01)  # Pause to create the animation effect

# Add the word "Garima" inside the heart shape
plt.text(0, 0, 'Garima', fontsize=40, fontweight='bold', color='white', ha='center', va='center')

# Turn off interactive mode and display the final plot
plt.ioff()
plt.show()

# Save the final heart shape plot with the text as an image to use as a mask
fig = plt.figure(figsize=(8, 6))
plt.fill(x, y, color='black')
plt.axis('off')
plt.text(0, 0, 'Guddu', fontsize=40, fontweight='bold', color='white', ha='center', va='center')
plt.savefig('heart_with_text.png', bbox_inches='tight', pad_inches=0, transparent=True)
plt.close()

# Load the heart-shaped mask with text
heart_mask_with_text = np.array(Image.open('heart_with_text.png'))

# Generate the word cloud with the heart shape mask
text = "Garima " * 1000  # Repeat the word "Garima" to fill the heart
wordcloud = WordCloud(width=800, height=600, background_color='white', mask=heart_mask_with_text, contour_color='red', contour_width=3).generate(text)

# Measure end time
end_time = time.time()

# Display the word cloud
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('Word Cloud with Heart Mask')
plt.axis('off')
plt.show()

# Print the time taken
print(f"Time taken to generate and display the word cloud: {end_time - start_time:.2f} seconds")
