
import numpy as np

# load .npy 文件
data = np.load('data/power_asd.npy', allow_pickle=True)

#print("数据形状:", data.shape)
#print("数据类型:", data.dtype)
#print("前几行数据:", data[:5])

import matplotlib.pyplot as plt

# visual the first image
plt.imshow(data[0], cmap='gray')
plt.colorbar()
plt.show()


