# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import matplotlib.pyplot as plt


# --- Activitat 4 --- 
# We read the data from the file
rawData = fp.readFileData()

# Save values for regions and channels for later
regions = fp.regionsExtraction(rawData)
channels = fp.channelsExtraction(rawData)

mds = fp.mdsComputation(rawData)

fig1 = plt.figure()
fig1.canvas.set_window_title('Color by channels')
plt.scatter(mds[:,0],mds[:,1],marker='o',c=channels)

fig2 = plt.figure()
fig2.canvas.set_window_title('Color by regions')
plt.scatter(mds[:,0],mds[:,1],marker='o',c=regions)

plt.show()