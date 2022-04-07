from ..models import Article


class ArticleRepo:
    def __init__(self) -> None:
        pass

    def create(self, title, abstract, cover_img):
        article = Article(title=title, abstract=abstract, cover_img=cover_img)
        article.save()

        self.article = article
        return article

    def add_prgs(self, article: Article, prgs: list):
        for prg in prgs:
            article.paragraph_set.add(prg, bulk=False)

    def add_imgs(self, article: Article, imgs: list):
        for img in imgs:
            article.image_set.add(img, bulk=False)

    def get(self, id: int):
        return Article.objects.get(pk=id)

    def all(self):
        return Article.objects.all()
