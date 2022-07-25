from django import forms
from accounts.models import User
from .models import report, Tag, class_info, teacher, scoring, university


class ClassCreateForm(forms.ModelForm):

    university = forms.ModelChoiceField(
        label='大学名',
        queryset=university.objects.all(),
        initial=User.university,
    )

    name = forms.CharField(
        label='講義名',
        max_length=30,
        widget=forms.widgets.Input(
            attrs={'placeholder': '例）基礎演習', 'id': 'class_name'}
        )
    )

    subject_class = forms.ChoiceField(
        label='講義分類',
        choices=class_info.subject_classes,
    )

    subject_detail = forms.ChoiceField(
        label='講義詳細',
        choices=class_info.subject_details,
    )

    credit_num = forms.ChoiceField(
        label='単位数',
        choices=class_info.credit_nums,
        initial=class_info.credit_nums[1],
    )

    class Meta:
        model = class_info
        fields = ('university', 'name', 'subject_class', 'subject_detail', 'credit_num')


class TeacherCreateForm(forms.ModelForm):

    university = forms.ModelChoiceField(
        label='大学名',
        queryset=university.objects.all(),
        initial=User.university,
    )

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


class TagCreateForm(forms.ModelForm):

    university = forms.ModelChoiceField(
        label='大学名',
        queryset=university.objects.all(),
        initial=User.university,
    )

    name = forms.CharField(
        label='タグ名',
        max_length=30,
        widget=forms.widgets.Input(
            attrs={'placeholder': '例）他学部にもおすすめ'}
        )
    )

    class Meta:
        model = Tag
        fields = ('university', 'name')


class ReviewCreateForm(forms.ModelForm):

    university = forms.ModelChoiceField(
        label='大学名',
        queryset=university.objects.all(),
        initial=User.university,
    )

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

    year = forms.ChoiceField(
        label='開講年度',
        choices=years,
    )

    seasons = (
        ('前期', '前期'),
        ('後期', '後期'),
        ('1Q', '1Q'),
        ('2Q', '2Q'),
        ('3Q', '3Q'),
        ('4Q', '4Q'),
        ('不明', '不明'),
    )

    season = forms.ChoiceField(
        label='開講時期',
        choices=seasons,
    )

    class_info = forms.ModelChoiceField(
        label='講義名',
        queryset=class_info.objects.all(),
    )

    teacher = forms.ModelMultipleChoiceField(
        label='担当教員名',
        queryset=teacher.objects.all(),
    )

    frequencies = (
        ('毎回', '毎回'),
        ('ときどき', 'ときどき'),
        ('課題(テスト)で出席扱い', '課題(テスト)で出席扱い'),
        ('なし', 'なし'),
        ('不明', '不明'),
    )

    attendants_check_frequency = forms.ChoiceField(
        label='出席確認の頻度',
        choices=frequencies,
    )

    difficulties = (
        (1, '激難'),
        (2, '難'),
        (3, '普通'),
        (4, '楽'),
        (5, '激楽'),
    )

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

    quality = forms.ChoiceField(
        label='講義内容の満足度',
        choices=impressions,
    )

    scoring_method = forms.ModelMultipleChoiceField(
        label='採点方法',
        queryset=scoring.objects.all(),
    )

    opinion = forms.CharField(
        label='コメント',
        max_length=500,
        widget=forms.Textarea(
            attrs={'rows': 4}),
    )

    tag = forms.ModelMultipleChoiceField(
        label='タグ',
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    class Meta:
        model = report
        fields = ('university', 'year', 'season', 'teacher', 'class_info',
                  'attendants_check_frequency', 'scoring_method', 'credit_difficulty',
                  'quality', 'opinion', 'tag')
