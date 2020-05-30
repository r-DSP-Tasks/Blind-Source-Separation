from sklearn.decomposition import FastICA
import numpy as np
from scipy.io import wavfile


def load_wav(file_path: str):
    """
    Load wave files.

    :param file_path: file path string (Absolute/Relative).
    :return:
            data: Data values of wave file.
            rate: Sampling Rate.
    """
    try:
        rate, data = wavfile.read(file_path)
    except FileNotFoundError:
        print("File %s not found" % file_path)

    return rate, data


def get_channels(data: np.array):
    """
    Extract channels from two channeled Data.

    :param data: numpy array to extract .
    :return: numpy arrays with each channel.
    """
    return [data[:, ch] for ch in range(data.shape[1])]


def decompose(data: np.array):
    """
    Decompose an array to it`s components using ICA

    :param data: numpy array to be decomposed
    :return: numpy array of different components
    """
    ica = FastICA(random_state=0)
    out_ica = ica.fit_transform(data)
    return get_channels(out_ica)




