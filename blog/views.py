from django.shortcuts import render

from drgmik.controllers.ArticleController import ArticleController
from drgmik.controllers.LineController import LineController

from drgmik.repositories.ArticleRepo import ArticleRepo
from drgmik.repositories.ImageRepo import ImageRepo

# Create your views here.


def index(request):
    aritcle_controller = ArticleController(ArticleRepo(), ImageRepo())

    result = aritcle_controller.get_all()

    if result.is_error():
        return render(request, "drgmik/404.html",
                      context={"err": result.err})

    return render(request, "blog/index.html",
                  context={"suc": result.suc})


def detail(request, id):
    line_controller = LineController()
    aritcle_controller = ArticleController(ArticleRepo(), ImageRepo())

    lines = line_controller.lines(id)
    article = aritcle_controller.get(id)

    if lines.is_error():
        return render(request, "drgmik/404.html",
                      context={"err": lines.err})

    context = {"lines_res": lines.suc} | {"art_res": article.suc}

    return render(request, "blog/detail.html",
                  context=context)
