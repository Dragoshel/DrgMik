from django.db.utils import Error
from drgmik.controllers.Result import Result, fail, succed
from drgmik.models import Article


class LineController:
    def __init__(self) -> None:
        pass

    def lines(self, art_id: int) -> Result:
        try:
            article = Article.objects.get(pk=art_id)

            paragraphs = list(article.paragraph_set.all())
            images = list(article.image_set.all())

            lines = paragraphs + images
            lines.sort(key=lambda line: line.index)

            return succed(lines)
        except Error as err:
            return fail(err)
