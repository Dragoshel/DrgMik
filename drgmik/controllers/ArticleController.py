from django.db import transaction
from django.db.utils import Error
from drgmik.repositories.ArticleRepo import ArticleRepo
from drgmik.repositories.ImageRepo import ImageRepo
from drgmik.models import Paragraph, Image
from drgmik.controllers.Result import Result, succed, fail


class ArticleController:
    def __init__(self, article_repo: ArticleRepo, image_repo: ImageRepo) -> None:
        self.article_repo = article_repo
        self.image_repo = image_repo

    def _prg_list(self, prg_data_list: list):
        prgs = []
        for prg_data in prg_data_list:
            prg = Paragraph(text=prg_data["text"], index=prg_data["index"])
            prgs.append(prg)
        return prgs

    def _img_list(self, img_data_list: list):
        imgs = []
        for img_data in img_data_list:
            img = Image(title=img_data["img"].name,
                        img=img_data["img"], index=img_data["index"])
            imgs.append(img)
        return imgs

    def create(self, title, abstract, cover_img, prg_data_list: list, img_data_list: list) -> Result:
        try:
            prgs = self._prg_list(prg_data_list)
            imgs = self._img_list(img_data_list)

            with transaction.atomic():
                cover_img_obj = self.image_repo.create(
                    title=cover_img.name, img=cover_img)

                article = self.article_repo.create(
                    title=title, abstract=abstract, cover_img=cover_img_obj)

                self.article_repo.add_prgs(article, prgs)
                self.article_repo.add_imgs(article, imgs)

            return succed(article.id)
        except Error as err:
            return fail(err)

    def get_all(self) -> Result:
        try:
            articles = self.article_repo.all()

            return succed(articles)
        except Error as err:
            return fail(err)

    def get(self, id: int) -> Result:
        try:
            article = self.article_repo.get(id)

            return succed(article)
        except Error as err:
            return fail(err)
