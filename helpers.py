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


def save_wav(filepath: str, data: np.array, sr: int):
    """
    Save wav file.

    :param filepath: string path to location.
    :param data: numpy array generated data to be saved.
    :param sr: sample rate
    """
    if data is not None:
        wavfile.write(filepath, rate=sr, data=data)


def get_channels(data: np.array):
    """
    Extract channels from two channeled Data.

    :param data: numpy array to extract .
    :return: numpy arrays with each channel.
    """
    return [np.array(data[:, ch], dtype=np.int16) for ch in range(data.shape[1])]


def decompose(data: np.array):
    """
    Decompose an array to it`s components using ICA

    :param data: numpy array to be decomposed
    :return: numpy array of different components
    """
    ica = FastICA(max_iter=1500, random_state=0)
    out_ica = ica.fit_transform(data)
    out_ica = out_ica * (2 ** 15 - 1) / np.max(np.abs(out_ica))
    out_ica = out_ica.astype(np.int16)

    return get_channels(out_ica)


def mixer(channel1: np.array, channel2: np.array):
    """
    Mix 2 mono files into one

    :param channel1: one dimensional array
    :param channel2: one dimensional array
    :return: two dimensional arrays
    """
    return np.array([list(row) for row in zip(channel1, channel2)])


if __name__ == '__main__':
    # mix1 = load_wav("cocktail/rsm2_mA.wav")
    # mix2 = load_wav("cocktail/rsm2_mB.wav")
    mix1 = load_wav("../../Downloads/rss_mA.wav")
    mix2 = load_wav("../../Downloads/rss_mB.wav")
    rate = mix1[0]
    print("Rates are Equal", mix1[0] == mix2[0])

    print(mix1[1].shape)
    print(mix2[1].shape)

    mix = mixer(mix1[1], mix2[1])
    print(mix)

    save_wav("cocktail/cocktailparty2.wav", sr=mix2[0], data=mix)
