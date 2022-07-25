from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.university = form.cleaned_data.get('university')
        user.openingSystem = form.cleaned_data.get('openingSystem')
        user.username = form.cleaned_data.get('userName')
        user.department = form.cleaned_data.get('department')
        user.subject = form.cleaned_data.get('subject')
        user.course = form.cleaned_data.get('course')
        user.email = form.cleaned_data.get('email')
        user.major = form.cleaned_data.get('major')
        user.specialization = form.cleaned_data.get('specialization')
        user.graduationYear = form.cleaned_data.get('graduationYear')
        user.save()
