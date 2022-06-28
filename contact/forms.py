from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


class ContactForm(forms.Form):
    name = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(label='あなたのメールアドレス', required=True)
    category = forms.ChoiceField(
        label='お問い合わせカテゴリー',
        choices=(
            ('エラーの報告', 'エラーの報告'),
            ('レビューの削除依頼', 'レビューの削除依頼'),
            ('実装してほしい機能', '実装してほしい機能'),
            ('退会希望', '退会希望'),
            ('その他', 'その他'),
        ),
        required=True,
    )
    message = forms.CharField(label='お問い合わせ内容', max_length=2000)

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        category = self.cleaned_data['category']
        email = self.cleaned_data['email']
        from_email = '{category} <{email}>'.format(category=category, email=email)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
