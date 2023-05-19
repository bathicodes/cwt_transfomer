import numpy as np
import matplotlib.pyplot as plt
import pywt
import pandas as pd
import matplotlib
import datetime

# setup matplotlib backend to AGG
matplotlib.use("Agg")


def cwt_transform(file_path):
    data = pd.read_csv(file_path, header=None)
    data = data.iloc[:,:-1].values

    # Define wavelet parameters
    wavelet = 'morl'  # Wavelet type
    scales = np.arange(1, 128)  # Range of scales

    electrodes = [0,1,2,3,4,5,6,7]
    image_array = []

    for i in electrodes:
        new = data[:,i]
        # Perform Continuous Wavelet Transform (CWT)
        coefficients, frequencies = pywt.cwt(new, scales, wavelet)

        image_array.append(coefficients)

    # extract individual electrode values
    e1 = image_array[0]
    e2 = image_array[1]
    e3 = image_array[2]
    e4 = image_array[3]
    e5 = image_array[4]
    e6 = image_array[5]
    e7 = image_array[6]
    e8 = image_array[7]

    col1 = np.hstack((e1, e2, e3, e4))
    col2 = np.hstack((e5, e6, e7, e8))

    combined = np.vstack((col1, col2))

    plt.figure(figsize=(10,10))

    plt.imshow(combined, cmap='prism', extent=[0, len(new), min(scales), max(scales)], aspect='auto')

    plt.axis(False)
    plt.savefig(str(datetime.datetime.now())+".png", bbox_inches='tight', pad_inches = 0)
    plt.clf()

# Add file path here
cwt_transform("<--- Add file path --->")