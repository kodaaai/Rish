from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)

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
