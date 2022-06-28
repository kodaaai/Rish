from django import forms
''' from accounts.models import User '''
from .models import report, Tag, className, teacher
''' scoring, university, '''

# 講義名登録


class ClassCreateForm(forms.ModelForm):

    university = forms.ChoiceField(
        label='大学名',
        choices=(
            ('基礎演習', '基礎演習'),
        )
    )
    ''' queryset=university.objects.all(),
    initial=User.university, '''

    name = forms.CharField(
        label='講義名',
        max_length=30,
        widget=forms.widgets.Input(
            attrs={'placeholder': '例）基礎演習', 'id': 'class_name'}
        )
    )

    class Meta:
        model = className
        fields = ('university', 'name')


# 先生登録
class TeacherCreateForm(forms.ModelForm):

    university = forms.ChoiceField(
        label='大学名',
        choices=(
            ('琉球大学', '琉球大学'),
        )
    )

    ''' queryset=university.objects.all(),
    initial=User.university, '''

    name = forms.CharField(
        label='教員名',
        max_length=30,
        widget=forms.widgets.Input(
            attrs={'placeholder': '例）山田太郎'}
        )
    )

    class Meta:
        model = teacher
        fields = ('university', 'name')

# タグ登録


class TagCreateForm(forms.ModelForm):

    university = forms.ChoiceField(
        label='大学名',
        choices=(
            ('#他学部にもおすすめ', '#他学部にもおすすめ'),
        )
    )
    ''' queryset=university.objects.all(),
        initial=User.university, '''

    name = forms.CharField(
        label='タグ名',
        max_length=30,
        widget=forms.widgets.Input(
            attrs={'placeholder': '例）#他学部にもおすすめ'}
        )
    )

    class Meta:
        model = Tag
        fields = ('name', 'university')


# レビュー投稿フォーム
class ReviewCreateForm(forms.ModelForm):

    university = forms.ChoiceField(
        label='大学名',
        choices=(
            ('琉球大学', '琉球大学')
        )
    )
    ''' queryset=university.objects.all(),
        initial=User.university, '''

    # 開講年・選択肢
    years = (
        ('2022年', '2022年'),
        ('2021年', '2021年'),
        ('2020年', '2020年'),
        ('2019年', '2019年'),
        ('2018年', '2018年'),
        ('2017年', '2017年'),
        ('2016年', '2016年'),
        ('不明', '不明'),
    )

    # 開講年
    year = forms.ChoiceField(
        label='開講年度',
        choices=years,
    )

    # 開講時期・選択肢
    seasons = (
        ('前期', '前期'),
        ('後期', '後期'),
        ('1Q', '1Q'),
        ('2Q', '2Q'),
        ('3Q', '3Q'),
        ('4Q', '4Q'),
        ('不明', '不明'),
    )

    # 開講時期
    season = forms.ChoiceField(
        label='開講時期',
        choices=seasons,
    )

    # 講義分類
    subject_choices = (
        ('共通教育科目（人文系）', '共通教育科目（人文系）'),
    )

    # 講義分類
    subject_class = forms.ChoiceField(
        label='講義分類',
        choices=subject_choices,
    )

    # 講義名
    class_name = forms.ChoiceField(
        label='講義名',
        choices=(
            ('基礎演習', '基礎演習')
        )
    )
    ''' queryset=className.objects.all(), '''

    # 担当教員名
    teacher = forms.MultipleChoiceField(
        label='担当教員名',
        choices=(
            ('堀勝彦', '堀勝彦')
        )
    )
    ''' queryset=teacher.objects.all(), '''

    # 出席確認の頻度・選択肢
    frequencies = (
        ('毎回', '毎回'),
        ('ときどき', 'ときどき'),
        ('課題(テスト)で出席扱い', '課題(テスト)で出席扱い'),
        ('なし', 'なし'),
        ('不明', '不明'),
    )

    # 出席確認の頻度
    attendants_check_frequency = forms.ChoiceField(
        label='出席確認の頻度',
        choices=frequencies,
    )

    # 講義難易度
    difficulties = (
        (1, '激難'),
        (2, '難'),
        (3, '普通'),
        (4, '楽'),
        (5, '激楽'),
    )

    # 単位の取りやすさ
    credit_difficulty = forms.ChoiceField(
        label='単位の取りやすさ',
        choices=difficulties,
    )

    impressions = (
        (1, '最悪'),
        (2, '悪い'),
        (3, '普通'),
        (4, '良い'),
        (5, '最良'),
    )

    # 講義の質
    quality = forms.ChoiceField(
        label='講義内容の満足度',
        choices=impressions,
    )

    # 採点方法
    scoring_method = forms.MultipleChoiceField(
        label='採点方法',
        choices=(
            ('出席', '出席'),
        )
    )
    ''' queryset=scoring.objects.all(), '''

    # コメント
    opinion = forms.CharField(
        label='コメント',
        max_length=500,
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 4}),
    )

    # タグ
    tag = forms.MultipleChoiceField(
        label='タグ',
        choices=(
            ('#他学部にもおすすめ', '#他学部にもおすすめ')
        )
    )
    ''' queryset=Tag.objects.all(), '''

    class Meta:
        model = report
        fields = ('university', 'year', 'season', 'subject_class', 'teacher', 'class_name',
                  'attendants_check_frequency', 'scoring_method', 'credit_difficulty',
                  'quality', 'opinion', 'tag')
