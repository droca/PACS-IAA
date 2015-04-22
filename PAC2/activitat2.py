# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import matplotlib.pyplot as plt

# --- Activitat 2 --- #

# We read the data from the file
rawData = fp.readFileData()

# Save values for regions and channels for later
regions = fp.regionsExtraction(rawData)
channels = fp.channelsExtraction(rawData)

projection = fp.pcaWithComponents(rawData, 2)

# We represent the graf where the channels are colored differently
fig1 = plt.figure()
fig1.canvas.set_window_title('Color by channels')
plt.scatter(projection[:,0],projection[:,1],marker='o',c=channels)


# We represent the graf where the regions are colored differenttly
fig2 = plt.figure()
fig2.canvas.set_window_title('Color by regions')
plt.scatter(projection[:,0],projection[:,1],marker='o',c=regions)
plt.show()
