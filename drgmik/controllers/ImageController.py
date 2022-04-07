from drgmik.models import Image


class ImageController:
    def __init__(self) -> None:
        pass

    def create(self, title, img, index=0):
        return Image(title=title, img=img, index=index)
