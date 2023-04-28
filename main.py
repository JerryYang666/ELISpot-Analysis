import matplotlib.pyplot as plt
import numpy as np

# generate some random data
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)

# create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# create a histogram of the first dataset on the first subplot
axs[0].hist(data1, bins=30)
axs[0].set_title("Histogram of Data 1")

# create a histogram of the second dataset on the second subplot
axs[1].hist(data2, bins=30)
axs[1].set_title("Histogram of Data 2")

# adjust the spacing between the subplots and the edges
fig.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

# set the overall title of the figure
fig.suptitle("Histograms of Random Data")

plt.show()

