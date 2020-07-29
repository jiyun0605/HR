from django.db import models

class Post(models.Model):
    title = models.CharField('제목', max_length=30)
    sports_name = models.CharField('운동 이름', max_length=100)
    routine = models.CharField('루틴', max_length=50)
    sets = models.CharField('세트', max_length=50)
    created_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    updated_date = models.DateTimeField('수정 날짜', auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)