import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class Images(Dataset):

    def __init__(self, folder, size):
        """
        Arguments:
            folder: a string, the path to a folder with images.
            size: a tuple of integers (h, w).
        """
        super(Dataset).__init__()

        h, w = size
        assert h == w
        assert h == 256

        transform = transforms.Compose([
            transforms.Resize((h + 30, w + 30)),
            transforms.RandomCrop(size),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor()
        ])

        self.names = os.listdir(folder)
        self.transform = transform
        self.folder = folder

    def __len__(self):
        return len(self.names)

    def __getitem__(self, i):
        """
        Returns:
            a float tensor with shape [3, h, w].
            It represents a RGB image with
            pixel values in [0, 1] range.
        """
        name = self.names[i]
        path = os.path.join(self.folder, name)
        image = Image.open(path).convert('RGB')
        return self.transform(image)
