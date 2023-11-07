import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

labels = pd.read_csv(r'labels.csv', header=None)

image_name = "case_0001256_00217_F_a_F_UU_H_N_G_G_01.jpg" # input the image name 
im = plt.imread(image_name)

ls = labels[labels[3] == image_name]

xx = ls[4].tolist()[0]
yy = ls[5].tolist()[0]

list_i = ls[1].tolist()
list_j = ls[2].tolist()
list_z = ls[0].tolist()

i = list(list_i[:])
j = list(list_j[:])
z = list(list_z[:])

ii = [int(t) for t in i]
jj = [int(t) for t in j]
zz = [int(t) for t in z]

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig, ax = plt.subplots()
im = ax.imshow(im, extent=[0, xx, yy, 0])

plt.scatter(ii, jj)

for a, b in enumerate(jj):
    pp = plt.annotate(zz[a], (ii[a], jj[a]), ha="center")

plt.show()





