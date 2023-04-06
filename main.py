from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

im = Image.open("amazon.png")
arr = np.array(im).transpose((1, 0, 2))
print(arr.shape)
series_max = []
series_min = []
for x, col in enumerate(arr):
    ys = []
    for y, rgb in enumerate(col):
        if np.all(rgb == [99, 168, 94]):
            ys.append(y)
        elif np.all(rgb == [51, 51, 51]):
            break
    if ys:
        series_max.append(-max(ys))
        series_min.append(-min(ys))
    else:
        series_max.append(np.nan)
        series_min.append(np.nan)

sns.lineplot([series_max, series_min])
plt.show()