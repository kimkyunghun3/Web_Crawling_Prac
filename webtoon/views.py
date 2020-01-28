from django.http import HttpResponse
from django.shortcuts import render

from webtoon.crwaling import main_crawling
from webtoon.models import Webtoon


def main(request):
    webtoon = Webtoon.objects.all()
    context = {'webtoon': webtoon}
    return render(request, 'webtoon/home.html', context)


def crawling_main(request):
    main_crawling()
    return HttpResponse(200)
