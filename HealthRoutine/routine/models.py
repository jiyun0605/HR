from django.db import models

class Post(models.Model):
    title = models.CharField('제목', max_length=10)
    sports_name = models.CharField('운동 이름', max_length=100)
    routine = models.IntegerField('루틴', default=0)
    sets = models.IntegerField('세트', default=0)
    created_date = models.DateTimeField('생성 날짜', auto_now_add=True)
    updated_date = models.DateTimeField('수정 날짜', auto_now_add=True)

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)