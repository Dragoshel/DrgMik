from django.forms.formsets import BaseFormSet
from django.shortcuts import render

from drgmik.controllers.ArticleController import ArticleController
from drgmik.repositories.ArticleRepo import ArticleRepo
from drgmik.repositories.ImageRepo import ImageRepo
from .forms import ArticleCreateForm, ImageCreateForm, ParagraphCreateForm
from django.forms import formset_factory


def _data_list_from_formset(formset: BaseFormSet):
    list = []
    for form in formset:
        list.append(form.cleaned_data)
    return list


def index(request):
    article_controller = ArticleController(ArticleRepo(), ImageRepo())

    ParagraphCreateFormSet = formset_factory(ParagraphCreateForm, extra=0)
    ImageCreateFormSet = formset_factory(ImageCreateForm, extra=0)

    if request.method == "POST":
        # FORM initialisation
        art_form = ArticleCreateForm(request.POST, request.FILES)
        prg_formset = ParagraphCreateFormSet(request.POST, prefix="prg")
        img_formset = ImageCreateFormSet(
            request.POST, request.FILES, prefix="img")

        # FORM validation
        if art_form.is_valid() and prg_formset.is_valid() and img_formset.is_valid():

            prg_data_list = _data_list_from_formset(prg_formset)
            img_data_list = _data_list_from_formset(img_formset)

            title = art_form.cleaned_data["title"]
            abstract = art_form.cleaned_data["abstract"]
            cover_img = art_form.cleaned_data["cover_img"]

            result = article_controller.create(
                title, abstract, cover_img, prg_data_list, img_data_list)

            if result.is_error():
                return render(request, "drgmik/404.html", context={"err": result.err})

            return render(request, "builder/confirmation.html", context={"res": result.suc})
    else:
        art_form = ArticleCreateForm()
        prg_formset = ParagraphCreateFormSet(prefix="prg")
        img_formset = ImageCreateFormSet(prefix="img")

    return render(request, "builder/index.html",
                  context={"art_form": art_form, "prg_formset": prg_formset, "img_formset": img_formset})
