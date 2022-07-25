from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model as user_model
from accounts.models import university

User = user_model()


class class_info(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名',
                                   on_delete=models.CASCADE)

    name = models.CharField('講義名', max_length=50)

    subject_classes = (
        ('', '選択してください（必須）'),
        ('共通教育', '共通教育'),
        ('人文社会学部専門教育', '人文社会学部専門教育'),
        ('国際地域創造学部専門教育', '国際地域創造学部専門教育'),
    )

    subject_class = models.CharField('講義分類', max_length=30, choices=subject_classes)

    subject_details = (
        ('', '選択してください（必須）'),
        ('健康運動系科目', '健康運動系科目'),
        ('人文系科目', '人文系科目'),
        ('社会系科目', '社会系科目'),
        ('自然系科目', '自然系科目'),
        ('総合科目', '総合科目'),
        ('琉大特色科目・地域創生科目', '琉大特色科目・地域創生科目'),
        ('キャリア関係科目', 'キャリア関係科目'),
        ('情報関係科目', '情報関係科目'),
        ('平和共生・沖縄理解科目群', '平和共生・沖縄理解科目群'),
        ('外国語科目', '外国語科目'),
        ('学部共通基盤科目', '学部共通基盤科目'),
        ('平和共生・沖縄理解基盤科目', '平和共生・沖縄理解基盤科目'),
        ('学科基盤科目', '学科基盤科目'),
        ('学科発展科目', '学科発展科目'),
        ('プログラム基盤科目', 'プログラム基盤科目'),
        ('プログラム発展科目', 'プログラム発展科目'),
        ('プログラムコア基礎科目', 'プログラムコア基礎科目'),
        ('プログラムコア発展科目', 'プログラムコア発展科目'),
        ('専門基盤力科目', '専門基盤力科目'),
        ('地域・国際基盤力科目（プログラム系科目）', '地域・国際基盤力科目（プログラム系科目）'),
        ('地域・国際基盤力科目（プログラム複合科目）', '地域・国際基盤力科目（プログラム複合科目）'),
        ('観光地域デザインプログラム専門科目（基礎科目）', '観光地域デザインプログラム専門科目（基礎科目）'),
        ('観光地域デザインプログラム専門科目（応用科目）', '観光地域デザインプログラム専門科目（応用科目）'),
        ('観光地域デザインプログラム専門科目（地域・国際実践力科目）', '観光地域デザインプログラム専門科目（地域・国際実践力科目）'),
        ('経営プログラム専門科目（基礎科目）', '経営プログラム専門科目（基礎科目）'),
        ('経営プログラム専門科目（応用科目）', '経営プログラム専門科目（応用科目）'),
        ('経営プログラム専門科目（地域・国際実践力科目）', '経営プログラム専門科目（地域・国際実践力科目）'),
        ('経済学プログラム専門科目（基礎科目）', '経済学プログラム専門科目（基礎科目）'),
        ('経済学プログラム専門科目（応用科目）', '経済学プログラム専門科目（応用科目）'),
        ('経済学プログラム専門科目（地域・国際実践力科目）', '経済学プログラム（地域・国際実践力科目）'),
        ('国際言語文化プログラム専門科目（基礎科目）', '国際言語文化プログラム専門科目（基礎科目）'),
        ('国際言語文化プログラム専門科目（応用科目）', '国際言語文化プログラム専門科目（応用科目）'),
        ('国際言語文化プログラム専門科目（地域・国際実践力科目）', '国際言語文化プログラム専門科目（地域・国際実践力科目）'),
        ('地域文化科学プログラム専門科目（基礎科目）', '地域文化科学プログラム専門科目（基礎科目）'),
        ('地域文化科学プログラム専門科目（応用科目）', '地域文化科学プログラム専門科目（応用科目）'),
        ('地域文化科学プログラム専門科目（地域・国際実践力科目）', '地域文化科学プログラム専門科目（地域・国際実践力科目）'),
        ('教職課程', '教職課程'),
    )

    subject_detail = models.CharField('講義詳細', max_length=50, choices=subject_details)

    credit_nums = (
        (1, '1単位'),
        (2, '2単位'),
        (4, '4単位'),
    )
    credit_num = models.IntegerField('単位数', choices=credit_nums)

    def __str__(self):
        return self.name


class teacher(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名', on_delete=models.CASCADE)
    name = models.CharField('講師名', max_length=30, unique=True)

    def __str__(self):
        return self.name


class scoring(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名',
                                   on_delete=models.CASCADE)
    name = models.CharField('採点方法', max_length=20, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    university = models.ForeignKey(university, verbose_name='大学名',
                                   on_delete=models.CASCADE)
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

    opinion = models.CharField('コメント', max_length=1000, null=True, blank=True)

    tag = models.ManyToManyField(Tag)

    created_at = models.DateField('投稿日', auto_now_add=True, null=True, blank=True)

    updated_at = models.DateField('更新日', auto_now=True,  null=True, blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='作成者',
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{} ( {} )'.format(self.class_info, self.university)
