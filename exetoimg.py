import numpy as np
from math import sqrt, ceil
import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2

root = tk.Tk()
root.withdraw()
input_file_name = askopenfilename()

with open(input_file_name, 'rb') as binary_file:
    data = binary_file.read()

data_len = len(data)

d = np.frombuffer(data, dtype=np.uint8)

sqrt_len = int(ceil(sqrt(data_len)))

new_len = sqrt_len*sqrt_len

pad_len = new_len - data_len

padded_d = np.hstack((d, np.zeros(pad_len, np.uint8)))

im = np.reshape(padded_d, (sqrt_len, sqrt_len))

cv2.imwrite(input_file_name + '.png', im)

cv2.imshow('im' ,im)
cv2.waitKey(0)
cv2.destroyAllWindows()
