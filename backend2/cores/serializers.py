# 
from django.contrib.flatpages.models import FlatPage



#
from rest_framework import serializers



# 
from accounts.serializers import *
from accounts.models import *

# from backend2.accounts.serializers import *
# from backend2.accounts.models import *



# 
from . import models




# ******************************************************************************
# ==============================================================================
# *** Category Section *** #
class CategorySectionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.CategorySection
        # fields = "__all__"
        fields = [
            "id",

            "user", 
            
            "title", 
            "description", 
            "image", 
            "image_url", 
            "is_visible", 
            
            "slug", 
            "created_at",
            "updated_at",
            
            "total_section_course",
            ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation
    
    # def __init__(self, *args, **kwargs):
    #     super(CategorySectionSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 2







# ******************************************************************************
# ==============================================================================
# *** Course *** #
class QuestionInCourseSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.QuestionInCourse
        fields = "__all__"


class FileInCourseSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.FileInCourse
        fields = "__all__"



class StudentAnswerInCourseSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.StudentAnswerInCourse
        # fields = "__all__"
        fields = [
            "id",

            "student",
            "lesson",

            "status",
            "uploaded_files",
            "degree",
            "is_visible", 

            "slug", 
            "created_at",
            "updated_at",
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        return representation



class LessonInCourseSerializer(serializers.ModelSerializer):
    files = FileInCourseSerializer(
        many=True, 
        read_only=True,
        source='file_in_course_lesson'
    )
    studentanswers = StudentAnswerInCourseSerializer(
        many=True,
        read_only=True,
        source='student_answer_in_course_lesson'
    )
    # questions = QuestionInCourseSerializer(many=True, read_only=True)

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.LessonInCourse
        # fields = "__all__"
        fields = [
            "id",

            "section",

            "type",
            
            "title",
            "description",
            "duration",

            "warning_message_user",
            "rush_watch_lessons",

            "video_file",
            "video_url",
            
            "questions",
            "questions_google_iframe",
            "questions_google_url",

            "content",
            "uploaded_files",
            
            "answer_form_pdf",
            "answer_form_pdf_url",
            
            "is_visible",
            "is_free",

            "order", 

            "slug", 
            "created_at",
            "updated_at",

            "files",
            "studentanswers",
        ]


class SectionInCourseSerializer(serializers.ModelSerializer):
    # items = LessonInCourseSerializer(many=True, read_only=True)
    lessons = LessonInCourseSerializer(
        many=True, 
        read_only=True, 
        source='section_lesson'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.SectionInCourse
        # fields = "__all__"
        fields = [
            "id",

            "course",

            "title",
            "is_visible",
            "is_free",
            "order",

            # 
            "lessons",

            "slug", 
            "created_at",
            "updated_at",

            "total_lesson",
        ]


class CourseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    # section = serializers.PrimaryKeyRelatedField(queryset=models.SectionCourse.objects.all())

    # section_course = SectionCourseSerializer(read_only=True)
    # section_course = SectionCourseSerializer(read_only=True, context={'request': None})
    
    # sections = SectionInCourseSerializer(many=True, read_only=True)
    sections = SectionInCourseSerializer(
        many=True, 
        read_only=True, 
        source='course_sections'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = models.Course
        # fields = "__all__"
        fields = [
            "id",
            
            "user",
            "section",

            "level",
            "title",
            "description",
            "image",
            "image_url",
            "duration",
            "rating",
            "reviews_count",
            "students_count",
            "language",
            "tag",
            "techs",
            "features",
            "requirements",
            "target_audience",

            "number_old_enrolled",

            "is_visible",

            # 
            "table_contents",
            "table_contents_url",

            # 
            "price",
            "discount",

            # 
            "price_like_egypt",
            "discount_like_egypt",

            "price_like_saudi",
            "discount_like_saudi",
            
            "price_like_america",
            "discount_like_america",

            # 
            "is_live",
            "start_data",
            "end_data",
            "time_at",

            # 
            "sections",

            "slug",
            "created_at",
            "updated_at",

            "teach_list",
            "total_section",
            "total_lesson",
            "total_enrolled_students",
            "course_rating",

            # 
            "price_after_discount",
            "price_after_discount_egypt",
            "price_after_discount_saudi",
            "price_after_discount_america",
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        # representation['section'] = SectionCourseSerializer(instance.section).data  # لعرض تفاصيل المستخدم
        return representation
    

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method in ['POST', 'PUT', 'PATCH']:
    #         self.Meta.depth = 0
    #     else:
    #         self.Meta.depth = 2

    # def __init__(self, *args, **kwargs):
    #         super(CourseSerializer, self).__init__(*args, **kwargs)
    #         request = self.context.get('request')
    #         if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #             print('Method is POST')
    #             self.Meta.depth = 0
    #             print(self.Meta.depth)
    #         else:
    #             print(f"Method is - {request.method}")
    #             self.Meta.depth = 2





# ******************************************************************************
# ==============================================================================
# *** Packages Course *** #
class PackageCourseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
    
    class Meta:
        model = models.PackageCourse
        # fields = "__all__"
        fields = [
            "id",
            "user",

            "title",
            "description",

            # 
            "price",
            "discount",

            # 
            "price_like_egypt",
            "discount_like_egypt",

            "price_like_saudi",
            "discount_like_saudi",
            
            "price_like_america",
            "discount_like_america",


            "courses",
            "image",
            "image_url",

            "is_admin",
            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "price_after_discount",
            
            "price_after_discount_egypt",
            "price_after_discount_saudi",
            "price_after_discount_america",
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# *** Package Course DiscountSerializer *** #
class PackageCourseDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackageCourseDiscount
        fields = ['id', 'number']






# ******************************************************************************
# ==============================================================================
# *** Questions Banks *** #
class ChoiceQuestionInBankSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    # question = serializers.PrimaryKeyRelatedField(queryset=models.SectionCourse.objects.all()) 
    # section = SectionCourseSerializer(many=True, read_only=True)

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.ChoiceQuestionInBank
        # fields = ['id', 'text', 'is_correct']
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        # representation['question'] = QuestionBankSerializer(instance.question).data  # لعرض تفاصيل المستخدم
        return representation
    

class QuestionInBankSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    question_bank = serializers.PrimaryKeyRelatedField(queryset=models.QuestionBank.objects.all()) 
    # question_bank = QuestionBankSerializer(many=True, read_only=True)

    # choices = ChoiceQuestionInBankSerializer(many=True)
    
    class Meta:
        model = models.QuestionInBank
        fields = "__all__"
        # fields = [
        #     'id', 

        #     "user",
        #     "question_bank",

        #     'text', 
        #     'image', 
        #     'image_url', 
        #     # 'display_image', 
        #     'choices',

        #     "slug", 
        #     "created_at",
        #     "updated_at",
        # ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['question_bank'] = QuestionBankSerializer(instance.question_bank).data  # لعرض تفاصيل المستخدم
        return representation
    

class QuestionInBankDetailSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    question_bank = serializers.PrimaryKeyRelatedField(queryset=models.QuestionBank.objects.all()) 

    choices = ChoiceQuestionInBankSerializer(many=True, source='choices_question_in_bank', read_only=True)
 
    
    class Meta:
        model = models.QuestionInBank
        # fields = ['id', 'text', 'image', 'image_url', 'display_image', 'choices']
        fields = "__all__"
    
    def create(self, validated_data):
        # choices_data = validated_data.pop('choices', [])
        choices_data = validated_data.pop('choices', [])
        question = models.QuestionInBank.objects.create(**validated_data)
        
        for choice_data in choices_data:
            models.ChoiceQuestionInBank.objects.create(question=question, **choice_data)
        # print("\n\n\n\n\n\n\n\n\n\n\n")
        # print("validated_data", validated_data)
        # print("question", question)
        # print("choices_data", choices_data)
        # print("\n\n\n\n\n\n\n\n\n\n\n")
        return question
    
    def update(self, instance, validated_data):
        choices_data = validated_data.pop('choices', None)
        
        # Update question fields
        # instance.text = validated_data.get('text', instance.text)
        
        # instance.image = validated_data.get('image', instance.image)
        # instance.image_url = validated_data.get('image_url', instance.image_url)
        # instance.save()

        # Update question fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update choices if provided
        if choices_data is not None:
            # Delete existing choices
            instance.choices.all().delete()
            
            # Create new choices
            for choice_data in choices_data:
                models.ChoiceQuestionInBank.objects.create(question=instance, **choice_data)
        
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['question_bank'] = QuestionBankSerializer(instance.question_bank).data  # لعرض تفاصيل المستخدم
        return representation
    



class QuestionBankSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    # section = serializers.PrimaryKeyRelatedField(queryset=models.SectionCourse.objects.all()) 

    question_count = serializers.IntegerField(read_only=True)
    section_name = serializers.CharField(source='section.name', read_only=True)
    
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.QuestionBank
        # fields = "__all__"
        fields = [
            'id',

            "user", 
            
            'title', 
            'description', 
            'image', 
            'image_url', 

            'is_visible', 

            'section_name', 
            'question_count',

            'total_question_in_bank',
            "total_student_result",
            'question_count',
            'display_image', 
            
            "slug", 
            "created_at",
            "updated_at",
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['section'] = SectionCourseSerializer(instance.section).data  # لعرض تفاصيل المستخدم
        return representation



class QuestionBankDetailSerializer(serializers.ModelSerializer):
    questions = QuestionInCourseSerializer(many=True, read_only=True)
    section_name = serializers.CharField(source='section.name', read_only=True)
    
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.QuestionBank 
        fields = "__all__"
        # fields = ['id', 'title', 'description', 'image', 'image_url', 
        #           'display_image', 'section', 'section_name', 'questions']






# ******************************************************************************
# ==============================================================================
# *** Section Course *** #
class SectionCourseSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  

    courses = CourseSerializer(
        many=True, 
        read_only=True, 
        source='section_course'  # يستخدم related_name الموجود في الموديل
    )
    questionbanks = QuestionBankSerializer(
        many=True, 
        read_only=True, 
        source='section_course_question_bank'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.SectionCourse
        # fields = "__all__"
        fields = [
            "id",

            "user",
            "courses",
            "questionbanks",
            
            "title",
            "description",
            "grade",
            "image",
            "image_url",
            "is_visible", 
            
            "slug", 
            "created_at",
            "updated_at",

            "total_course",
            "total_question_bank",
            ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم 
        return representation
    

    # def __init__(self, *args, **kwargs):
    #     super(SectionCourseSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 2







# ******************************************************************************
# ==============================================================================
# *** Coupon Course *** #
class CouponCourseSerializer(serializers.ModelSerializer):
    """Serializer for Coupon model (admin view)"""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.CouponCourse
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  *** #
# class TeacherDashboardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Teacher
#         fields=['total_teacher_course','total_teacher_chapters','total_teacher_students']


# class StudentDashboardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Student
#         fields=['enrolled_courses','favorite_courses','complete_assignments','pending_assignments']






# ******************************************************************************
# ==============================================================================
# *** Student Course Enroll *** #
class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all()) 
  
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.StudentCourseEnrollment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['course'] = CourseSerializer(instance.course).data  # لعرض تفاصيل المستخدم
        return representation
    
    # def __init__(self, *args, **kwargs):
    #     super(StudentCourseEnrollSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 2






# ******************************************************************************
# ==============================================================================
# *** Course Rating *** #
class CourseRatingSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all()) 
    
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.CourseRating
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['course'] = CourseSerializer(instance.course).data  # لعرض تفاصيل المستخدم
        return representation
    

    # def __init__(self, *args, **kwargs):
    #     super(CourseRatingSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 2




# ******************************************************************************
# ==============================================================================
# *** Student Favorite Course *** #
class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())     
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all())     

    slug = serializers.SlugField(read_only=True)
  

    class Meta:
        model = models.StudentFavoriteCourse
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['course'] = CourseSerializer(instance.course).data  # لعرض تفاصيل المستخدم
        return representation
    
    # def __init__(self, *args, **kwargs):
    #     super(StudentFavoriteCourseSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 2





# ******************************************************************************
# ==============================================================================
# *** Teacher Student Chat *** #
class TeacherStudentChatSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.TeacherStudentChat
        fields = "__all__"

    def to_representation(self,instance):
        representation = super(TeacherStudentChatSerializer, self).to_representation(instance)
        representation['msg_time'] = instance.msg_time.strftime("%Y-%m-%d %H:%M")
        return representation

    # def __init__(self, *args, **kwargs):
    #     super(TeacherStudentChatSerializer, self).__init__(*args, **kwargs)
    #     request = self.context.get('request')
    #     if request and request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH':
    #         print('Method is POST')
    #         self.Meta.depth = 0
    #         print(self.Meta.depth)
    #     else:
    #         print(f"Method is - {request.method}")
    #         self.Meta.depth = 3





# ******************************************************************************
# ==============================================================================
# *** Student Progress Course *** #
# class StudentProgressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.StudentProgressCourse
#         fields = '__all__'

# class CourseProgressSerializer(serializers.ModelSerializer):
#     progress = serializers.SerializerMethodField()
    
#     class Meta:
#         model = models.Course
#         fields = ['id', 'title', 'progress']
    
#     def get_progress(self, obj):
#         user = self.context['request'].user
#         progress = models.StudentProgressCourse.objects.filter(user=user, course=obj).aggregate(
#             avg_progress=models.Avg('progress_percentage')
#         )
#         return progress['avg_progress'] or 0


# ->
class LessonInCourseCompletionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    lesson = serializers.PrimaryKeyRelatedField(queryset=models.LessonInCourse.objects.all()) 
    
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.LessonInCourseCompletion
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['lesson'] = LessonInCourseSerializer(instance.lesson).data  # لعرض تفاصيل المستخدم
        return representation
    

class CourseProgressSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all()) 
    
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_image = serializers.SerializerMethodField()
    
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.CourseProgress
        fields = "__all__"
    
    def get_course_image(self, obj):
        request = self.context.get('request')
        if obj.course.image:
            return request.build_absolute_uri(obj.course.image.url)
        return None
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['course'] = UserSerializer(instance.course).data  # لعرض تفاصيل المستخدم
        return representation    



    

# ******************************************************************************
# ==============================================================================
# *** Student Certificate *** #
class StudentCertificateSerializer(serializers.ModelSerializer):
    # enrollment = StudentCourseEnrollSerializer(many=True, read_only=True)
    enrollment = serializers.PrimaryKeyRelatedField(queryset=models.StudentCourseEnrollment.objects.all()) 

    course_title = serializers.CharField(source='enrollment.course.title', read_only=True)
    user_name = serializers.SerializerMethodField()
    
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.StudentCertificate
        fields = "__all__"
    
    def get_user_name(self, obj):
        return obj.user.get_full_name()
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['enrollment'] = StudentCourseEnrollSerializer(instance.enrollment).data  # لعرض تفاصيل المستخدم 
        return representation   










# ******************************************************************************
# ==============================================================================
# ***   *** #

# class QuestionBankResultSerializer(serializers.Serializer): # QuizResult
#     question_id = serializers.IntegerField()
#     selected_choice_id = serializers.IntegerField(allow_null=True)



# class StudentQuestionBankResultSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
#     question_bank = QuestionBankSerializer(many=True, read_only=True)

#     class Meta:
#         model = models.StudentQuestionBankResult
#         fields = '__all__'
#         # read_only_fields = ('user', 'created_at')
    
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
#         return representation


# class StudentQuestionBankAnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.StudentQuestionBankAnswer
#         fields = '__all__'
#         extra_kwargs = {
#             'all_choices': {'write_only': True}
#         }








# ******************************************************************************
# ==============================================================================
class StudentQuestionBankResultSerializer(serializers.ModelSerializer):
    """Serializer for Student Question Bank Result (admin view)"""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    question_bank = serializers.PrimaryKeyRelatedField(queryset=models.QuestionBank.objects.all()) 

    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.StudentQuestionBankResult
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['question_bank'] = QuestionBankSerializer(instance.question_bank).data  # لعرض تفاصيل المستخدم
        return representation






# ******************************************************************************
# ==============================================================================
# *** Famous Sayings *** #
class FamousSayingsSerializer(serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  

    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.FamousSayings
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  Books  *** #
class BookSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.Book
        fields = "__all__"
       
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation
 


class CategoryBookSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    books = BookSerializer(
        many=True, 
        read_only=True, 
        source='book_category_book'  # يستخدم related_name الموجود في الموديل
    )

    class Meta:
        model = models.CategoryBook
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# ***  Proofreading Service   *** #
class ProofreadingServiceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.ProofreadingService
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation







# ******************************************************************************
# ==============================================================================
# ***   Powerpoint   *** #
class PowerpointSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.Powerpoint
        # fields = "__all__"
        fields = [
            "id",

            "user",

            "title",
            "description",
            "image",
            "image_url",
            
            # 
            "price",
            "discount",

            # 
            "price_like_egypt",
            "discount_like_egypt",

            "price_like_saudi",
            "discount_like_saudi",
            
            "price_like_america",
            "discount_like_america",
            
            "rating",
            "reviews_count",
            "students_count",

            "file_powerpoint",
            "file_powerpoint_url",

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            "total_enrolled_students",

            # 
            "price_after_discount",
            "price_after_discount_egypt",
            "price_after_discount_saudi",
            "price_after_discount_america",
        ]

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation



class StudentPowerpointEnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    powerpoint = serializers.PrimaryKeyRelatedField(queryset=models.Powerpoint.objects.all()) 
  
    slug = serializers.SlugField(read_only=True)
  
    class Meta:
        model = models.StudentPowerpointEnrollment
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['powerpoint'] = PowerpointSerializer(instance.powerpoint).data  # لعرض تفاصيل المستخدم
        return representation







# ******************************************************************************
# ==============================================================================
# ***  Powerpoint Service   *** #
class PowerpointServiceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.PowerpointService
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation



# ******************************************************************************
# ==============================================================================
# *** Quran School *** #




# ******************************************************************************
# ==============================================================================
# ***   Interview Date   *** #
class InterviewDateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.InterviewDate
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation



# ******************************************************************************
# ==============================================================================
# *** Quran School *** #

# *** Certificate Quran *** #
class CertificateQuranSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.CertificateQuran
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# *** Teacher Note *** #
class TeacherNoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.TeacherNote
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        return representation



# *** File And Library *** #
class FileAndLibrarySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.FileAndLibrary
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# *** Degree Presence And Absence *** #
class DegreePresenceAndAbsenceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    presence_and_absence = serializers.PrimaryKeyRelatedField(queryset=models.PresenceAndAbsence.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.DegreePresenceAndAbsence
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['presence_and_absence'] = PresenceAndAbsenceSerializer(instance.presence_and_absence).data  # لعرض تفاصيل المستخدم
        return representation



# ***  Presence And Absence  *** #
class PresenceAndAbsenceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # degrees_presence_and_absence = DegreePresenceAndAbsenceSerializer(
    #     many=True, 
    #     read_only=True, 
    #     source='presence_and_absence_degree_presence_and_absence'  # يستخدم related_name الموجود في الموديل
    # )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.PresenceAndAbsence
        # fields = "__all__"
        fields = [
            "id",
            "user",
            "chapter_in_quran",

            "session_type",
            "date_time",

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_degree_presence_and_absence",

            # 
            # "degrees_presence_and_absence",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# *** Degree Quran Exam *** #
class DegreeQuranExamSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    quran_exam = serializers.PrimaryKeyRelatedField(queryset=models.QuranExam.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.DegreeQuranExam
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['quran_exam'] = QuranExamSerializer(instance.quran_exam).data  # لعرض تفاصيل المستخدم
        return representation



# ***  Quran Exam  *** #
class QuranExamSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # degrees_quran_exam = DegreeQuranExamSerializer(
    #     many=True, 
    #     read_only=True, 
    #     source='quran_exam_degree_quran_exam'  # يستخدم related_name الموجود في الموديل
    # )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.QuranExam
        # fields = "__all__"
        fields = [
            "id",
            "user",
            "chapter_in_quran",

            "exam_status",
            "exam_type",

            "title",
            "date_time",

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_degree_quran_exam",

            # 
            # "degrees_quran_exam",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation







# ******************************************************************************
# ==============================================================================
# ***  Live Quran Circle  *** #
class LiveQuranCircleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.LiveQuranCircle
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation







# ******************************************************************************
# ==============================================================================
# ***  Degree Quran Circle  *** #
class DegreeQuranCircleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    quran_circle = serializers.PrimaryKeyRelatedField(queryset=models.QuranCircle.objects.all()) 

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.DegreeQuranCircle
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        representation['quran_circle'] = QuranCircleSerializer(instance.quran_circle).data  # لعرض تفاصيل المستخدم
        return representation



# ***  Quran Circle  *** #
class QuranCircleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # degrees_quran_circle = DegreeQuranCircleSerializer(
    #     many=True, 
    #     read_only=True, 
    #     source='quran_circle_degree_quran_circle'  # يستخدم related_name الموجود في الموديل
    # )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.QuranCircle
        # fields = "__all__"
        fields = [
            "id",
            "user",
            "chapter_in_quran",

            "date_time",
            "present_roses",
            "past_roses", 

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_degree_quran_circle",

            # 
            # "degrees_quran_circle",
        ]
        # read_only_fields = ('id',)  # تأكد من أن id للقراءة فقط


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation









# ******************************************************************************
# ==============================================================================
# ***  Quran Circle  *** #
class ChapterInQuranSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # 
    quran_circles = QuranCircleSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_quran_circle'  # يستخدم related_name الموجود في الموديل
    )
    # 
    live_quran_circles = LiveQuranCircleSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_live_quran_circle'  # يستخدم related_name الموجود في الموديل
    )
    # 
    quran_exams = QuranExamSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_quran_exam'  # يستخدم related_name الموجود في الموديل
    )
    # 
    presence_and_absences = PresenceAndAbsenceSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_presence_and_absence'  # يستخدم related_name الموجود في الموديل
    )
    # 
    file_and_librarys = FileAndLibrarySerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_file_and_library'  # يستخدم related_name الموجود في الموديل
    )
    # 
    teacher_notes = TeacherNoteSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_teacher_note'  # يستخدم related_name الموجود في الموديل
    )
    # 
    certificate_qurans = CertificateQuranSerializer(
        many=True, 
        read_only=True, 
        source='chapter_in_quran_certificate_quran'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.ChapterInQuran
        # fields = "__all__"
        fields = [
            "id",
            "user",

            "quran_path",
            "classroom",
            "review_level",

            "class_type",

            "title",
            "description",


            "student_enrollment", 
            "maximum_students", 

            "image", 
            "image_url", 

            "date_quran_sessions", 
            "quranic_sciences_lecture_schedule", 

            "approach_quran", 
            "quran_sciences", 

            "duration",

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_quran_circle",
            "total_degree_quran_circle",

            "total_live_quran_circle",
            
            "total_quran_exam",
            "total_degree_quran_exam",
            
            "total_presence_and_absence",
            "total_degree_presence_and_absence",
            
            "total_file_and_library",

            "total_teacher_note",
            
            "total_certificate_quran",

            "total_enrolled_students",

            # 
            "quran_circles",
            "live_quran_circles",
            "quran_exams",
            "presence_and_absences",
            "file_and_librarys",
            "teacher_notes",
            "certificate_qurans",

        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# ***  Review Level  *** #
class ReviewLevelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    chapter_in_qurans = ChapterInQuranSerializer(
        many=True, 
        read_only=True, 
        source='review_level_chapter'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.ReviewLevel
        # fields = "__all__"
        fields = [
            "id",
            "user",
            "quran_path",

            "title",
            "description",
            "duration", 

            "stamp_number", 
            "daily_auscultation", 
            "days_per_week", 
            "duration_seal", 

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_chapter_in_quran",

            # 
            "chapter_in_qurans",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  Class Room  *** #
class ClassRoomSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    chapter_in_qurans = ChapterInQuranSerializer(
        many=True, 
        read_only=True, 
        source='class_room_chapter'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.ClassRoom
        # fields = "__all__"
        fields = [
            "id",
            "user",
            "quran_path",

            "title",
            "description",

            "preservation_decision", 
            "associated_sciences", 
            "condition_acceptance",  

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_chapter_in_quran",

            # 
            "chapter_in_qurans",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  Quran Path  *** #
class QuranPathSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # 
    class_rooms = ClassRoomSerializer(
        many=True, 
        read_only=True, 
        source='quran_path_class_room'  # يستخدم related_name الموجود في الموديل
    )
    # 
    review_levels = ReviewLevelSerializer(
        many=True, 
        read_only=True, 
        source='quran_path_review_level'  # يستخدم related_name الموجود في الموديل
    )
    # 
    chapter_in_qurans = ChapterInQuranSerializer(
        many=True, 
        read_only=True, 
        source='quran_path_chapter'  # يستخدم related_name الموجود في الموديل
    )

    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.QuranPath
        # fields = "__all__"
        fields = [
            "id",
            "user",

            "name",

            "title",
            "description",

            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "total_class_room",
            "total_review_level",
            "total_chapter_in_quran",
            "total_enrolled_students",

            # 
            "class_rooms",
            "review_levels",
            "chapter_in_qurans",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  Student Quran School Enrollment  *** #
class StudentQuranSchoolEnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    
    # 
    quran_paths = QuranPathSerializer(
        # many=True, 
        # read_only=True, 
        source='quran_path',  # يستخدم related_name الموجود في الموديل
    )
    classrooms = ClassRoomSerializer(
        # many=True, 
        # read_only=True, 
        source='classroom',
    )
    review_levels = ReviewLevelSerializer(
        # many=True, 
        # read_only=True, 
        source='review_level',
    )
    chapter_in_qurans = ChapterInQuranSerializer(
        # many=True, 
        # read_only=True, 
        source='chapter_in_quran',
    )
    interview_dates = InterviewDateSerializer(
        # many=True, 
        # read_only=True, 
        source='interview_date',
    )

    # 
    # degree_quran_circle = DegreeQuranCircleSerializer()
    # degree_quran_exam = DegreeQuranExamSerializer()
    # degree_presence_and_absence = DegreePresenceAndAbsenceSerializer()
    # teacher_note = TeacherNoteSerializer()
    # certificate_quran = CertificateQuranSerializer()

    # 
    degree_quran_circle = serializers.SerializerMethodField()
    degree_quran_exam = serializers.SerializerMethodField()
    degree_presence_and_absence = serializers.SerializerMethodField()
    teacher_note = serializers.SerializerMethodField()
    certificate_quran = serializers.SerializerMethodField()


    slug = serializers.SlugField(read_only=True)
 
    class Meta:
        model = models.StudentQuranSchoolEnrollment
        # fields = "__all__"
        fields = [
            "id",
            "student",

            # 
            "quran_path",
            "classroom",
            "review_level",
            "chapter_in_quran",
            "interview_date",

            # 
            "full_name",
            "age",
            "phone_number",
            "whatsapp_number",
            "email",
            "description",
            "country",
            "about_level",

            # 
            "price",
            "total_amount",
            "remaining_amount",
            "paid_amount",

            # 
            "enrolled_time",
            "payment_id",

            # 
            "completed",
            "completion_date",
            "certificate_id",
            
            # 
            "is_visible",

            "slug",
            "created_at",
            "updated_at",

            # 
            "quran_paths",
            "classrooms",
            "review_levels",
            "chapter_in_qurans",
            "interview_dates",

            # 
            "degree_quran_circle",
            "degree_quran_exam",
            "degree_presence_and_absence",
            "teacher_note",
            "certificate_quran",
        ]

    # 1
    def get_degree_quran_circle(self, obj):
        # استرجاع شهادات الطالب المحدد فقط
        degreeQuranCircles = obj.student.degree_quran_circle_student.all()
        return DegreeQuranCircleSerializer(degreeQuranCircles , many=True).data

    # 2
    def get_degree_quran_exam(self, obj):
        # استرجاع شهادات الطالب المحدد فقط
        degreeQuranExams = obj.student.degree_quran_exam_student.all()
        return DegreeQuranExamSerializer(degreeQuranExams , many=True).data

    # 3
    def get_degree_presence_and_absence(self, obj):
        # استرجاع شهادات الطالب المحدد فقط
        degreePresenceAndAbsences = obj.student.degree_presence_and_absence_student.all()
        return DegreePresenceAndAbsenceSerializer(degreePresenceAndAbsences, many=True).data

    # 4
    def get_teacher_note(self, obj):
        # استرجاع شهادات الطالب المحدد فقط
        teacherNotes = obj.student.teacher_note_student.all()
        return TeacherNoteSerializer(teacherNotes, many=True).data

    # 5
    def get_certificate_quran(self, obj):
        # استرجاع شهادات الطالب المحدد فقط
        certificates = obj.student.certificate_quran_student.all()
        return CertificateQuranSerializer(certificates, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['student'] = UserSerializer(instance.student).data  # لعرض تفاصيل المستخدم
        return representation



























# ******************************************************************************
# ==============================================================================
# *** ContactUs *** #
class ContactUsUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.ContactUsUser
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation





# ******************************************************************************
# ==============================================================================
# *** Review *** #
class ReviewUserSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    profile = serializers.PrimaryKeyRelatedField(queryset=StudentProfile.objects.all()) 

    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.ReviewUser
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        representation['profile'] = StudentProfileSerializer(instance.profile).data  # لعرض تفاصيل المستخدم
        return representation




# ******************************************************************************
# ==============================================================================
# ***  Blogs  *** #


class YouTubeSuggestionsBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.YouTubeSuggestionsBlog
        fields = "__all__"


class ReportBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportBlog
        fields = "__all__"


class NotificationBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotificationBlog
        fields = "__all__"


class ReplyBlogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.ReplyBlog
        fields = "__all__"

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation


class CommentBlogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.CommentBlog
        fields = "__all__"
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    likes_count = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    view = serializers.IntegerField(read_only=True)
    total_comment = serializers.SerializerMethodField(read_only=True)
    teach_list = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = models.Blog
        fields = "__all__"
    
    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_total_comment(self, obj):
        return obj.total_comment()
    
    def get_teach_list(self, obj):
        return obj.teach_list()
       
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation
 

class CategoryBlogSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 

    slug = serializers.SlugField(read_only=True)
    view = serializers.IntegerField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    total_blog = serializers.SerializerMethodField(read_only=True)

    blogs = BlogSerializer(
        many=True, 
        read_only=True, 
        source='blog_category'  # يستخدم related_name الموجود في الموديل
    )

    class Meta:
        model = models.CategoryBlog
        fields = "__all__"

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_total_blog(self, obj):
        return obj.total_blog()
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user).data  # لعرض تفاصيل المستخدم
        return representation



# ******************************************************************************
# ==============================================================================
# ***  *** #