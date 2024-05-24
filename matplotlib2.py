import numpy as np
import matplotlib.pyplot as plt

# compute x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Plot the sine and cosine curves
plt.plot(x, y_sin)
plt.plot(x, y_cos)
# Add labels and title
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine Curves')
# Add a legend
plt.legend(['Sine', 'Cosine'])
# Display the plot
plt.show()
