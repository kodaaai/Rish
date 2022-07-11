from django import forms
from .models import User, university
from allauth.account.forms import SignupForm, LoginForm


class CustomSignupForm(SignupForm):

    userName = forms.CharField(
        label='ユーザーネーム',
        max_length=20,
    )

    university = forms.ModelChoiceField(
        label='大学名',
        queryset=university.objects.all(),
        initial=university.objects.get(id=1),
    )

    openingSystem = forms.ChoiceField(
        label='昼間主・夜間主',
        choices=User.openingSystems,
    )

    department = forms.ChoiceField(
        label='学部',
        choices=User.departments,
        widget=forms.widgets.Select,
    )

    subject = forms.ChoiceField(
        label='学科・課程',
        widget=forms.widgets.Select,
        choices=User.subjects,
        required=False,
    )

    course = forms.ChoiceField(
        label='コース・プログラム',
        widget=forms.widgets.Select,
        choices=User.courses,
        required=False,
    )

    major = forms.ChoiceField(
        label='専攻',
        widget=forms.widgets.Select,
        choices=User.majors,
        required=False,
    )

    specialization = forms.ChoiceField(
        label='専修',
        widget=forms.widgets.Select,
        choices=User.specializations,
        required=False,
    )

    graduationYear = forms.ChoiceField(
        label='卒業見込み年',
        choices=User.graduationYears,
        widget=forms.widgets.Select,
    )
    email = forms.EmailField(initial='@eve.u-ryukyu.ac.jp', )

    class Meta:
        model = User
        fields = ('university', 'openingSystem', 'username', 'department', 'subject',
                  'course', 'major', 'specialization', 'graduationYear', 'email')

    def signup(self, request, user):
        user.university = self.cleaned_data['university']
        user.openingSystem = self.cleaned_data['openingSystem']
        user.username = self.cleaned_data['userName']
        user.department = self.cleaned_data['department']
        user.subject = self.cleaned_data['subject']
        user.course = self.cleaned_data['course']
        user.major = self.cleaned_data['major']
        user.specialization = self.cleaned_data['specialization']
        user.graduationYear = self.cleaned_data['graduationYear']
        user.email = self.cleaned_data['email']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = '琉球大学メールアドレス'

class CustomLoginForm(LoginForm):

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = '琉球大学メールアドレス'
        self.fields['login'].widget.attrs['placeholder'] = '琉球大学メールアドレス'
        self.fields['login'].widget.attrs['class'] = "form-control"
        self.fields['password'].widget.attrs['class'] = "form-control"
