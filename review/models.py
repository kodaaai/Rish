from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model as user_model
from accounts.models import university

User = user_model()


class class_info(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('講義名', max_length=30, unique=True)
    subject_class = models.CharField('講義分類', max_length=30)
    subject_detail = models.CharField('講義詳細', max_length=30)
    credit_num = models.IntegerField('単位数')

    def __str__(self):
        return self.name


class teacher(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('講師名', max_length=30, unique=True)

    def __str__(self):
        return self.name


class scoring(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('採点方法', max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = CharField('タグ名', max_length=20, unique=True)

    def __str__(self):
        return self.name


class report(models.Model):

    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)

    year = models.CharField(
        '開講年',
        max_length=10,
    )

    season = models.CharField(
        '開講時期',
        max_length=10,
    )

    class_info = models.ForeignKey(
        class_info,
        on_delete=models.CASCADE,
        verbose_name='講義名',
    )

    teacher = models.ManyToManyField(
        teacher,
        verbose_name='担当教員名',
    )

    attendants_check_frequency = models.CharField(
        max_length=20,
        verbose_name='出席確認の頻度',
    )

    scoring_method = models.ManyToManyField(scoring, verbose_name='採点方法')

    credit_difficulty = models.IntegerField('単位の取りやすさ')

    quality = models.IntegerField('講義内容の満足度')

    opinion = models.CharField('コメント', max_length=500, blank=True, null=True)

    tag = models.ManyToManyField(Tag)

    created_at = models.DateField('投稿日', auto_now_add=True)

    updated_at = models.DateField('更新日', auto_now=True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='作成者',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} ( {} )'.format(self.class_info, self.university)
