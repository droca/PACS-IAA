# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import matplotlib.pyplot as plt

# --- Activitat 3 --- #
# We read the data from the file
rawData = fp.readFileData()

# Save values for regions and channels for later
regions = fp.regionsExtraction(rawData)
channels = fp.channelsExtraction(rawData)

projection = fp.pcaWithComponents(rawData, 4)


# Figure representation, using the second and third components

# We represent the figure where the channels are colored differently
fig1 = plt.figure()
fig1.canvas.set_window_title('Components 2 & 3. Color by channels')
plt.scatter(projection[:,1],projection[:,2],marker='o',c=channels)

# We represent the figure where the regions are colored differenttly
fig2 = plt.figure()
fig2.canvas.set_window_title('Components 2 & 3. Color by regions')
plt.scatter(projection[:,1],projection[:,2],marker='o',c=regions)


# Figure representation, using the third and fourth components
# We represent the figure where the channels are colored differently
fig1 = plt.figure()
fig1.canvas.set_window_title('Components 3 & 4. Color by channels')
plt.scatter(projection[:,2],projection[:,3],marker='o',c=channels)

# We represent the figure where the regions are colored differenttly
fig2 = plt.figure()
fig2.canvas.set_window_title('Components 3 & 4. Color by regions')
plt.scatter(projection[:,2],projection[:,3],marker='o',c=regions)


# Print all the figures
plt.show()