from ..models import Image


class ImageRepo:
    def __init__(self) -> None:
        pass

    def create(self, title, img, index=0):
        img = Image(title=title, img=img, index=index)
        img.save()
        return img
