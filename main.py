import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def parse_num(obs, ref):
    num = []
    for x_obs in range(0, len(obs), 13):
        obs_digit = obs[x_obs : x_obs+13, :, :]
        min_diff = np.infty
        digit = None
        for x_ref in range(0, len(ref), 13):
            ref_digit = ref[x_ref : x_ref+13, :, :]
            diff = np.sqrt(np.sum(np.square(ref_digit - obs_digit)))
            if diff < min_diff:
                min_diff = diff
                digit = x_ref // 13
        num += str(digit)
    return int("".join(num))

arr = np.array(Image.open("amazon.png")).transpose((1, 0, 2))
ref = np.array(Image.open("numbers.png").convert("RGB")).transpose((1, 0, 2))

plot_area = arr[84:1606, 48:856]
y_max = arr[24:63, 41:58]
y_min = arr[24:63, 849:866]
y_max_num = parse_num(y_max, ref)
y_min_num = parse_num(y_min, ref)
y_range = y_max_num - y_min_num
series_max = []
series_min = []
for x, col in enumerate(plot_area):
    ys = []
    for y, rgb in enumerate(col):
        if np.all(rgb == [99, 168, 94]):
            ys.append(y)
        elif np.all(rgb == [51, 51, 51]):
            break
    if ys:
        series_max.append((856 - max(ys)) / 856 * y_range + y_min_num)
        series_min.append((856 - min(ys)) / 856 * y_range + y_min_num)
    else:
        series_max.append(np.nan)
        series_min.append(np.nan)



sns.lineplot([series_max, series_min])
plt.show()