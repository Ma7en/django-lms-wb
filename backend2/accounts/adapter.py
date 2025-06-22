from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        
        # تعيين المستخدم كطالب وتفعيل الحساب
        user.is_student = True
        user.is_active = True
        user.is_verified = True

        if commit:
            user.save()
        return user
    

