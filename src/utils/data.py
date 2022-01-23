from torch.utils.data import Dataset


class LyricsDataset(Dataset):
    def __init__(self, encodings, labels):
        """
        Dataset class for training.
        @param encodings: word encodings for the lines
        @param labels: whether the line belongs to a song of Ben Fero
        """
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, index):
        """
        Gets the `index`th item from the dataset.
        @param index: index of the desired item
        @return: `index`th item in the dataset
        """
        pass

    def __len__(self):
        """
        Returns the length of the dataset.
        @return: length of the dataset
        """
        return len(self.labels)
