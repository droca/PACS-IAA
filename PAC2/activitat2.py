# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import numpy as np
import matplotlib.pyplot
# --- Activitat 2 --- #

rawData = fp.readFileData()
normalised = fp.dataNormalization(rawData)

projection = fp.pcaWithComponents(normalised, 2)

matplotlib.pyplot.scatter(projection[:,0],projection[:,1],marker='o')
matplotlib.pyplot.show()