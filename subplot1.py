import numpy as np
import matplotlib.pyplot as plt

# compute x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# first plot for the sine curve
plt.subplot(2, 1, 1)  # setting up a subplot grid of height 2 and width 1, and first plot is active
plt.plot(x, y_sin)
plt.title('Sine Curve')
# second plot for the cosine curve
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine Curve')
# Display the plots
plt.show()
