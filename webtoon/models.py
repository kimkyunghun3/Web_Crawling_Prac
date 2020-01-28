from django.db import models


class Webtoon(models.Model):
    title = models.CharField(max_length=255)
    webtoon_url = models.URLField()
    thumb_src = models.URLField()

    def __str__(self):
        return self.title


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    webtoon_url = models.URLField()
    thumb_src = models.URLField()

    def __str__(self):
        return self.title


class Cut(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    num = models.IntegerField()
    cut_src = models.URLField()
