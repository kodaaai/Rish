from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model as user_model
from accounts.models import university

# カスタムユーザーを代入
User = user_model()


class className(models.Model):
    """ 講義名 """
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('講義名', max_length=30, unique=True)

    def __str__(self):
        return self.name


class teacher(models.Model):
    """ 講師名 """
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('講師名', max_length=30, unique=True)

    def __str__(self):
        return self.name


class scoring(models.Model):
    """ 採点方法 """
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('採点方法', max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """ タグ """
    name = CharField('タグ名', max_length=20, unique=True)

    def __str__(self):
        return self.name


class report(models.Model):
    """ レビュー """

    # 大学名
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)

    # 開講年
    year = models.CharField(
        '開講年',
        max_length=10,
    )

    # 開講時期
    season = models.CharField(
        '開講時期',
        max_length=10,
    )

    subject_class = models.CharField(
        '講義分類',
        max_length=30,
    )

    # 講義名
    class_name = models.ForeignKey(
        className,
        on_delete=models.CASCADE,
        verbose_name='講義名',
    )

    # 担当教員名
    teacher = models.ManyToManyField(
        teacher,
        verbose_name='担当教員名',
    )

    # 出席確認の頻度
    attendants_check_frequency = models.CharField(
        max_length=20,
        verbose_name='出席確認の頻度',
    )

    # 採点方法
    scoring_method = models.ManyToManyField(scoring, verbose_name='採点方法')

    # 単位の取りやすさ
    credit_difficulty = models.IntegerField(verbose_name='単位の取りやすさ',)

    # 講義の質
    quality = models.IntegerField(verbose_name='講義内容の満足度',)

    # 講義に対するコメント
    opinion = models.CharField('コメント', max_length=500, blank=True, null=True)

    # タグ
    tag = models.ManyToManyField(Tag)

    # 投稿日
    created_at = models.DateField('投稿日', auto_now_add=True)

    # 更新日
    updated_at = models.DateField('更新日', auto_now=True)

    # 投稿者
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='作成者',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} ( {} )'.format(self.class_name, self.university)
