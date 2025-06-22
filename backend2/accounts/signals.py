# 
from django.db.models.signals import post_save
from django.dispatch import receiver



# 
from .models import User, StudentProfile



@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.is_student:
        StudentProfile.objects.create(user=instance)







# =========
# # 
# import requests


# # 
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.core.files import File
# from django.core.files.base import ContentFile
# from django.contrib.auth.models import User

# # 
# from allauth.socialaccount.models import SocialAccount

# # 
# from .models import User

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, ** kwargs):
#     if created: 
#         try:
#             User.objects.create(
#                 user=instance
#             )

#         except Exception as e:
#             print(e)