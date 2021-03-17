import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt

num_house = 123
np.random.seed(42)
house_size = np.random.randint(low=1234, high=5678, size=num_house)

np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low=23456, high=76543, size=num_house)

plt.plot(house_size, house_price, "bx")
plt.ylabel("Price")
plt.xlabel("size")
plt.show()
