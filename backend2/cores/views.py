# 
import random
import requests
import uuid



# 
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.flatpages.models import FlatPage
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.core.files.base import ContentFile
from django_filters.rest_framework import DjangoFilterBackend


# 
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors



# 
from io import BytesIO
from datetime import datetime




# 
from rest_framework import generics, filters
from rest_framework import permissions
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)




# 
from accounts.serializers import *
# from backend2.accounts.serializers import *




# 
from . import models
from . import serializers





# Create your views here.



# ******************************************************************************
# ==============================================================================
# *** Pagination *** #
class StandardResultSetPagination(PageNumberPagination):
    page_size=9
    page_size_query_param='page_size'
    max_page_size = 100


class Space(generics.ListCreateAPIView):
    pass




# ******************************************************************************
# ==============================================================================
# *** Category Section *** #
class CategorySectionList(generics.ListCreateAPIView):
    queryset = models.CategorySection.objects.all()
    serializer_class = serializers.CategorySectionSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]


class CategorySectionListAdmin(generics.ListCreateAPIView):
    queryset = models.CategorySection.objects.all()
    serializer_class = serializers.CategorySectionSerializer
    permission_classes = [AllowAny]


class CategorySectionListApp(generics.ListCreateAPIView):
    queryset = models.CategorySection.objects.filter(is_visible=True)
    serializer_class = serializers.CategorySectionSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]

        

class CategorySectionResultList(generics.ListCreateAPIView):
    queryset = models.CategorySection.objects.all()
    serializer_class = serializers.CategorySectionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class CategorySectionPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategorySection.objects.all()
    serializer_class = serializers.CategorySectionSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]


class CategorySectionSearchList(generics.ListCreateAPIView):
    queryset = models.CategorySection.objects.all()
    serializer_class = serializers.CategorySectionSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                )
        return qs





# ******************************************************************************
# ==============================================================================
# *** Section Course *** #
class SectionCourseList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class SectionCourseListApp(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.filter(is_visible=True)
    serializer_class = serializers.SectionCourseSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination



class SectionCourseListAdmin(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    permission_classes = [IsAuthenticated]

        

class SectionCourseResultList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class SectionCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]



class SectionCourseSearchList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(grade__icontains=search)
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** Section Course *** #
class SectionCourseCategoriesList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_visible']
    search_fields = ['title', 'description', 'grade']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']



class SectionCourseCategoryList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.SectionCourseSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs["pk"]
        category = models.CategorySection.objects.get(id=category_id)
        return models.SectionCourse.objects.filter(category=category)




# ******************************************************************************
# ==============================================================================
# *** Course *** #
class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_live=False)
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.Course.objects.none()
        
        user = self.request.user
        if user.is_superuser:
            return models.Course.objects.filter(is_live=False)
        else:
            return models.Course.objects.filter(user=user, is_live=False)



class CourseListApp(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_visible=True, is_live=False)
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class CourseListAdmin(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_live=False)
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = StandardResultSetPagination

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.Course.objects.none()
        
        user = self.request.user
        if user.is_superuser:
            return models.Course.objects.filter(is_live=False)
        else:
            return models.Course.objects.filter(is_visible=True, is_live=False)




class CourseIsFreeListApp(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_visible=True, price=0, is_live=False)
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny]


class CourseIsLiveList(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_live=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class CourseIsLiveListApp(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_visible=True, is_live=True)
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny]


class CourseIsLiveListAdmin(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_live=True)
    serializer_class = serializers.CourseSerializer
    permission_classes = [IsAuthenticated]



class CourseResultList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True, is_live=False)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class CourseIdsList(generics.ListCreateAPIView):
    serializer_class = serializers.CourseSerializer

    def get_queryset(self):
        ids = self.request.GET.get('ids')
        if ids:
            ids = [int(id) for id in ids.split(',')]
            return models.Course.objects.filter(pk__in=ids, is_live=False)
        return models.Course.objects.filter(is_live=False)








class CoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     # هذه السطر يحل مشكلة إنشاء schema
    #     if getattr(self, 'swagger_fake_view', False):
    #         return models.Course.objects.none()
        
    #     user = self.request.user
    #     if user.is_superuser:
    #         return models.Course.objects.all()
    #     else:
    #         return models.Course.objects.filter(user=user)




class CourseIsLivePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    permission_classes = [AllowAny]




class CourseDetailAll(generics.RetrieveAPIView):
    """
    API View لعرض تفاصيل الكورس باستخدام الـ PK
    """
    queryset = models.Course.objects.all()  # كل الكورسات
    serializer_class = serializers.CourseSerializer  # السيريالايزر الذي نستخدمه
    lookup_field = 'pk'  # البحث بالـ PK (هذا هو الافتراضي، يمكن حذفه إذا أردت)



class CourseListAPI(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            qs = models.Course.objects.all().order_by('-id')[:limit]

        if 'popular' in self.request.GET:
            qs = models.Course.objects.all().order_by('-id')#[:limit]

        if 'category' in self.request.GET :
            category = self.request.GET['category']
            category = models.SectionCourse.objects.filter(id=category).first()
            qs = models.Course.objects.filter(category=category)

        if 'skill_name' in self.request.GET and 'teacher' in self.request.GET:
            skill_name = self.request.GET['skill_name']
            teacher = self.request.GET['teacher']
            teacher = models.User.objects.filter(id=teacher).first()
            qs = models.Course.objects.filter(techs__icontains=skill_name, teacher=teacher)

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring']
            qs = qs.filter(
                Q(level__icontains=search)
                |Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(duration__icontains=search)
                |Q(price__icontains=search)
                |Q(discount__icontains=search)
                |Q(rating__icontains=search)
                |Q(language__icontains=search)
                |Q(tag__icontains=search)
                |Q(techs__icontains=search)
                |Q(features__icontains=search)
                |Q(requirements__icontains=search)
                |Q(target_audience__icontains=search)
                )
        
        return qs





class CourseListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return models.Course.objects.all()
        return models.Course.objects.filter(user=user)


class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
                # هذه السطر يحل مشكلة إنشاء schema
        if getattr(self, 'swagger_fake_view', False):
            return models.Course.objects.none()
        
        user = self.request.user
        if user.is_superuser:
            return models.Course.objects.all()
        return models.Course.objects.filter(user=user)
    

class PublicCourseList(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.Course.objects.filter(is_visible=True)
        
        # # Filter by category
        # category = self.request.query_params.get('category')
        # if category:
        #     queryset = queryset.filter(category__id=category)

        # Filter by section
        section = self.request.query_params.get('section')
        if section:
            queryset = queryset.filter(section__id=section)
        
        # Filter by level
        level = self.request.query_params.get('level')
        if level:
            queryset = queryset.filter(level=level)
        
        # Search
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search))
        
        return queryset



class CoursesSearchList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(level__icontains=search)
                |Q(duration__icontains=search)
                |Q(price__icontains=search)
                |Q(duration__icontains=search)
                |Q(language__icontains=search)
                )
        return qs


class CoursesIsLiveSearchList(generics.ListCreateAPIView):
    queryset = models.Course.objects.filter(is_live=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(level__icontains=search)
                |Q(duration__icontains=search)
                |Q(price__icontains=search)
                |Q(duration__icontains=search)
                |Q(language__icontains=search)
                )
        return qs
    






class CourseSectionCourseList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.CourseSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        section_id = self.kwargs["pk"]
        section = models.SectionCourse.objects.get(id=section_id)
        return models.Course.objects.filter(section=section)




# ******************************************************************************
# ==============================================================================
# *** Section In Course *** #
class SectionInCourseList(generics.ListCreateAPIView):
    queryset = models.SectionInCourse.objects.all()
    serializer_class = serializers.SectionInCourseSerializer


class SectionInCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SectionInCourse.objects.all()
    serializer_class = serializers.SectionInCourseSerializer


class SectionInCourseListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.SectionInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return models.SectionInCourse.objects.filter(course__id=course_id)

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id')
        course = models.Course.objects.get(id=course_id)
        serializer.save(course=course)


class SectionInCourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SectionInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs.get('course_id')
        return models.SectionInCourse.objects.filter(course__id=course_id)
    








# ******************************************************************************
# ==============================================================================
# *** Lesson In Course *** #
class LessonInCourseList(generics.ListCreateAPIView):
    queryset = models.LessonInCourse.objects.all()
    serializer_class = serializers.LessonInCourseSerializer


class LessonInCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LessonInCourse.objects.all()
    serializer_class = serializers.LessonInCourseSerializer



class LessonInCourseListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.LessonInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        section_id = self.kwargs.get('section_id')
        return models.LessonInCourse.objects.filter(section__id=section_id)

    def perform_create(self, serializer):
        section_id = self.kwargs.get('section_id')
        section = models.SectionInCourse.objects.get(id=section_id)
        serializer.save(section=section)


class LessonInCourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.LessonInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        section_id = self.kwargs.get('section_id')
        return models.LessonInCourse.objects.filter(section__id=section_id)


class LessonInCourseCreateView(generics.CreateAPIView):
    queryset = models.LessonInCourse.objects.all()
    serializer_class = serializers.LessonInCourseSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        section_id = kwargs.get('section_id')
        section = models.SectionInCourse.objects.get(id=section_id)
        
        data = request.data.copy()
        data['section'] = section.id
        
        # Handle video file upload if present
        if 'video_file' in request.FILES:
            data['video_file'] = request.FILES['video_file']
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Handle files and questions if provided
        lesson = serializer.instance
        
        # Process files
        if 'uploaded_files' in request.FILES:
            files = request.FILES.getlist('uploaded_files')
            for file in files:
                models.FileInCourse.objects.create(
                    lesson=lesson,
                    name=file.name,
                    file=file,
                    size=file.size,
                    file_type=file.type
                )
        
        # Process questions (for assessments)
        if data.get('type') == 'assessment' and 'questions' in data:
            questions_data = data.get('questions', [])
            print("\n\n\n\n\n\n")
            print("questions_data", questions_data)
            print("\n\n\n\n\n\n")
            for question_data in questions_data:
                print("\n\n\n\n\n\n")
                print("question_data", question_data)
                print("\n\n\n\n\n\n")
                models.QuestionInCourse.objects.create(
                    lesson=lesson,
                    text=question_data.get('text'),
                    question_type=question_data.get('question_type'),
                    image_url=question_data.get('image_url'),
                    choices=question_data.get('choices', []),
                    correct_answer=question_data.get('correct_answer', 0)
                )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    








# ******************************************************************************
# ==============================================================================
# *** Student Answer In Course *** #
class StudentAnswerInCourseList(generics.ListCreateAPIView):
    queryset = models.StudentAnswerInCourse.objects.all()
    serializer_class = serializers.StudentAnswerInCourseSerializer


class StudentAnswerInCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentAnswerInCourse.objects.all()
    serializer_class = serializers.StudentAnswerInCourseSerializer




class FetchStudentAnswerInLesson(generics.RetrieveAPIView):
    serializer_class = serializers.StudentAnswerInCourseSerializer

    def get_object(self):
        student_id = self.kwargs['student_id']
        lesson_id = self.kwargs['lesson_id']
        student = models.User.objects.filter(id=student_id).first()
        lesson = models.LessonInCourse.objects.filter(id=lesson_id).first()
        return models.StudentAnswerInCourse.objects.filter(lesson=lesson, student=student).first()




class FetchStudentAnswerInCourseStatus(APIView): 
    def get(self, request, student_id, lesson_id):
        student = models.User.objects.filter(id=student_id).first()
        lesson = models.LessonInCourse.objects.filter(id=lesson_id).first()
        enroll_status = models.StudentAnswerInCourse.objects.filter(lesson=lesson, student=student).exists()
        return Response({'bool': enroll_status})





# ******************************************************************************
# ==============================================================================
# *** File In Course *** #
class FileInCourseList(generics.ListCreateAPIView):
    queryset = models.FileInCourse.objects.all()
    serializer_class = serializers.FileInCourseSerializer


class FileInCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FileInCourse.objects.all()
    serializer_class = serializers.FileInCourseSerializer


class FileInCourseListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.FileInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return models.FileInCourse.objects.filter(lesson__id=lesson_id)

    def perform_create(self, serializer):
        lesson_id = self.kwargs.get('lesson_id')
        lesson = models.LessonInCourse.objects.get(id=lesson_id)
        serializer.save(lesson=lesson)


class FileInCourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.FileInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return models.FileInCourse.objects.filter(lesson__id=lesson_id)
    

class FileInCourseCreateView(generics.CreateAPIView):
    queryset = models.FileInCourse.objects.all()
    serializer_class = serializers.FileInCourseSerializer

    def create(self, request, *args, **kwargs):
        lesson_id = kwargs.get('lesson_id')
        lesson = models.LessonInCourse.objects.get(id=lesson_id)
        
        # Handle multiple file uploads
        files = request.FILES.getlist('files')
        created_files = []
        
        for file in files:
            file_data = {
                'lesson': lesson.id,
                'name': file.name,
                'file': file,
                'size': file.size,
                'file_type': file.content_type,
            }
            
            serializer = self.get_serializer(data=file_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_files.append(serializer.data)
        
        return Response(created_files, status=status.HTTP_201_CREATED)








# ******************************************************************************
# ==============================================================================
# *** Question In Course *** #
class QuestionInCourseList(generics.ListCreateAPIView):
    queryset = models.QuestionInCourse.objects.all()
    serializer_class = serializers.QuestionInCourseSerializer


class QuestionInCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuestionInCourse.objects.all()
    serializer_class = serializers.QuestionInCourseSerializer


class QuestionInCourseListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.QuestionInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return models.QuestionInCourse.objects.filter(lesson__id=lesson_id)

    def perform_create(self, serializer):
        lesson_id = self.kwargs.get('lesson_id')
        lesson = models.LessonInCourse.objects.get(id=lesson_id)
        serializer.save(lesson=lesson)


class QuestionInCourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.QuestionInCourseSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return models.QuestionInCourse.objects.filter(lesson__id=lesson_id)


class QuestionCreateView(generics.CreateAPIView):
    queryset = models.QuestionInCourse.objects.all()
    serializer_class = serializers.QuestionInCourseSerializer

    def create(self, request, *args, **kwargs):
        lesson_id = kwargs.get('lesson_id')
        lesson = models.LessonInCourse.objects.get(id=lesson_id)
        
        # Handle multiple questions
        questions_data = request.data if isinstance(request.data, list) else [request.data]
        created_questions = []
        
        for question_data in questions_data:
            question_data['lesson'] = lesson.id
            
            # Handle image file upload if present
            if 'image_file' in request.FILES:
                question_data['image_file'] = request.FILES['image_file']
            
            serializer = self.get_serializer(data=question_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_questions.append(serializer.data)
        
        return Response(created_questions, status=status.HTTP_201_CREATED)
    




# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = models.Course.objects.all()
#     serializer_class = serializer.CourseSerializer

# class SectionViewSet(viewsets.ModelViewSet):
#     queryset = models.Section.objects.all()
#     serializer_class = serializer.SectionSerializer

# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = models.Item.objects.all()
#     serializer_class = serializer.ItemSerializer

# class FileViewSet(viewsets.ModelViewSet):
#     queryset = models.File.objects.all()
#     serializer_class = serializer.FileSerializer

# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = models.Question.objects.all()
#     serializer_class = serializer.QuestionSerializer








# ******************************************************************************
# ==============================================================================
# *** Packages Course *** #
class PackageCourseList(generics.ListCreateAPIView):
    queryset = models.PackageCourse.objects.all()
    serializer_class = serializers.PackageCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_student:
            return models.PackageCourse.objects.filter(user=self.request.user)
        return models.PackageCourse.objects.all()


class PackageCourseListApp(generics.ListCreateAPIView):
    queryset = models.PackageCourse.objects.filter(is_admin=True)
    serializer_class = serializers.PackageCourseSerializer
    permission_classes = [AllowAny]


class PackageCourseListAdmin(generics.ListCreateAPIView):
    queryset = models.PackageCourse.objects.all()
    serializer_class = serializers.PackageCourseSerializer
    permission_classes = [IsAuthenticated]


class PackageCourseResultList(generics.ListCreateAPIView):
    queryset = models.PackageCourse.objects.all()
    serializer_class = serializers.PackageCourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class PackageCoursePk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PackageCourse.objects.all()
    serializer_class = serializers.PackageCourseSerializer


  

class PackageCoursesSearchList(generics.ListCreateAPIView):
    queryset = models.PackageCourse.objects.all()
    serializer_class = serializers.PackageCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(price__icontains=search) 
                |Q(discount__icontains=search) 
                )
        return qs







# ******************************************************************************
# ==============================================================================
# *** Package Course Discount *** #
class PackageCourseDiscountView(generics.RetrieveUpdateAPIView):
    queryset = models.PackageCourseDiscount.objects.all()
    serializer_class = serializers.PackageCourseDiscountSerializer

    def get_object(self):
        obj, created = models.PackageCourseDiscount.objects.get_or_create(id=1)
        return obj






# ******************************************************************************
# ==============================================================================
# *** Coupon Course *** #
class CouponCourseList(generics.ListCreateAPIView):
    queryset = models.CouponCourse.objects.all()
    serializer_class = serializers.CouponCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class CouponCourseListApp(generics.ListCreateAPIView):
    queryset = models.CouponCourse.objects.filter(is_visible=True)
    serializer_class = serializers.CouponCourseSerializer
    permission_classes = [AllowAny]


class CouponCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CouponCourse.objects.all()
    serializer_class = serializers.CouponCourseSerializer
    # permission_classes = [IsAuthenticated]


class CouponCourseSearch(generics.ListCreateAPIView):
    queryset = models.CouponCourse.objects.all()
    serializer_class = serializers.CouponCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring']
            # coupon = models.CouponCourse.objects.get(name=search)
            qs = qs.filter(
                Q(name__icontains=search)
                |Q(discount__icontains=search)
                )
        return qs


class CouponCourseSearchApp(generics.ListCreateAPIView):
    queryset = models.CouponCourse.objects.all()
    serializer_class = serializers.CouponCourseSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring']
            qs = qs.filter(is_visible=True).filter(
                Q(name__iexact=search)
            )
        return qs








# ******************************************************************************
# ==============================================================================
# *** Course Payment Checkout *** #
class CourseCreateCheckoutView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        course_id = request.data.get("course_id")
        course = models.Course.objects.get(id=course_id)

        url = f"{settings.HYPERPAY_BASE_URL}/v1/checkouts"
        data = {
            'entityId': settings.HYPERPAY_ENTITY_ID,
            'amount': str(course.price),
            'currency': 'SAR',
            'paymentType': 'DB',
        }
        headers = {
            # 'Authorization': f"Bearer {settings.HYPERPAY_ACCESS_TOKEN}"
        }
        response = requests.post(url, data=data, headers=headers)
        return Response(response.json())


class CoursePaymentResultView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        resource_path = request.GET.get('resourcePath')
        course_id = request.GET.get('course_id')

        url = f"{settings.HYPERPAY_BASE_URL}{resource_path}"
        headers = {
            'Authorization': f"Bearer {settings.HYPERPAY_ACCESS_TOKEN}"
        }
        response = requests.get(url, headers=headers)
        result = response.json()

        if result.get("result", {}).get("code") == "000.100.110":  # successful payment
            models.StudentCourseEnrollment.objects.get_or_create(
                user=request.user,
                course_id=course_id,
                defaults={"payment_id": result.get("id")}
            )
            return Response({
                "status": "success", 
                "message": "Enrollment recorded"
                })
        return Response({
            "status": "failed", 
            "message": "Payment not successful"
            })





# ******************************************************************************
# ==============================================================================
# *** Student Enroll Course *** #
class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class StudentEnrollCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    # permission_classes = [IsAuthenticated]


class EnrolledStuentPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer


def fetch_enroll_status(request,student_id,course_id):
    student = models.User.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    enroll_status = models.StudentCourseEnrollment.objects.filter(course=course,student=student).count()

    if enroll_status:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})


# class FetchEnrollStatusView(generics.RetrieveAPIView):
class FetchEnrollStatusView(APIView):
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get(self, request, student_id, course_id):
        student = models.User.objects.filter(id=student_id).first()
        course = models.Course.objects.filter(id=course_id).first()
        enroll_status = models.StudentCourseEnrollment.objects.filter(course=course, student=student).exists()
        return Response({'bool': enroll_status})


# class EnrolledStuentList(generics.ListCreateAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = ""
#         if 'course_id' in self.kwargs:
#             course_id = self.kwargs['course_id']
#             # course = models.Course.objects.get(pk=course_id)
#             return models.StudentCourseEnrollment.objects.filter(course=course_id)
        
#         # elif 'teacher_id' in self.kwargs:
#         #     teacher_id = self.kwargs['teacher_id']
#         #     teacher = models.User.objects.get(pk=teacher_id)
#         #     return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
        
#         # elif 'student_id' in self.kwargs:
#         #     student_id = self.kwargs['student_id']
#         #     student = models.User.objects.get(pk=student_id)
#         #     return models.StudentCourseEnrollment.objects.filter(student=student).distinct()
        
#         # elif 'studentId' in self.kwargs:
#         #     student_id = self.kwargs['student_id']
#         #     student = models.User.objects.get(pk=student_id)
#         #     print(student.interseted_categories)
#         #     queries = [Q(techs__iendwith=value) for value in student.interseted_categories]
#         #     query = queries.pop()
#         #     for item in queries:
#         #         query |= item
#         #     qs = models.Course.objects.filter(query)

#         # return qs


#-
class EnrolledStuentCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""
        if 'course_id' in self.kwargs:
            course_id = self.kwargs['course_id']
            # course = models.Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course_id)
        

class EnrolledAllStuentList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""   
        if 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.User.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
       

class EnrolledStuentPkList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.User.objects.get(pk=student_id)
            return models.StudentCourseEnrollment.objects.filter(student=student).distinct()
        

class EnrolledRecomemdedStuentList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = serializers.StudentCourseEnrollSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""

        if 'studentId' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.User.objects.get(pk=student_id)
            print(student.interseted_categories)
            queries = [Q(techs__iendwith=value) for value in student.interseted_categories]
            query = queries.pop()
            for item in queries:
                query |= item
            qs = models.Course.objects.filter(query)

        return qs





# ******************************************************************************
# ==============================================================================
# *** Course Rating ***
class CourseRatingList(generics.ListCreateAPIView):
    queryset = models.CourseRating.objects.all()
    serializer_class = serializers.CourseRatingSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class CourseRatingPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CourseRating.objects.all()
    serializer_class = serializers.CourseRatingSerializer
    # permission_classes = [IsAuthenticated]




class CourseRatingListAPI(generics.ListCreateAPIView):
    queryset = models.CourseRating.objects.all()
    serializer_class = serializers.CourseRatingSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if 'popular' in self.request.GET:
            sql = "SELECT *, AVG(cr.rating) as avg_rating FROM main_courserating as cr INNER JOIN main_course as c ON cr.course_id=c.id GROUP BY c.id ORDER BY avg_rating desc LIMIT 3"
            return models.CourseRating.objects.raw(sql)
        
        if 'all' in self.request.GET:
            sql = "SELECT *, AVG(cr.rating) as avg_rating FROM main_courserating as cr INNER JOIN main_course as c ON cr.course_id=c.id GROUP BY c.id ORDER BY avg_rating desc"
            return models.CourseRating.objects.raw(sql)
        
        return models.CourseRating.objects.filter(course__isnull=False).order_by('-rating')




def fetch_rating_status(request,student_id,course_id):
    student = models.User.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    rating_status = models.CourseRating.objects.filter(course=course,student=student).count()

    if rating_status:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})

# class FetchRatingStatusView(generics.RetrieveAPIView):
class FetchRatingStatusView(APIView):
    # pagination_class = StandardResultSetPagination

    def get(self, request, student_id, course_id):
        student = models.User.objects.filter(id=student_id).first()
        course = models.Course.objects.filter(id=course_id).first()
        rating_status = models.CourseRating.objects.filter(course=course, student=student).exists()
        return Response({'bool': rating_status})





# ******************************************************************************
# ==============================================================================
# *** Student Favorite Course ***
class StudentFavoriteCourseList(generics.ListCreateAPIView):
    queryset = models.StudentFavoriteCourse.objects.all()
    serializer_class = serializers.StudentFavoriteCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class StudentFavoriteCoursePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentFavoriteCourse.objects.all()
    serializer_class = serializers.StudentFavoriteCourseSerializer
    # permission_classes = [IsAuthenticated]



class StudentFavoriteCourseListAPI(generics.ListCreateAPIView):
    queryset = models.StudentFavoriteCourse.objects.all()
    serializer_class = serializers.StudentFavoriteCourseSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.User.objects.get(pk=student_id)
            return models.StudentFavoriteCourse.objects.filter(student=student).distinct()


class FetchFavoriteCourseStatusView(APIView):
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get(self, request, student_id, course_id):
        student = models.User.objects.filter(id=student_id).first()
        course = models.Course.objects.filter(id=course_id).first()
        enroll_status = models.StudentFavoriteCourse.objects.filter(course=course, student=student).exists()
        return Response({'bool': enroll_status})



def remove_favorite_course(request,course_id,student_id):
    student = models.User.objects.filter(id=student_id).first()
    course = models.Course.objects.filter(id=course_id).first()
    favorite_status = models.StudentFavoriteCourse.objects.filter(course=course,student=student).delete()

    if favorite_status:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})


class RemoveFavoriteCourseView(generics.DestroyAPIView):    
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]
    
    def delete(self, request, course_id, student_id):
        student = models.User.objects.filter(id=student_id).first()
        course = models.Course.objects.filter(id=course_id).first()
        favorite_status = models.StudentFavoriteCourse.objects.filter(course=course, student=student).delete()
        return Response({'bool': favorite_status[0] > 0})






# ******************************************************************************
# ==============================================================================
# *** Teacher Student Chat ***
class TeacherStudentChatList(generics.ListCreateAPIView):
    queryset = models.TeacherStudentChat.objects.all()
    serializer_class = serializers.TeacherStudentChatSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class TeacherStudentChatPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TeacherStudentChat.objects.all()
    serializer_class = serializers.TeacherStudentChatSerializer
    # permission_classes = [IsAuthenticated]



# @csrf_exempt
# def TeacherStudentChatBot(request,teacher_id,student_id):
#     teacher = models.User.objects.get(id=teacher_id)
#     student = models.User.objects.get(id=student_id)
#     msg_to = request.POST.get('msg_to')
#     msg_from = request.POST.get('msg_from')
#     print("\n\n\n\n\n")
#     print("teacher", teacher)
#     print("student", student)
#     print("request", request)
#     print("msg_to", request.POST.get('msg_to'))
#     print("msg_from", request.POST.get('msg_from'))
#     print("\n\n\n\n\n")
#     msg_res = models.TeacherStudentChat.objects.create(
#         teacher=teacher,
#         student=student,
#         msg_to=msg_to,
#         msg_from=msg_from
#     )

#     if msg_res:
#         return JsonResponse({'bool':True,'msg':'Message sended'})
#     else:
#         return JsonResponse({'bool':False,'msg':'Message failed'})




# class TeacherStudentChatBot(generics.CreateAPIView):
#     serializer_class = serializers.TeacherStudentChatSerializer

#     def post(self, request, teacher_id, student_id):
#         teacher = models.User.objects.get(id=teacher_id)
#         student = models.User.objects.get(id=student_id)
        
#         print("\n\n\n\n\n")
#         print("teacher", teacher)
#         print("student", student)
#         print("request", request.data)
#         # print("msg_from", msg_from)
#         print("\n\n\n\n\n")
#         print("\n\n\n\n\n")

#         serializer = self.get_serializer(data=request.data)
#         print("serializer", serializer)
#         print("\n\n\n\n\n")
#         serializer.is_valid(raise_exception=True)
#         serializer.save(teacher=teacher, student=student)

#         return Response({'bool': True, 'msg': 'Message sent'}, status=status.HTTP_201_CREATED)




# class TeacherStudentChatBot(generics.CreateAPIView):
#     serializer_class = serializers.TeacherStudentChatSerializer

#     def post(self, request, teacher_id, student_id):
#         teacher = get_object_or_404(models.User, id=teacher_id)
#         student = get_object_or_404(models.User, id=student_id)

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(teacher=teacher, student=student)

#         return Response({'bool': True, 'msg': 'Message sent'}, status=status.HTTP_201_CREATED)




class TeacherStudentChatBot(generics.CreateAPIView):
    serializer_class = serializers.TeacherStudentChatSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, teacher_id, student_id):
        try:
            # Validate participants
            # teacher = get_object_or_404(models.User, id=teacher_id, user_type='teacher')
            # student = get_object_or_404(models.User, id=student_id, user_type='student')
            
            # # Check if the authenticated user is either the teacher or student
            # if request.user not in [teacher, student]:
            #     return Response(
            #         {"error": "You are not authorized to send messages in this chat"},
            #         status=status.HTTP_403_FORBIDDEN
            #     )

            # Prepare chat data
            chat_data = {
                'teacher': teacher_id,
                'student': student_id,
                'msg_to': request.data.get('msg_to'),
                'msg_from': request.data.get('msg_from'),
            }

            serializer = self.get_serializer(data=chat_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            headers = self.get_success_headers(serializer.data)
            return Response({
                "bool": True,
                "msg": "Message sent successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            return Response({
                "bool": False,
                "msg": str(e),
                "error": "Failed to send message"
            }, status=status.HTTP_400_BAD_REQUEST)
    


class TeacherStudentChatListAPI(generics.ListAPIView):
    queryset = models.TeacherStudentChat.objects.all()
    serializer_class = serializers.TeacherStudentChatSerializer

    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        student_id = self.kwargs['student_id']
        teacher = models.User.objects.get(pk=teacher_id)
        student = models.User.objects.get(pk=student_id)
        return models.TeacherStudentChat.objects.filter(teacher=teacher,student=student).exclude(msg_to='')


@csrf_exempt
def GroupTeacherStudentChatBot(request,teacher_id):
    teacher = models.User.objects.get(id=teacher_id)
    msg_to = request.POST.get('msg_to')
    msg_from = request.POST.get('msg_from')
    enrolled_list = models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
    
    for enrolled in enrolled_list:
        msg_res = models.TeacherStudentChat.objects.create(
            teacher=teacher,
            student=enrolled.student,
            msg_to=msg_to,
            msg_from=msg_from
        )

    if msg_res:
        return JsonResponse({'bool':True,'msg':'Message sended'})
    else:
        return JsonResponse({'bool':False,'msg':'Message failed'})





# ******************************************************************************
# ==============================================================================
# *** Student Progress Course *** #
class TrackLessonProgressView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, lesson_id):
        try:
            lesson = models.LessonInCourse.objects.get(id=lesson_id)
            completion, created = models.LessonInCourseCompletion.objects.get_or_create(
                user=request.user,
                lesson=lesson
            )
            
            if not completion.is_completed:
                completion.is_completed = True
                completion.completed_at = timezone.now()
                completion.save()
            
            # Update course progress
            course_progress, _ = models.CourseProgress.objects.get_or_create(
                user=request.user,
                course=lesson.section.course
            )
            course_progress.update_progress()
            
            return Response({
                'status': 'success',
                'message': 'Lesson progress updated',
                'progress': course_progress.progress_percentage
            })
        
        except models.LessonInCourse.DoesNotExist:
            return Response({'error': 'Lesson not found'}, status=404)


class GetUserProgressView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        courses_progress = models.CourseProgress.objects.filter(user=request.user)
        serializer = serializers.CourseProgressSerializer(courses_progress, many=True, context={'request': request})
        return Response(serializer.data)




# ******************************************************************************
# ==============================================================================
# *** Student Certificate ***
def student_generate_certificate(request, enrollment_id):
    enrollment = models.StudentCourseEnrollment.objects.get(id=enrollment_id)
    
    # تحقق من أن الطالب قد أكمل الكورس
    # if not enrollment.completed:
    #     return HttpResponse("Course not completed yet", status=400)
    
    # إنشاء PDF في الذاكرة
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    # إعداد الصفحة
    width, height = A4
    
    # إضافة خلفية (اختياري)
    # p.drawImage("path/to/certificate_template.jpg", 0, 0, width=width, height=height)
    
    # إضافة محتوى الشهادة
    p.setFont("Helvetica-Bold", 24)
    # p.drawCentredString(width/2, height-150, "شهادة إنجاز")
    p.drawCentredString(width/2, height-150, "Certificate of Achievement")
    
    p.setFont("Helvetica", 18)
    # p.drawCentredString(width/2, height-200, "تعلن منصة الريادة بأن")
    p.drawCentredString(width/2, height-200, "The Entrepreneurship Platform announces that")
    
    p.setFont("Helvetica-Bold", 20)
    p.drawCentredString(width/2, height-250, f"{enrollment.student.get_full_name()}")
    
    p.setFont("Helvetica", 16)
    # p.drawCentredString(width/2, height-300, "قد أكمل بنجاح دورة")
    p.drawCentredString(width/2, height-300, "I have successfully completed the course")
    
    p.setFont("Helvetica-Bold", 18)
    p.drawCentredString(width/2, height-350, f"{enrollment.course.title}")
    
    p.setFont("Helvetica", 14)
    # p.drawCentredString(width/2, height-400, f"بتاريخ: {enrollment.completion_date.strftime('%Y-%m-%d')}")
    p.drawCentredString(width/2, height-400, f"On The Date: {enrollment.completion_date.strftime('%Y-%m-%d')}")
    
    p.setFont("Helvetica", 12)
    p.drawCentredString(width/2, 100, f"Certificate Number: {enrollment.certificate_id}")
    
    # حفظ PDF
    p.showPage()
    p.save()
    
    buffer.seek(0)
    
    # إنشاء response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{enrollment.certificate_id}.pdf"'
    
    return response


class StudentGenerateCertificateView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def post(self, request, course_id):
        try:
            course = models.Course.objects.get(id=course_id)
            user = request.user
            
            # تحقق من إكمال الكورس
            # progress = CourseProgress.objects.filter(user=user, course=course).first()
            # if not progress or progress.progress_percentage < 100:
            #     return Response(
            #         {'error': 'Course not completed yet'}, 
            #         status=status.HTTP_400_BAD_REQUEST
            #     )
            
            # تحقق من وجود شهادة مسبقة
            if models.StudentCertificate.objects.filter(user=user, course=course).exists():
                certificate = models.StudentCertificate.objects.get(user=user, course=course)
                serializer = serializers.StudentCertificateSerializer(certificate)
                return Response(serializer.data)
            
            # إنشاء شهادة جديدة
            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            
            # تصميم الشهادة
            p.setFont("Helvetica-Bold", 24)
            p.drawCentredString(width/2, height-150, "Certificate of Completion")
            
            p.setFont("Helvetica", 16)
            p.drawCentredString(width/2, height-200, f"This is to certify that")
            
            p.setFont("Helvetica-Bold", 20)
            p.drawCentredString(width/2, height-240, user.get_full_name())
            
            p.setFont("Helvetica", 16)
            p.drawCentredString(width/2, height-280, f"has successfully completed the course")
            
            p.setFont("Helvetica-Bold", 18)
            p.drawCentredString(width/2, height-320, course.title)
            
            p.setFont("Helvetica", 14)
            p.drawCentredString(width/2, height-360, f"Issued on: {datetime.now().strftime('%B %d, %Y')}")
            
            p.setFont("Helvetica", 10)
            p.drawCentredString(width/2, height-400, f"Verification Code: {str(uuid.uuid4().hex)[:16].upper()}")
            
            p.showPage()
            p.save()
            
            # حفظ ملف PDF
            buffer.seek(0)
            pdf_content = ContentFile(buffer.getvalue())
            
            certificate = models.StudentCertificate(
                user=user,
                course=course,
                completion_date=datetime.now()
            )
            certificate.certificate_pdf.save(
                f"certificate_{user.id}_{course.id}.pdf", 
                pdf_content
            )
            certificate.save()
            
            # إنشاء رابط للشهادة
            certificate_url = request.build_absolute_uri(certificate.certificate_pdf.url)
            certificate.certificate_url = certificate_url
            certificate.save()
            
            serializer = serializers.StudentCertificateSerializer(certificate)
            return Response(serializer.data)
            
        except models.Course.DoesNotExist:
            return Response(
                {'error': 'Course not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )


class StudentCertificatesView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        certificates = models.StudentCertificate.objects.filter(user=request.user)
        serializer = serializers.StudentCertificateSerializer(certificates, many=True)
        return Response(serializer.data)


class StudentVerifyCertificateView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, verification_code):
        try:
            certificate = models.StudentCertificate.objects.get(verification_code=verification_code)
            serializer = serializers.StudentCertificateSerializer(certificate)
            return Response(serializer.data)
        except models.StudentCertificate.DoesNotExist:
            return Response(
                {
                    'error': 'Invalid verification code'
                }, 
                status=status.HTTP_404_NOT_FOUND
            )





# ******************************************************************************
# ==============================================================================
# # *** Question Bank ***
# # https://chat.deepseek.com/a/chat/s/213f735f-4a29-4eff-b6e7-72262c349c91
# class QuestionBankList(generics.ListCreateAPIView):
#     queryset = models.QuestionBank.objects.all()
#     serializer_class = serializers.QuestionBankSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     if self.request.user.is_student:
#     #         return models.QuestionBank.objects.filter(user=self.request.user)
#     #     return models.QuestionBank.objects.all()

#     # def get_queryset(self):
#     #     user = self.request.user
#     #     if user.is_student:
#     #         return models.QuestionBank.objects.filter(user=user)
#     #     return models.QuestionBank.objects.all()


# class QuestionBankPK(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.QuestionBank.objects.all()
#     serializer_class = serializers.QuestionBankSerializer
#     # permission_classes = [IsAuthenticated]

#     # def get_queryset(self):
#     #     # هذه السطر يحل مشكلة إنشاء schema
#     #     if getattr(self, 'swagger_fake_view', False):
#     #         return models.QuestionBank.objects.none()
        
#     #     user = self.request.user
#     #     if user.is_superuser:
#     #         return models.QuestionBank.objects.all()
#     #     else:
#     #         return models.QuestionBank.objects.filter(user=user)



# class QuestionBankViewSet(viewsets.ModelViewSet):
#     queryset = models.QuestionBank.objects.all()
    
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return serializers.QuestionBankDetailSerializer
#         return serializers.QuestionBankSerializer
    
#     @action(detail=True, methods=['get'])
#     def questions(self, request, pk=None):
#         """Get all questions for a question bank"""
#         question_bank = self.get_object()
#         questions = question_bank.questions.all()
#         serializer = serializers.QuestionBankSerializer(questions, many=True)
#         return Response(serializer.data)
    
#     @action(detail=True, methods=['get'])
#     def quiz(self, request, pk=None):
#         """Get randomized questions for quiz taking"""
#         question_bank = self.get_object()
#         questions = list(question_bank.questions.all())
        
#         # Randomize questions
#         random.shuffle(questions)
        
#         # Serialize questions but exclude is_correct from choices
#         serialized_questions = []
#         for question in questions:
#             question_data = serializers.QuestionBankSerializer(question).data
            
#             # Remove is_correct field from choices
#             for choice in question_data['choices']:
#                 if 'is_correct' in choice:
#                     del choice['is_correct']
            
#             serialized_questions.append(question_data)
        
#         return Response(serialized_questions)


# class QuestionInBankViewSet(viewsets.ModelViewSet):
#     queryset = models.QuestionInBank.objects.all()
    
#     def get_serializer_class(self):
#         if self.action in ['create', 'update', 'partial_update']:
#             return serializers.QuestionInBankDetailSerializer
#         return serializers.QuestionInBankSerializer
    
#     def get_queryset(self):
#         queryset = models.QuestionInBank.objects.all()
#         question_bank_id = self.request.query_params.get('question_bank')
        
#         if question_bank_id:
#             queryset = queryset.filter(question_bank_id=question_bank_id)
        
#         return queryset




# ******************************************************************************
# ==============================================================================
# ***    *** #

# Question Bank Views
class QuestionBankList(generics.ListCreateAPIView):
    queryset = models.QuestionBank.objects.all()
    serializer_class = serializers.QuestionBankSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     return serializers.QuestionBankSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return self.queryset
    #     return self.queryset.filter(user=self.request.user)


    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.QuestionBank.objects.none()
        
        user = self.request.user
        if user.is_superuser:
            return models.QuestionBank.objects.all()
        else:
            return models.QuestionBank.objects.filter(user=user)
        


class QuestionBankListAdmin(generics.ListCreateAPIView):
    queryset = models.QuestionBank.objects.all()
    serializer_class = serializers.QuestionBankSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return models.QuestionBank.objects.none()
        
        user = self.request.user
        if user.is_superuser:
            return models.QuestionBank.objects.all()
        else:
            return models.QuestionBank.objects.filter(user=user)


class QuestionBankListApp(generics.ListCreateAPIView):
    queryset = models.QuestionBank.objects.filter(is_visible=True)
    serializer_class = serializers.QuestionBankSerializer
    permission_classes = [AllowAny]



class QuestionBankResultList(generics.ListCreateAPIView):
    queryset = models.QuestionBank.objects.all()
    serializer_class = serializers.QuestionBankSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    


class QuestionBankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuestionBank.objects.all()
    serializer_class = serializers.QuestionBankSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     # هذه السطر يحل مشكلة إنشاء schema
    #     if getattr(self, 'swagger_fake_view', False):
    #         return models.QuestionBank.objects.none()
        
    #     user = self.request.user
    #     if user.is_superuser:
    #         return models.QuestionBank.objects.all()
    #     else:
    #         return models.QuestionBank.objects.filter(user=user)

    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return serializers.QuestionBankDetailSerializer
    #     return serializers.QuestionBankSerializer



# Custom Views for Relationships
class BankQuestionsListView(generics.ListAPIView):
    serializer_class = serializers.QuestionInBankSerializer
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        return models.QuestionInBank.objects.filter(question_bank=bank_id)











# Question Views
class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = models.QuestionInBank.objects.all()
    serializer_class = serializers.QuestionInBankDetailSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.QuestionInBankDetailSerializer
        return serializers.QuestionInBankSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        # if not self.request.user.is_staff:
        #     queryset = queryset.filter(user=self.request.user)
        
        bank_id = self.request.query_params.get('bank')
        if bank_id:
            queryset = queryset.filter(bank_id=bank_id)
        
        return queryset




# Question Views
class QuestionListCreate(generics.ListCreateAPIView):
    queryset = models.QuestionInBank.objects.all()
    serializer_class = serializers.QuestionInBankSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]



class QuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuestionInBank.objects.all()
    serializer_class = serializers.QuestionInBankSerializer    
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    # def get_serializer_class(self):
    #     if self.request.method in ['PUT', 'PATCH']:
    #         return serializers.QuestionInBankDetailSerializer
    #     return serializers.QuestionInBankSerializer




class QuestionChoicesListView(generics.ListAPIView):
    serializer_class = serializers.ChoiceQuestionInBankSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return models.ChoiceQuestionInBank.objects.filter(question=question_id)


class QuestionInBankSearchList(generics.ListCreateAPIView):
    queryset = models.QuestionInBank.objects.all()
    serializer_class = serializers.QuestionInBankSerializer
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(text__icontains=search)
                # |Q(description__icontains=search)
                )
        return qs
    



class BanksQuestionInBankSearchList(generics.ListAPIView):
    queryset = models.QuestionInBank.objects.all()
    serializer_class = serializers.QuestionInBankSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        bank_id = self.kwargs['bank_id']
        search = self.kwargs['searchstring']
        qs = qs.filter(question_bank_id=bank_id).filter(
            Q(text__icontains=search)
        )
        return qs



# Choice Views
class ChoiceListCreateView(generics.ListCreateAPIView):
    queryset = models.ChoiceQuestionInBank.objects.all()
    serializer_class = serializers.ChoiceQuestionInBankSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        # if not self.request.user.is_staff:
        #     queryset = queryset.filter(user=self.request.user)
        
        question_id = self.request.query_params.get('question')
        if question_id:
            queryset = queryset.filter(question_id=question_id)
        
        return queryset



class ChoiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ChoiceQuestionInBank.objects.all()
    serializer_class = serializers.ChoiceQuestionInBankSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrAdmin]










# ******************************************************************************
# ==============================================================================
# ***   *** #
# old code 
# class QuestionBankResultView(APIView):
#     def post(self, request, question_bank_id):
#         """Calculate quiz results"""
#         # Get the question bank
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
        
#         # Validate the request data
#         serializer = serializer.QuestionBankResultSerializer(data=request.data, many=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # Process the results
#         answers = serializer.validated_data
#         total_questions = len(answers)
#         correct_answers = 0
#         results = []
        
#         for answer in answers:
#             question_id = answer['question_id']
#             selected_choice_id = answer['selected_choice_id']
            
#             # Get the question and its correct choice
#             question = get_object_or_404(models.QuestionInBank, pk=question_id)
#             correct_choice = question.choices.filter(is_correct=True).first()
            
#             # Check if the answer is correct
#             is_correct = correct_choice.id == selected_choice_id if correct_choice else False
#             if is_correct:
#                 correct_answers += 1
            
#             # Add to results
#             results.append({
#                 'question_id': question_id,
#                 'question_text': question.text,
#                 'selected_choice_id': selected_choice_id,
#                 'correct_choice_id': correct_choice.id if correct_choice else None,
#                 'is_correct': is_correct
#             })
        
#         # Calculate percentage
#         percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
#         return Response({
#             'total_questions': total_questions,
#             'correct_answers': correct_answers,
#             'percentage': round(percentage, 2),
#             'results': results
#         })








# ******************************************************************************
# ==============================================================================
# ***   *** #

# class QuestionBankResultView(APIView):
#     def post(self, request, question_bank_id):
#         """Calculate quiz results"""
#         # Get the question bank
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
        
#         # Get all questions for this bank
#         all_questions = models.QuestionInBank.objects.filter(question_bank=question_bank_id)
        
#         # Validate the request data
#         serializer = serializers.QuestionBankResultSerializer(data=request.data, many=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         # Process the results
#         submitted_answers = {answer['question_id']: answer['selected_choice_id'] for answer in serializer.validated_data}
#         total_questions = all_questions.count()
#         correct_answers = 0
#         results = []
        
#         for question in all_questions:
#             question_id = question.id
#             selected_choice_id = submitted_answers.get(question_id)
            
#             # Get the correct choice
#             correct_choice = question.choices.filter(is_correct=True).first()
            
#             # Check if the answer is correct (only if answered)
#             is_answered = question_id in submitted_answers
#             is_correct = False
            
#             if is_answered and correct_choice:
#                 is_correct = correct_choice.id == selected_choice_id
#                 if is_correct:
#                     correct_answers += 1
            
#             # Add to results
#             results.append({
#                 'question_id': question_id,
#                 'question_text': question.text,
#                 'is_answered': is_answered,
#                 'selected_choice_id': selected_choice_id,
#                 'correct_choice_id': correct_choice.id if correct_choice else None,
#                 'is_correct': is_correct,
#                 'choices': [
#                     {
#                         'id': choice.id,
#                         'text': choice.text,
#                         'is_correct': choice.is_correct
#                     }
#                     for choice in question.choices.all()
#                 ]
#             })
        
#         # Calculate percentage
#         percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
#         return Response({
#             'total_questions': total_questions,
#             'answered_questions': len(submitted_answers),
#             'correct_answers': correct_answers,
#             'percentage': round(percentage, 2),
#             'results': results
#         })


# # 
# class StudentQuestionBankResultSaveView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def post(self, request, question_bank_id):
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
        
#         result_data = {
#             'user': request.user.id,
#             'question_bank': question_bank.id,
#             'answered_questions': request.data.get('answered_questions'),
#             'correct_answers': request.data.get('correct_answers'),
#             'percentage': request.data.get('percentage'),
#             'total_questions': request.data.get('total_questions'),
#         }
        
#         result_serializer = serializers.StudentQuestionBankResultSerializer(data=result_data)
#         if not result_serializer.is_valid():
#             return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         quiz_result = result_serializer.save()
        
#         answers_data = request.data.get('results', [])
#         for answer_data in answers_data:
#             selected_choice = next(
#                 (c for c in answer_data.get('choices', []) if c['id'] == answer_data.get('selected_choice_id')),
#                 None
#             )
#             correct_choice = next(
#                 (c for c in answer_data.get('choices', []) if c.get('is_correct', False)),
#                 None
#             )
            
#             answer_data['quiz_result'] = quiz_result.id
#             answer_data['selected_choice_text'] = selected_choice['text'] if selected_choice else None
#             answer_data['correct_choice_text'] = correct_choice['text'] if correct_choice else None
#             answer_data['all_choices'] = answer_data.get('choices', [])
            
#             answer_serializer = serializers.StudentQuestionBankAnswerSerializer(data=answer_data)
#             if answer_serializer.is_valid():
#                 answer_serializer.save()
        
#         return Response({
#             'status': 'success',
#             'result_id': quiz_result.id
#         }, status=status.HTTP_201_CREATED)
    






# ******************************************************************************
# ==============================================================================
# ***   *** #

# class QuestionBankResultView(APIView):
#     def post(self, request, question_bank_id):
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
#         questions = models.QuestionInBank.objects.filter(question_bank=question_bank)
        
#         serializer = serializers.QuestionBankResultSerializer(data=request.data, many=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         submitted_answers = {answer['question_id']: answer['selected_choice_id'] for answer in serializer.validated_data}
#         total_questions = questions.count()
#         correct_answers = 0
#         results = []
        
#         for question in questions:
#             question_id = question.id
#             selected_choice_id = submitted_answers.get(question_id)
#             is_answered = selected_choice_id is not None
#             is_correct = False
            
#             if is_answered:
#                 # تحقق مما إذا كان الخيار المحدد هو الصحيح
#                 correct_index = question.correct_answer
#                 if correct_index < len(question.choices):
#                     is_correct = selected_choice_id == correct_index
#                     if is_correct:
#                         correct_answers += 1
            
#             # إعداد بيانات النتيجة
#             result_data = {
#                 'question_id': question_id,
#                 'question_text': question.text,
#                 'is_answered': is_answered,
#                 'selected_choice_id': selected_choice_id,
#                 'correct_choice_id': question.correct_answer,
#                 'is_correct': is_correct,
#                 'all_choices': question.choices,
#             }
#             results.append(result_data)
        
#         # حساب النسبة المئوية
#         percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
#         return Response({
#             'total_questions': total_questions,
#             'answered_questions': len(submitted_answers),
#             'correct_answers': correct_answers,
#             'percentage': round(percentage, 2),
#             'results': results
#         })
    

# class StudentQuestionBankResultSaveView(APIView):
#     def post(self, request, question_bank_id):
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
#         user = request.user
        
#         # حفظ النتيجة الرئيسية
#         result_data = {
#             'user': user.id,
#             'question_bank': question_bank.id,
#             'answered_questions': request.data.get('answered_questions'),
#             'correct_answers': request.data.get('correct_answers'),
#             'percentage': request.data.get('percentage'),
#             'total_questions': request.data.get('total_questions'),
#         }
        
#         result_serializer = serializers.StudentQuestionBankResultSerializer(data=result_data)
#         if not result_serializer.is_valid():
#             return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         quiz_result = result_serializer.save()
        
#         # حفظ الإجابات التفصيلية
#         answers_data = request.data.get('results', [])
#         for answer_data in answers_data:
#             answer_data['question_bank_result'] = quiz_result.id
            
#             # الحصول على نص الخيار المحدد والصحيح
#             selected_choice_text = None
#             correct_choice_text = None
            
#             if answer_data.get('selected_choice_id') is not None:
#                 selected_choice = answer_data['all_choices'][answer_data['selected_choice_id']]
#                 selected_choice_text = selected_choice.get('text')
            
#             if answer_data.get('correct_choice_id') is not None:
#                 correct_choice = answer_data['all_choices'][answer_data['correct_choice_id']]
#                 correct_choice_text = correct_choice.get('text')
            
#             answer_data.update({
#                 'selected_choice_text': selected_choice_text,
#                 'correct_choice_text': correct_choice_text,
#             })
            
#             answer_serializer = serializers.StudentQuestionBankAnswerSerializer(data=answer_data)
#             if answer_serializer.is_valid():
#                 answer_serializer.save()
        
#         return Response({
#             'status': 'success',
#             'result_id': quiz_result.id
#         }, status=status.HTTP_201_CREATED)


# ******************************************************************************
# ==============================================================================
# 

# class QuestionBankResultView(APIView):
#     def post(self, request, question_bank_id):
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
#         questions = models.QuestionInBank.objects.filter(question_bank=question_bank)
        
#         serializer = serializers.QuestionBankResultSerializer(data=request.data, many=True)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         submitted_answers = {answer['question_id']: answer['selected_choice_id'] for answer in serializer.validated_data}
#         total_questions = questions.count()
#         correct_answers = 0
#         results = []
        
#         for question in questions:
#             question_id = question.id
#             selected_choice_id = submitted_answers.get(question_id)
#             is_answered = selected_choice_id is not None
#             is_correct = False
            
#             if is_answered:
#                 # تحقق مما إذا كان الخيار المحدد هو الصحيح
#                 correct_index = question.correct_answer
#                 if correct_index < len(question.choices):
#                     is_correct = selected_choice_id == correct_index
#                     if is_correct:
#                         correct_answers += 1
            
#             # إعداد بيانات النتيجة
#             result_data = {
#                 'question_id': question_id,
#                 'question_text': question.text,
#                 'is_answered': is_answered,
#                 'selected_choice_id': selected_choice_id,
#                 'correct_choice_id': question.correct_answer,
#                 'is_correct': is_correct,
#                 'all_choices': question.choices,
#             }
#             results.append(result_data)
        
#         # حساب النسبة المئوية
#         percentage = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        
#         return Response({
#             'total_questions': total_questions,
#             'answered_questions': len(submitted_answers),
#             'correct_answers': correct_answers,
#             'percentage': round(percentage, 2),
#             'results': results
#         })

# class StudentQuestionBankResultSaveView(APIView):
#     def post(self, request, question_bank_id):
#         question_bank = get_object_or_404(models.QuestionBank, pk=question_bank_id)
#         user = request.user
        
#         # حفظ النتيجة الرئيسية
#         result_data = {
#             'user': user.id,
#             'question_bank': question_bank.id,
#             'answered_questions': request.data.get('answered_questions'),
#             'correct_answers': request.data.get('correct_answers'),
#             'percentage': request.data.get('percentage'),
#             'total_questions': request.data.get('total_questions'),
#         }
        
#         result_serializer = serializers.StudentQuestionBankResultSerializer(data=result_data)
#         if not result_serializer.is_valid():
#             return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         quiz_result = result_serializer.save()
        
#         # حفظ الإجابات التفصيلية
#         answers_data = request.data.get('results', [])
#         for answer_data in answers_data:
#             answer_data['question_bank_result'] = quiz_result.id
            
#             # الحصول على نص الخيار المحدد والصحيح
#             selected_choice_text = None
#             correct_choice_text = None
            
#             if answer_data.get('selected_choice_id') is not None:
#                 selected_choice = answer_data['all_choices'][answer_data['selected_choice_id']]
#                 selected_choice_text = selected_choice.get('text')
            
#             if answer_data.get('correct_choice_id') is not None:
#                 correct_choice = answer_data['all_choices'][answer_data['correct_choice_id']]
#                 correct_choice_text = correct_choice.get('text')
            
#             answer_data.update({
#                 'selected_choice_text': selected_choice_text,
#                 'correct_choice_text': correct_choice_text,
#             })
            
#             answer_serializer = serializers.StudentQuestionBankAnswerSerializer(data=answer_data)
#             if answer_serializer.is_valid():
#                 answer_serializer.save()
        
#         return Response({
#             'status': 'success',
#             'result_id': quiz_result.id
#         }, status=status.HTTP_201_CREATED)








# ******************************************************************************
# ==============================================================================
# 


class StudentQuestionBankResultListApp(generics.ListCreateAPIView):
    queryset = models.StudentQuestionBankResult.objects.all()
    serializer_class = serializers.StudentQuestionBankResultSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class StudentQuestionBankResultPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentQuestionBankResult.objects.all()
    serializer_class = serializers.StudentQuestionBankResultSerializer
    permission_classes = [AllowAny]


class StudentQuestionBankResultBankList(generics.ListAPIView):
    serializer_class = serializers.StudentQuestionBankResultSerializer
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        bank_id = self.kwargs['bank_id']
        return models.StudentQuestionBankResult.objects.filter(question_bank=bank_id)


class StudentQuestionBankResultUserList(generics.ListAPIView):
    serializer_class = serializers.StudentQuestionBankResultSerializer
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return models.StudentQuestionBankResult.objects.filter(user=user_id)







# ******************************************************************************
# ==============================================================================
# ***   *** #
# 
class QuestionBankSearchList(generics.ListCreateAPIView):
    queryset = models.QuestionBank.objects.all()
    serializer_class = serializers.QuestionBankSerializer
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                )
        return qs
    






# ******************************************************************************
# ==============================================================================
# ***  ***
class QuestionBankSectionList(generics.ListCreateAPIView):
    queryset = models.SectionCourse.objects.all()
    serializer_class = serializers.QuestionBankSerializer
    # pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        section_id = self.kwargs["pk"]
        section = models.SectionCourse.objects.get(id=section_id)
        return models.QuestionBank.objects.filter(section=section)






# ******************************************************************************
# ==============================================================================
# ***  Famous Sayings  ***
class FamousSayingsList(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class FamousSayingsListApp(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer 
    permission_classes = [AllowAny]


class FamousSayingsListAdmin(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer 
    permission_classes = [IsAuthenticated]


class FamousSayingsResultList(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class FamousSayingsRandomResultList(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.filter(is_visible=True).order_by('?')[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs

class FamousSayingsPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers.FamousSayingsSerializer
    permission_classes = [AllowAny]




class FamousSayingsSearchList(generics.ListCreateAPIView):
    queryset = models.FamousSayings.objects.all()
    serializer_class = serializers. FamousSayingsSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                )
        return qs










# ******************************************************************************
# ==============================================================================
# ***  Category Book  ***
class CategoryBookList(generics.ListCreateAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class CategoryBookListApp(generics.ListCreateAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer 
    permission_classes = [AllowAny]


class CategoryBookListAdmin(generics.ListCreateAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer 
    permission_classes = [IsAuthenticated]


class CategoryBookResultList(generics.ListCreateAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class CategoryBookPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer
    permission_classes = [AllowAny]
 

class CategoryBookSearchList(generics.ListCreateAPIView):
    queryset = models.CategoryBook.objects.all()
    serializer_class = serializers.CategoryBookSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(grade__icontains=search)
                )
        return qs
 




# ******************************************************************************
# ==============================================================================
# ***  Book  ***
class BookList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class BookListApp(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [AllowAny]


class BookListAdmin(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticated]


class BookResultList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class BookPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
 
  

class BooksSearchList(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                )
        return qs





# ******************************************************************************
# ==============================================================================
# ***   Proofreading Service   ***
class ProofreadingServiceList(generics.ListCreateAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_student:
            return models.ProofreadingService.objects.filter(user=self.request.user)
        return models.ProofreadingService.objects.all()
    

class ProofreadingServiceListApp(generics.ListCreateAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer 
    permission_classes = [AllowAny]


class ProofreadingServiceListAdmin(generics.ListCreateAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer 
    permission_classes = [IsAuthenticated]


class ProofreadingServiceResultList(generics.ListCreateAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class ProofreadingServicePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer
    permission_classes = [AllowAny]
 
    
  
  

class ProofreadingServicesSearchList(generics.ListCreateAPIView):
    queryset = models.ProofreadingService.objects.all()
    serializer_class = serializers.ProofreadingServiceSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(status__icontains=search)
                |Q(type_proofreading__icontains=search) 
                |Q(number_page__icontains=search) 
                |Q(receipt_period__icontains=search) 
                |Q(phone_number__icontains=search) 
                |Q(state__icontains=search) 
                |Q(field_study__icontains=search) 
                )
        return qs

  







# ******************************************************************************
# ==============================================================================
# ***   Powerpoint   ***
class PowerpointList(generics.ListCreateAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class PowerpointListApp(generics.ListCreateAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer 
    permission_classes = [AllowAny]


class PowerpointListAdmin(generics.ListCreateAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer 
    permission_classes = [IsAuthenticated]


class PowerpointResultList(generics.ListCreateAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class PowerpointPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer
    permission_classes = [AllowAny]

    

class PowerpointsSearchList(generics.ListCreateAPIView):
    queryset = models.Powerpoint.objects.all()
    serializer_class = serializers.PowerpointSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search)
                |Q(price__icontains=search)
                |Q(discount__icontains=search) 
                )
        return qs
 


# ******************************************************************************
# ==============================================================================
# *** Student Enroll Powerpoint *** #
class StudentEnrollPowerpointList(generics.ListCreateAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class StudentEnrollPowerpointPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    # permission_classes = [IsAuthenticated]


class EnrolledStuentPowerpointPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer


def fetch_enroll_status(request,student_id,powerpoint_id):
    student = models.User.objects.filter(id=student_id).first()
    powerpoint = models.Powerpoint.objects.filter(id=powerpoint_id).first()
    enroll_status = models.StudentPowerpointEnrollment.objects.filter(powerpoint=powerpoint,student=student).count()

    if enroll_status:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})

# class FetchEnrollStatusView(generics.RetrieveAPIView):
class FetchEnrollStatusPowerpointView(APIView):
    # pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get(self, request, student_id, powerpoint_id):
        student = models.User.objects.filter(id=student_id).first()
        powerpoint = models.Powerpoint.objects.filter(id=powerpoint_id).first()
        enroll_status = models.StudentPowerpointEnrollment.objects.filter(powerpoint=powerpoint, student=student).exists()
        return Response({'bool': enroll_status})


class EnrolledStuentPowerpointList(generics.ListCreateAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""
        if 'powerpoint_id' in self.kwargs:
            powerpoint_id = self.kwargs['powerpoint_id']
            # course = models.Course.objects.get(pk=powerpoint_id)
            return models.StudentPowerpointEnrollment.objects.filter(powerpoint=powerpoint_id)
        

class EnrolledAllStuentPowerpointList(generics.ListCreateAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""   
        if 'teacher_id' in self.kwargs:
            teacher_id = self.kwargs['teacher_id']
            teacher = models.User.objects.get(pk=teacher_id)
            return models.StudentPowerpointEnrollment.objects.filter(powerpoint__teacher=teacher).distinct()
       

class EnrolledStuentPowerpointPkList(generics.ListCreateAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""
        if 'student_id' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.User.objects.get(pk=student_id)
            return models.StudentPowerpointEnrollment.objects.filter(student=student).distinct()
        

class EnrolledRecomemdedStuentPowerpointList(generics.ListCreateAPIView):
    queryset = models.StudentPowerpointEnrollment.objects.all()
    serializer_class = serializers.StudentPowerpointEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ""

        if 'studentId' in self.kwargs:
            student_id = self.kwargs['student_id']
            student = models.User.objects.get(pk=student_id)
            print(student.interseted_categories)
            queries = [Q(techs__iendwith=value) for value in student.interseted_categories]
            query = queries.pop()
            for item in queries:
                query |= item
            qs = models.Powerpoint.objects.filter(query)

        return qs







# ******************************************************************************
# ==============================================================================
# ***   Powerpoint Service   ***
class PowerpointServiceList(generics.ListCreateAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_student:
            return models.PowerpointService.objects.filter(user=self.request.user)
        return models.PowerpointService.objects.all()
    

class PowerpointServiceListApp(generics.ListCreateAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer 
    permission_classes = [AllowAny]


class PowerpointServiceListAdmin(generics.ListCreateAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer 
    permission_classes = [IsAuthenticated]


class PowerpointServiceResultList(generics.ListCreateAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


class PowerpointServicePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer
    permission_classes = [AllowAny]
 
    
  
  

class PowerpointsServicesSearchList(generics.ListCreateAPIView):
    queryset = models.PowerpointService.objects.all()
    serializer_class = serializers.PowerpointServiceSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(status__icontains=search)
                |Q(mold_shape__icontains=search) 
                |Q(description__icontains=search) 
                |Q(number_page__icontains=search) 
                |Q(receipt_period__icontains=search) 
                |Q(phone_number__icontains=search) 
                )
        return qs

  







# ******************************************************************************
# ==============================================================================
# ***  ***











# ******************************************************************************
# ==============================================================================
# *** ContactUs ***
# (List of contact us -> [GET, POST])
class ContactUsListAPIView(generics.ListCreateAPIView):
    queryset = models.ContactUsUser.objects.all()
    serializer_class = serializers.ContactUsUserSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_student:
            return models.ContactUsUser.objects.filter(user=self.request.user)
        return models.ContactUsUser.objects.all()

    # def get_queryset(self):
    #     if self.request.user:
    #         user = self.request.user
    #         if user.is_student:
    #             return models.ContactUsUser.objects.filter(user=user)
    #         else:
    #             return models.ContactUsUser.objects.all()
    
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_authenticated:
    #         if user.is_student:
    #             return models.ContactUsUser.objects.filter(user=user)
    #         else:
    #             return models.ContactUsUser.objects.all()
    #     else:
    #         return models.ContactUsUser.objects.none


# (List of contact us -> [GET, POST, PUT, DELETE])
class ContactUsPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ContactUsUser.objects.all()
    serializer_class = serializers.ContactUsUserSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        #     # هذه السطر يمنع المشكلة أثناء إنشاء schema لوثائق API
        if getattr(self, 'swagger_fake_view', False):
            return models.ContactUsUser.objects.none()
        
        if self.request.user.is_student:
            return models.ContactUsUser.objects.filter(user=self.request.user)
        return models.ContactUsUser.objects.all()

    # def get_queryset(self):
    #     # هذه السطر يمنع المشكلة أثناء إنشاء schema لوثائق API
    #     if getattr(self, 'swagger_fake_view', False):
    #         return models.ReviewUser.objects.none()
        
    #     user = self.request.user
    #     if user.is_student:
    #         return models.ContactUsUser.objects.filter(user=user)
    #     else:
    #         return models.ContactUsUser.objects.all()


# 
class ContactusUserSearchList(generics.ListCreateAPIView):
    queryset = models.ContactUsUser.objects.all()
    serializer_class = serializers.ContactUsUserSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_student:
            qs = models.ContactUsUser.objects.filter(user=self.request.user)
        else:
            qs = models.ContactUsUser.objects.all()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(full_name__icontains=search)
                |Q(email__icontains=search)
                |Q(titleofmessage__icontains=search)
                |Q(message__icontains=search)
                )
        return qs



# class ContactusUserSearchList(generics.ListCreateAPIView):
#     queryset = models.ContactUsUser.objects.all()
#     serializer_class = serializers.ContactUsUserSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         if self.request.user.is_student:
#             qs = models.ContactUsUser.objects.filter(user=self.request.user)
#         else:
#             qs = models.ContactUsUser.objects.all()

#         search = self.request.GET.get('searchstring')
#         if search:
#             qs = qs.filter(
#                 Q(full_name__icontains=search) |
#                 Q(email__icontains=search) |
#                 Q(titleofmessage__icontains=search) |
#                 Q(message__icontains=search)
#             )
#         return qs


# ******************************************************************************
# ==============================================================================
# *** Review ***
# (List of review -> [GET, POST])
class ReviewUserListAPIView(generics.ListCreateAPIView):
    queryset = models.ReviewUser.objects.all()
    serializer_class = serializers.ReviewUserSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_student:
            return models.ReviewUser.objects.filter(user=self.request.user)
        return models.ReviewUser.objects.all()

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         if self.request.user.is_student:
    #             return models.ReviewUser.objects.filter(user=self.request.user)
    #         else:
    #             return models.ReviewUser.objects.all()
    #     else:
    #         # يمكنك إرجاع queryset فارغ أو رفع استثناء إذا لم يكن المستخدم مصادقًا عليه
    #         return models.ReviewUser.objects.none()


class ReviewUserListApp(generics.ListCreateAPIView):
    queryset = models.ReviewUser.objects.all()
    serializer_class = serializers.ReviewUserSerializer
    permission_classes = [AllowAny]



class ReviewUserResultList(generics.ListCreateAPIView):
    queryset = models.ReviewUser.objects.all()
    serializer_class = serializers.ReviewUserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True,status="publication")[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs

# (List of review -> [GET, POST, PUT, DELETE])
class ReviewUserPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReviewUser.objects.all()
    serializer_class = serializers.ReviewUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # هذه السطر يمنع المشكلة أثناء إنشاء schema لوثائق API
        if getattr(self, 'swagger_fake_view', False):
            return models.ReviewUser.objects.none()
        
        user = self.request.user
        if user.is_student:
            return models.ReviewUser.objects.filter(user=user)
        else:
            return models.ReviewUser.objects.all()
        

# (List of review -> [GET])
class ReviewUserSearchList(generics.ListCreateAPIView):
    queryset = models.ReviewUser.objects.all()
    serializer_class = serializers.ReviewUserSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_student:
            qs = models.ReviewUser.objects.filter(user=self.request.user)
        else:
            qs = models.ReviewUser.objects.all()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = models.ReviewUser.objects.filter(
                Q(status__icontains=search)
                |Q(first_name__icontains=search)
                |Q(message__icontains=search)
                |Q(rating__icontains=search)
                )
        return qs






# ******************************************************************************
# ==============================================================================
# ***  ***









# ******************************************************************************
# ==============================================================================
# ***  Category Blogs  ***
class CategoryBlogListView(generics.ListCreateAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class CategoryBlogListApp(generics.ListCreateAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer 
    permission_classes = [AllowAny]


class CategoryBlogListAdmin(generics.ListCreateAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer 
    permission_classes = [IsAuthenticated]


class CategoryBlogResultList(generics.ListCreateAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer  

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class CategoryBlogPkAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer
    # permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
 
class CategoryBlogPKLike(APIView):
    def post(self, request, pk):
        try:
            category = models.CategoryBlog.objects.get(pk=pk)
            user = request.user
            
            if user in category.likes.all():
                category.likes.remove(user)
                message = "Category unliked!"
            else:
                category.likes.add(user)
                message = "Category liked!"
                models.NotificationBlog.objects.create(
                    user=category.user,
                    message=f"{user.username} liked your category: {category.title}",
                    notification_type='like_post',
                )
            
            return Response({
                "message": message, 
                "likes_count": category.likes.count()
            }, status=status.HTTP_200_OK)
            
        except models.CategoryBlog.DoesNotExist:
            return Response(
                {"error": "Category not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )



class CategoryBlogSearchList(generics.ListCreateAPIView):
    queryset = models.CategoryBlog.objects.all()
    serializer_class = serializers.CategoryBlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                )
        return qs







# ******************************************************************************
# ==============================================================================
# ***  Blogs  ***
class BlogListView(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]


class BlogListApp(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [AllowAny]


class BlogListAdmin(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogResultList(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs



class BlogPkAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
     

class BlogPKLike(APIView):
    def post(self, request, pk):
        try:
            blog = models.Blog.objects.get(pk=pk)
            user = request.user
            
            if user in blog.likes.all():
                blog.likes.remove(user)
                message = "Blog unliked!"
            else:
                blog.likes.add(user)
                message = "Blog liked!"
                models.NotificationBlog.objects.create(
                    user=blog.user,
                    message=f"{user.username} liked your blog: {blog.title}",
                    notification_type='like_post',
                    blog=blog,
                )
            
            return Response({
                "message": message, 
                "likes_count": blog.likes.count()
            }, status=status.HTTP_200_OK)
            
        except models.Blog.DoesNotExist:
            return Response(
                {"error": "Blog not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

 
  

class BlogsSearchList(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(summary__icontains=search) 
                )
        return qs








# ******************************************************************************
# ==============================================================================
# ***  Comment Blogs  ***
class CommentBlogListView(generics.ListCreateAPIView):
    queryset = models.CommentBlog.objects.all()
    serializer_class = serializers.CommentBlogSerializer

    def perform_create(self, serializer):
        comment = serializer.save(user=self.request.user)
        # Create notification for blog author
        if comment.blog.user != self.request.user:
            models.NotificationBlog.objects.create(
                user=comment.blog.user,
                message=f"{self.request.user.username} commented on your blog: {comment.blog.title}",
                notification_type='comment',
                blog=comment.blog,
                comment=comment,
                reply=None,
            )


class CommentBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CommentBlog.objects.all()
    serializer_class = serializers.CommentBlogSerializer
 


class CommentBlogPKLike(APIView):
    def post(self, request, pk):
        try:
            comment = models.CommentBlog.objects.get(pk=pk)
            user = request.user
            
            if user in comment.likes.all():
                comment.likes.remove(user)
                message = "Comment unliked!"
            else:
                comment.likes.add(user)
                message = "Comment liked!"
                models.NotificationBlog.objects.create(
                    user=comment.user,
                    message=f"{user.username} liked your comment",
                    notification_type='like_comment',
                    comment=comment,
                    blog=comment.blog,
                )
            
            return Response({
                "message": message, 
                "likes_count": comment.likes.count()
            }, status=status.HTTP_200_OK)
            
        except models.CommentBlog.DoesNotExist:
            return Response(
                {"error": "Comment not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        








# ******************************************************************************
# ==============================================================================
# ***  Reply Blogs  *** 
class ReplyBlogListView(generics.ListCreateAPIView):
    queryset = models.ReplyBlog.objects.all()
    serializer_class = serializers.ReplyBlogSerializer

    def perform_create(self, serializer):
        reply = serializer.save(user=self.request.user)
        # Create notification for comment author
        if reply.comment.user != self.request.user:
            models.NotificationBlog.objects.create(
                user=reply.comment.user,
                message=f"{self.request.user.username} replied to your comment",
                notification_type='reply',
                blog=reply.comment.blog,
                comment=reply.comment,
                reply=reply,
            )


class ReplyBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReplyBlog.objects.all()
    serializer_class = serializers.ReplyBlogSerializer


class ReplyBlogPKLike(APIView):
    def post(self, request, pk):
        try:
            reply = models.ReplyBlog.objects.get(pk=pk)
            user = request.user
            
            if user in reply.likes.all():
                reply.likes.remove(user)
                message = "Reply unliked!"
            else:
                reply.likes.add(user)
                message = "Reply liked!"
                models.NotificationBlog.objects.create(
                    user=reply.user,
                    message=f"{user.username} liked your reply",
                    notification_type='like_reply',
                    reply=reply,
                    comment=reply.comment,
                    blog=reply.comment.blog,
                )
            
            return Response({
                "message": message, 
                "likes_count": reply.likes.count()
            }, status=status.HTTP_200_OK)
            
        except models.ReplyBlog.DoesNotExist:
            return Response(
                {"error": "Reply not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        









# ******************************************************************************
# ==============================================================================
# ***  Notification Blogs  ***
class NotificationBlogListView(generics.ListCreateAPIView):
    queryset = models.NotificationBlog.objects.all()
    serializer_class = serializers.NotificationBlogSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user, is_visible=True)


class NotificationBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NotificationBlog.objects.all()
    serializer_class = serializers.NotificationBlogSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.is_read:
            instance.is_read = True
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)









# ******************************************************************************
# ==============================================================================
# ***  Report Blogs  ***
class ReportBlogListView(generics.ListCreateAPIView):
    queryset = models.ReportBlog.objects.all()
    serializer_class = serializers.ReportBlogSerializer


class ReportBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReportBlog.objects.all()
    serializer_class = serializers.ReportBlogSerializer






# ******************************************************************************
# ==============================================================================
# ***  YouTube Suggestions Blog ***
class YouTubeSuggestionsBlogList(generics.ListCreateAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]



class YouTubeSuggestionsBlogListApp(generics.ListCreateAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer
    permission_classes = [AllowAny]



class YouTubeSuggestionsBlogListAdmin(generics.ListCreateAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer
    permission_classes = [IsAuthenticated]



class YouTubeSuggestionsBlogPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer
    permission_classes = [AllowAny]



class YouTubeSuggestionsBlogResultList(generics.ListCreateAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs


  

class YouTubeSuggestionsBlogSearchList(generics.ListCreateAPIView):
    queryset = models.YouTubeSuggestionsBlog.objects.all()
    serializer_class = serializers.YouTubeSuggestionsBlogSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(video_url__icontains=search)  
                )
        return qs




# ******************************************************************************
# ==============================================================================
# ***  Blogs ***
# class CategoryBlogListView(generics.ListCreateAPIView):
#     queryset = models.CategoryBlog.objects.all()
#     serializer_class = serializers.CategoryBlogSerializer


# class CategoryBlogPkAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.CategoryBlog.objects.all()
#     serializer_class = serializers.CategoryBlogSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.view += 1  # زيادة عدد المشاهدات
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         category = models.CategoryBlog.objects.get(id=pk)
        
#         # # التحقق مما إذا كان المستخدم قد أعجب بالمقالة مسبقًا
#         if request.user in category.likes.all():
#             category.likes.remove(request.user)  # إزالة الإعجاب إذا كان موجودًا
#             print("\n\n\n\n")
#             print("->", category)
#             print("\n\n\n\n")
#             message = "category unliked!"
#         else:
#             print("\n\n\n\n")
#             print("--->",request.user)
#             print("\n\n\n\n")
#             # category.likes.add(request.user)  # إضافة إعجاب
#             # message = "category liked!"
#             # # إرسال إشعار إلى المستخدم صاحب المقالة
#             # models.Notification.objects.create(
#             #     user=category.user,  # المستخدم صاحب المقالة
#             #     message=f"{request.user.username} liked your category: {category.title}",
#             #     notification_type='like_category',
#             #     category=category,
#             # )
        
#         return Response()
#         # return Response({"message": message, "likes_count": category.likes.count()})


# class BlogListView(generics.ListCreateAPIView):
#     queryset = models.Blog.objects.all()
#     serializer_class = serializers.BlogSerializer


# class BlogPkAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Blog.objects.all()
#     serializer_class = serializers.BlogSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.views += 1  # زيادة عدد المشاهدات
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)



# class CommentBlogListView(generics.ListCreateAPIView):
#     queryset = models.CommentBlog.objects.all()
#     serializer_class = serializers.CommentBlogSerializer


# class CommentBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.CommentBlog.objects.all()
#     serializer_class = serializers.CommentBlogSerializer


# class ReplyBlogListView(generics.ListCreateAPIView):
#     queryset = models.ReplyBlog.objects.all()
#     serializer_class = serializers.ReplyBlogSerializer


# class ReplyBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.ReplyBlog.objects.all()
#     serializer_class = serializers.ReplyBlogSerializer


# class NotificationBlogListView(generics.ListCreateAPIView):
#     queryset = models.NotificationBlog.objects.all()
#     serializer_class = serializers.NotificationBlogSerializer


# class NotificationBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.NotificationBlog.objects.all()
#     serializer_class = serializers.NotificationBlogSerializer


# class ReportBlogListView(generics.ListCreateAPIView):
#     queryset = models.ReportBlog.objects.all()
#     serializer_class = serializers.ReportBlogSerializer


# class ReportBlogPKAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.ReportBlog.objects.all()
#     serializer_class = serializers.ReportBlogSerializer







# ******************************************************************************
# ==============================================================================
# *** Quran School ***




# ******************************************************************************
# ==============================================================================
# *** Interview Date *** #
class InterviewDateList(generics.ListCreateAPIView):
    queryset = models.InterviewDate.objects.all()
    serializer_class = serializers.InterviewDateSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class InterviewDateListApp(generics.ListAPIView):
    queryset = models.InterviewDate.objects.filter(is_visible=True)
    serializer_class = serializers.InterviewDateSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class InterviewDateListAdmin(generics.ListAPIView):
    queryset = models.InterviewDate.objects.all()
    serializer_class = serializers.InterviewDateSerializer
    permission_classes = [IsAuthenticated]



class InterviewDatePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.InterviewDate.objects.all()
    serializer_class = serializers.InterviewDateSerializer
    permission_classes = [AllowAny]



class InterviewDateResultList(generics.ListCreateAPIView):
    queryset = models.InterviewDate.objects.all()
    serializer_class = serializers.InterviewDateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class InterviewDateSearchList(generics.ListCreateAPIView):
    queryset = models.InterviewDate.objects.all()
    serializer_class = serializers.InterviewDateSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(schedule_time__icontains=search)
                |Q(is_visible__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** Quran Path *** #
class QuranPathList(generics.ListCreateAPIView):
    queryset = models.QuranPath.objects.all()
    serializer_class = serializers.QuranPathSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class QuranPathListApp(generics.ListAPIView):
    queryset = models.QuranPath.objects.filter(is_visible=True)
    serializer_class = serializers.QuranPathSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class QuranPathListAdmin(generics.ListAPIView):
    queryset = models.QuranPath.objects.all()
    serializer_class = serializers.QuranPathSerializer
    permission_classes = [IsAuthenticated]



class QuranPathPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuranPath.objects.all()
    serializer_class = serializers.QuranPathSerializer
    permission_classes = [AllowAny]




# class InterviewDateResultList(generics.ListCreateAPIView):
#     queryset = models.InterviewDate.objects.all()
#     serializer_class = serializers.InterviewDateSerializer

#     def get_queryset(self):
#         qs = super().get_queryset()
#         if 'result' in self.request.GET:
#             try:
#                 limit = int(self.request.GET['result'])
#                 qs = qs.order_by('-id').filter(is_visible=True)[:limit]
#             except ValueError:
#                 # Handle the case where 'result' is not an integer
#                 pass
#         return qs
    

    
# class InterviewDateSearchList(generics.ListCreateAPIView):
#     queryset = models.InterviewDate.objects.all()
#     serializer_class = serializers.InterviewDateSerializer
#     pagination_class = StandardResultSetPagination
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = super().get_queryset()

#         if 'searchstring' in self.kwargs:
#             search = self.kwargs['searchstring'] 
#             qs = qs.filter(
#                 Q(schedule_time__icontains=search)
#                 |Q(is_visible__icontains=search) 
#                 )
#         return qs





# ******************************************************************************
# ==============================================================================
# *** Class Room *** #
class ClassRoomList(generics.ListCreateAPIView):
    queryset = models.ClassRoom.objects.all()
    serializer_class = serializers.ClassRoomSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class ClassRoomListApp(generics.ListAPIView):
    queryset = models.ClassRoom.objects.filter(is_visible=True)
    serializer_class = serializers.ClassRoomSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class ClassRoomListAdmin(generics.ListAPIView):
    queryset = models.ClassRoom.objects.all()
    serializer_class = serializers.ClassRoomSerializer
    permission_classes = [IsAuthenticated]



class ClassRoomPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ClassRoom.objects.all()
    serializer_class = serializers.ClassRoomSerializer
    permission_classes = [AllowAny]




# class InterviewDateResultList(generics.ListCreateAPIView):
#     queryset = models.InterviewDate.objects.all()
#     serializer_class = serializers.InterviewDateSerializer

#     def get_queryset(self):
#         qs = super().get_queryset()
#         if 'result' in self.request.GET:
#             try:
#                 limit = int(self.request.GET['result'])
#                 qs = qs.order_by('-id').filter(is_visible=True)[:limit]
#             except ValueError:
#                 # Handle the case where 'result' is not an integer
#                 pass
#         return qs
    

    
# class InterviewDateSearchList(generics.ListCreateAPIView):
#     queryset = models.InterviewDate.objects.all()
#     serializer_class = serializers.InterviewDateSerializer
#     pagination_class = StandardResultSetPagination
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = super().get_queryset()

#         if 'searchstring' in self.kwargs:
#             search = self.kwargs['searchstring'] 
#             qs = qs.filter(
#                 Q(schedule_time__icontains=search)
#                 |Q(is_visible__icontains=search) 
#                 )
#         return qs






# ******************************************************************************
# ==============================================================================
# *** Review Level *** #
class ReviewLevelList(generics.ListCreateAPIView):
    queryset = models.ReviewLevel.objects.all()
    serializer_class = serializers.ReviewLevelSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class ReviewLevelListApp(generics.ListAPIView):
    queryset = models.ReviewLevel.objects.filter(is_visible=True)
    serializer_class = serializers.ReviewLevelSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class ReviewLevelListAdmin(generics.ListAPIView):
    queryset = models.ReviewLevel.objects.all()
    serializer_class = serializers.ReviewLevelSerializer
    permission_classes = [IsAuthenticated]



class ReviewLevelPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReviewLevel.objects.all()
    serializer_class = serializers.ReviewLevelSerializer
    permission_classes = [AllowAny]




class ReviewLevelResultList(generics.ListCreateAPIView):
    queryset = models.ReviewLevel.objects.all()
    serializer_class = serializers.ReviewLevelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class ReviewLevelSearchList(generics.ListCreateAPIView):
    queryset = models.ReviewLevel.objects.all()
    serializer_class = serializers.ReviewLevelSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(duration__icontains=search) 
                |Q(stamp_number__icontains=search) 
                |Q(daily_auscultation__icontains=search) 
                |Q(days_per_week__icontains=search) 
                |Q(duration_seal__icontains=search) 
                )
        return qs






# ******************************************************************************
# ==============================================================================
# *** Chapter In Quran *** #
class ChapterInQuranList(generics.ListCreateAPIView):
    queryset = models.ChapterInQuran.objects.all()
    serializer_class = serializers.ChapterInQuranSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class ChapterInQuranListApp(generics.ListAPIView):
    queryset = models.ChapterInQuran.objects.filter(is_visible=True)
    serializer_class = serializers.ChapterInQuranSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class ChapterInQuranListAdmin(generics.ListAPIView):
    queryset = models.ChapterInQuran.objects.all()
    serializer_class = serializers.ChapterInQuranSerializer
    permission_classes = [IsAuthenticated]



class ChapterInQuranPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ChapterInQuran.objects.all()
    serializer_class = serializers.ChapterInQuranSerializer
    permission_classes = [AllowAny]




class ChapterInQuranResultList(generics.ListCreateAPIView):
    queryset = models.ChapterInQuran.objects.all()
    serializer_class = serializers.ChapterInQuranSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class ChapterInQuranSearchList(generics.ListCreateAPIView):
    queryset = models.ChapterInQuran.objects.all()
    serializer_class = serializers.ChapterInQuranSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(class_type__icontains=search)
                |Q(title__icontains=search) 
                |Q(description__icontains=search) 
                |Q(maximum_students__icontains=search) 
                |Q(image__icontains=search) 
                |Q(image_url__icontains=search) 
                |Q(date_quran_sessions__icontains=search) 
                |Q(quranic_sciences_lecture_schedule__icontains=search) 
                |Q(approach_quran__icontains=search) 
                |Q(quran_sciences__icontains=search) 
                )
        return qs






# ******************************************************************************
# ==============================================================================
# *** Quran Circle *** #
class QuranCircleList(generics.ListCreateAPIView):
    queryset = models.QuranCircle.objects.all()
    serializer_class = serializers.QuranCircleSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class QuranCircleListApp(generics.ListAPIView):
    queryset = models.QuranCircle.objects.filter(is_visible=True)
    serializer_class = serializers.QuranCircleSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class QuranCircleListAdmin(generics.ListAPIView):
    queryset = models.QuranCircle.objects.all()
    serializer_class = serializers.QuranCircleSerializer
    permission_classes = [IsAuthenticated]



class QuranCirclePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuranCircle.objects.all()
    serializer_class = serializers.QuranCircleSerializer
    permission_classes = [AllowAny]




class QuranCircleResultList(generics.ListCreateAPIView):
    queryset = models.QuranCircle.objects.all()
    serializer_class = serializers.QuranCircleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class QuranCircleSearchList(generics.ListCreateAPIView):
    queryset = models.QuranCircle.objects.all()
    serializer_class = serializers.QuranCircleSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(date__icontains=search)
                |Q(present_roses__icontains=search) 
                |Q(past_roses__icontains=search) 
                )
        return qs






# ******************************************************************************
# ==============================================================================
# *** Degree Quran Circle *** #
class DegreeQuranCircleList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranCircle.objects.all()
    serializer_class = serializers.DegreeQuranCircleSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class DegreeQuranCircleListApp(generics.ListAPIView):
    queryset = models.DegreeQuranCircle.objects.filter(is_visible=True)
    serializer_class = serializers.DegreeQuranCircleSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class DegreeQuranCircleListAdmin(generics.ListAPIView):
    queryset = models.DegreeQuranCircle.objects.all()
    serializer_class = serializers.DegreeQuranCircleSerializer
    permission_classes = [IsAuthenticated]



class DegreeQuranCirclePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DegreeQuranCircle.objects.all()
    serializer_class = serializers.DegreeQuranCircleSerializer
    permission_classes = [AllowAny]




class DegreeQuranCircleResultList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranCircle.objects.all()
    serializer_class = serializers.DegreeQuranCircleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class DegreeQuranCircleSearchList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranCircle.objects.all()
    serializer_class = serializers.DegreeQuranCircleSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(degree_present_roses__icontains=search)
                |Q(degree_past_roses__icontains=search) 
                )
        return qs






# ******************************************************************************
# ==============================================================================
# *** Live Quran Circle *** #
class LiveQuranCircleList(generics.ListCreateAPIView):
    queryset = models.LiveQuranCircle.objects.all()
    serializer_class = serializers.LiveQuranCircleSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class LiveQuranCircleListApp(generics.ListAPIView):
    queryset = models.LiveQuranCircle.objects.filter(is_visible=True)
    serializer_class = serializers.LiveQuranCircleSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class LiveQuranCircleListAdmin(generics.ListAPIView):
    queryset = models.LiveQuranCircle.objects.all()
    serializer_class = serializers.LiveQuranCircleSerializer
    permission_classes = [IsAuthenticated]



class LiveQuranCirclePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LiveQuranCircle.objects.all()
    serializer_class = serializers.LiveQuranCircleSerializer
    permission_classes = [AllowAny]





class LiveQuranCircleResultList(generics.ListCreateAPIView):
    queryset = models.LiveQuranCircle.objects.all()
    serializer_class = serializers.LiveQuranCircleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class LiveQuranCircleSearchList(generics.ListCreateAPIView):
    queryset = models.LiveQuranCircle.objects.all()
    serializer_class = serializers.LiveQuranCircleSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(zoom_url__icontains=search) 
                |Q(date_time__icontains=search)  
                )
        return qs





# ******************************************************************************
# ==============================================================================
# ***   Quran Exam   *** #
class QuranExamList(generics.ListCreateAPIView):
    queryset = models.QuranExam.objects.all()
    serializer_class = serializers.QuranExamSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class QuranExamListApp(generics.ListAPIView):
    queryset = models.QuranExam.objects.filter(is_visible=True)
    serializer_class = serializers.QuranExamSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class QuranExamListAdmin(generics.ListAPIView):
    queryset = models.QuranExam.objects.all()
    serializer_class = serializers.QuranExamSerializer
    permission_classes = [IsAuthenticated]



class QuranExamPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.QuranExam.objects.all()
    serializer_class = serializers.QuranExamSerializer
    permission_classes = [AllowAny]





class QuranExamResultList(generics.ListCreateAPIView):
    queryset = models.QuranExam.objects.all()
    serializer_class = serializers.QuranExamSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class QuranExamSearchList(generics.ListCreateAPIView):
    queryset = models.QuranExam.objects.all()
    serializer_class = serializers.QuranExamSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(exam_status__icontains=search)
                |Q(exam_type__icontains=search) 
                |Q(title__icontains=search) 
                |Q(date__icontains=search) 
                )
        return qs





# ******************************************************************************
# ==============================================================================
# ***   Degree Quran Exam   *** #
class DegreeQuranExamList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranExam.objects.all()
    serializer_class = serializers.DegreeQuranExamSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class DegreeQuranExamListApp(generics.ListAPIView):
    queryset = models.DegreeQuranExam.objects.filter(is_visible=True)
    serializer_class = serializers.DegreeQuranExamSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class DegreeQuranExamListAdmin(generics.ListAPIView):
    queryset = models.DegreeQuranExam.objects.all()
    serializer_class = serializers.DegreeQuranExamSerializer
    permission_classes = [IsAuthenticated]



class DegreeQuranExamPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DegreeQuranExam.objects.all()
    serializer_class = serializers.DegreeQuranExamSerializer
    permission_classes = [AllowAny]






class DegreeQuranExamResultList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranExam.objects.all()
    serializer_class = serializers.DegreeQuranExamSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class DegreeQuranExamSearchList(generics.ListCreateAPIView):
    queryset = models.DegreeQuranExam.objects.all()
    serializer_class = serializers.DegreeQuranExamSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(degree_exam__icontains=search)
                |Q(is_visible__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# ***    Presence And Absence    *** #
class PresenceAndAbsenceList(generics.ListCreateAPIView):
    queryset = models.PresenceAndAbsence.objects.all()
    serializer_class = serializers.PresenceAndAbsenceSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class PresenceAndAbsenceListApp(generics.ListAPIView):
    queryset = models.PresenceAndAbsence.objects.filter(is_visible=True)
    serializer_class = serializers.PresenceAndAbsenceSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class PresenceAndAbsenceListAdmin(generics.ListAPIView):
    queryset = models.PresenceAndAbsence.objects.all()
    serializer_class = serializers.PresenceAndAbsenceSerializer
    permission_classes = [IsAuthenticated]



class PresenceAndAbsencePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PresenceAndAbsence.objects.all()
    serializer_class = serializers.PresenceAndAbsenceSerializer
    permission_classes = [AllowAny]






class PresenceAndAbsenceResultList(generics.ListCreateAPIView):
    queryset = models.PresenceAndAbsence.objects.all()
    serializer_class = serializers.PresenceAndAbsenceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class PresenceAndAbsenceSearchList(generics.ListCreateAPIView):
    queryset = models.PresenceAndAbsence.objects.all()
    serializer_class = serializers.PresenceAndAbsenceSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(session_type__icontains=search)
                |Q(date__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** Degree Presence And Absence *** #
class DegreePresenceAndAbsenceList(generics.ListCreateAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.all()
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class DegreePresenceAndAbsenceListApp(generics.ListAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.filter(is_visible=True)
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class DegreePresenceAndAbsenceListAdmin(generics.ListAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.all()
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer
    permission_classes = [IsAuthenticated]



class DegreePresenceAndAbsencePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.all()
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer
    permission_classes = [AllowAny]






class DegreePresenceAndAbsenceResultList(generics.ListCreateAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.all()
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class DegreePresenceAndAbsenceSearchList(generics.ListCreateAPIView):
    queryset = models.DegreePresenceAndAbsence.objects.all()
    serializer_class = serializers.DegreePresenceAndAbsenceSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(status_icontains=search)
                |Q(date__icontains=search) 
                |Q(is_visible__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** File And Library *** #
class FileAndLibraryList(generics.ListCreateAPIView):
    queryset = models.FileAndLibrary.objects.all()
    serializer_class = serializers.FileAndLibrarySerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class FileAndLibraryListApp(generics.ListAPIView):
    queryset = models.FileAndLibrary.objects.filter(is_visible=True)
    serializer_class = serializers.FileAndLibrarySerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class FileAndLibraryListAdmin(generics.ListAPIView):
    queryset = models.FileAndLibrary.objects.all()
    serializer_class = serializers.FileAndLibrarySerializer
    permission_classes = [IsAuthenticated]



class FileAndLibraryPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FileAndLibrary.objects.all()
    serializer_class = serializers.FileAndLibrarySerializer
    permission_classes = [AllowAny]





class FileAndLibraryResultList(generics.ListCreateAPIView):
    queryset = models.FileAndLibrary.objects.all()
    serializer_class = serializers.FileAndLibrarySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class FileAndLibrarySearchList(generics.ListCreateAPIView):
    queryset = models.FileAndLibrary.objects.all()
    serializer_class = serializers.FileAndLibrarySerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(file__icontains=search) 
                |Q(file_url__icontains=search) 
                )
        return qs





# ******************************************************************************
# ==============================================================================
# ***   Teacher Note   *** #
class TeacherNoteList(generics.ListCreateAPIView):
    queryset = models.TeacherNote.objects.all()
    serializer_class = serializers.TeacherNoteSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class TeacherNoteListApp(generics.ListAPIView):
    queryset = models.TeacherNote.objects.filter(is_visible=True)
    serializer_class = serializers.TeacherNoteSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class TeacherNoteListAdmin(generics.ListAPIView):
    queryset = models.TeacherNote.objects.all()
    serializer_class = serializers.TeacherNoteSerializer
    permission_classes = [IsAuthenticated]



class TeacherNotePK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TeacherNote.objects.all()
    serializer_class = serializers.TeacherNoteSerializer
    permission_classes = [AllowAny]






class TeacherNoteResultList(generics.ListCreateAPIView):
    queryset = models.TeacherNote.objects.all()
    serializer_class = serializers.TeacherNoteSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class TeacherNoteSearchList(generics.ListCreateAPIView):
    queryset = models.TeacherNote.objects.all()
    serializer_class = serializers.TeacherNoteSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(description__icontains=search)
                |Q(is_visible__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** Certificate Quran *** #
class CertificateQuranList(generics.ListCreateAPIView):
    queryset = models.CertificateQuran.objects.all()
    serializer_class = serializers.CertificateQuranSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class CertificateQuranListApp(generics.ListAPIView):
    queryset = models.CertificateQuran.objects.filter(is_visible=True)
    serializer_class = serializers.CertificateQuranSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class CertificateQuranListAdmin(generics.ListAPIView):
    queryset = models.CertificateQuran.objects.all()
    serializer_class = serializers.CertificateQuranSerializer
    permission_classes = [IsAuthenticated]



class CertificateQuranPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CertificateQuran.objects.all()
    serializer_class = serializers.CertificateQuranSerializer
    permission_classes = [AllowAny]






class CertificateQuranResultList(generics.ListCreateAPIView):
    queryset = models.CertificateQuran.objects.all()
    serializer_class = serializers.CertificateQuranSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class CertificateQuranSearchList(generics.ListCreateAPIView):
    queryset = models.CertificateQuran.objects.all()
    serializer_class = serializers.CertificateQuranSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(title__icontains=search)
                |Q(description__icontains=search) 
                |Q(file__icontains=search) 
                |Q(file_url__icontains=search) 
                |Q(is_visible__icontains=search) 
                )
        return qs




# ******************************************************************************
# ==============================================================================
# *** Student Quran School Enrollment *** #
class StudentQuranSchoolEnrollmentList(generics.ListCreateAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.all()
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]


class StudentQuranSchoolEnrollmentListApp(generics.ListAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.filter(is_visible=True)
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer
    permission_classes = [AllowAny]
    # pagination_class = StandardResultSetPagination


class StudentQuranSchoolEnrollmentListAdmin(generics.ListAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.all()
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer
    permission_classes = [IsAuthenticated]



class StudentQuranSchoolEnrollmentPK(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.all()
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer
    permission_classes = [AllowAny]





class StudentQuranSchoolEnrollmentResultList(generics.ListCreateAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.all()
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            try:
                limit = int(self.request.GET['result'])
                qs = qs.order_by('-id').filter(is_visible=True)[:limit]
            except ValueError:
                # Handle the case where 'result' is not an integer
                pass
        return qs
    

    
class StudentQuranSchoolEnrollmentSearchList(generics.ListCreateAPIView):
    queryset = models.StudentQuranSchoolEnrollment.objects.all()
    serializer_class = serializers.StudentQuranSchoolEnrollmentSerializer
    pagination_class = StandardResultSetPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()

        if 'searchstring' in self.kwargs:
            search = self.kwargs['searchstring'] 
            qs = qs.filter(
                Q(full_name__icontains=search)
                |Q(age__icontains=search) 
                |Q(phone_number__icontains=search) 
                |Q(whatsapp_number__icontains=search) 
                |Q(email__icontains=search) 
                |Q(description__icontains=search) 
                |Q(country__icontains=search) 
                |Q(price__icontains=search) 
                |Q(payment_id__icontains=search) 
                |Q(is_visible__icontains=search) 
                )
        return qs

# 
# class EnrolledStuentPK(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer


# def fetch_enroll_status(request,student_id,course_id):
#     student = models.User.objects.filter(id=student_id).first()
#     course = models.Course.objects.filter(id=course_id).first()
#     enroll_status = models.StudentCourseEnrollment.objects.filter(course=course,student=student).count()

#     if enroll_status:
#         return JsonResponse({'bool':True})
#     else:
#         return JsonResponse({'bool':False})


# # class FetchEnrollStatusView(generics.RetrieveAPIView):
# class FetchEnrollStatusView(APIView):
#     # pagination_class = StandardResultSetPagination
#     # permission_classes = [IsAuthenticated]

#     def get(self, request, student_id, course_id):
#         student = models.User.objects.filter(id=student_id).first()
#         course = models.Course.objects.filter(id=course_id).first()
#         enroll_status = models.StudentCourseEnrollment.objects.filter(course=course, student=student).exists()
#         return Response({'bool': enroll_status})


 


# #-
# class EnrolledStuentCourseList(generics.ListCreateAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = ""
#         if 'course_id' in self.kwargs:
#             course_id = self.kwargs['course_id']
#             # course = models.Course.objects.get(pk=course_id)
#             return models.StudentCourseEnrollment.objects.filter(course=course_id)
        

# class EnrolledAllStuentList(generics.ListCreateAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = ""   
#         if 'teacher_id' in self.kwargs:
#             teacher_id = self.kwargs['teacher_id']
#             teacher = models.User.objects.get(pk=teacher_id)
#             return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
       

# class EnrolledStuentPkList(generics.ListCreateAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = ""
#         if 'student_id' in self.kwargs:
#             student_id = self.kwargs['student_id']
#             student = models.User.objects.get(pk=student_id)
#             return models.StudentCourseEnrollment.objects.filter(student=student).distinct()
        

# class EnrolledRecomemdedStuentList(generics.ListCreateAPIView):
#     queryset = models.StudentCourseEnrollment.objects.all()
#     serializer_class = serializers.StudentCourseEnrollSerializer
#     pagination_class = StandardResultSetPagination
#     permission_classes = [AllowAny]
#     # permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = ""

#         if 'studentId' in self.kwargs:
#             student_id = self.kwargs['student_id']
#             student = models.User.objects.get(pk=student_id)
#             print(student.interseted_categories)
#             queries = [Q(techs__iendwith=value) for value in student.interseted_categories]
#             query = queries.pop()
#             for item in queries:
#                 query |= item
#             qs = models.Course.objects.filter(query)

#         return qs



# ******************************************************************************
# ==============================================================================
# *** Interview Date *** #












































# ******************************************************************************
# ==============================================================================
# *** App Stats ***
class AppStatsView(generics.GenericAPIView):
    def get(self, request):
        # 
        users_count = models.User.objects.count()
        admins_count = models.User.objects.filter(is_admin=True).count()
        teachers_count = models.User.objects.filter(is_teacher=True).count()
        staffs_count = models.User.objects.filter(is_superuser=False, is_staff=True).count()
        students_count = models.User.objects.filter(is_student=True).count()

        # 
        categories_section_count = models.CategorySection.objects.filter(is_visible=True).count()
        sections_course_count = models.SectionCourse.objects.filter(is_visible=True).count()

        # 
        courses_count = models.Course.objects.filter(is_visible=True).count()
        sections_in_course_count = models.SectionInCourse.objects.filter(is_visible=True).count()
        lessons_count = models.LessonInCourse.objects.filter(is_visible=True).count()

        # 
        coupons_course_count = models.CouponCourse.objects.filter(is_visible=True).count()
        
        # 
        total_enrolled_students = models.StudentCourseEnrollment.objects.count()

        # 
        questionbanks_count = models.QuestionBank.objects.filter(is_visible=True).count()

        # 
        contacts_count = models.ContactUsUser.objects.count()
        reviews_count = models.ReviewUser.objects.count()

        return Response({
            # 
            'users_count': users_count,
            'admins_count': admins_count,
            'teachers_count': teachers_count,
            'staffs_count': staffs_count,
            'students_count': students_count,
            
            # 
            'categories_section_count': categories_section_count,
            'sections_course_count': sections_course_count,

            # 
            'courses_count': courses_count,
            'sections_in_course_count': sections_in_course_count,
            'lessons_count': lessons_count,

            # 
            'coupons_course_count': coupons_course_count,

            # 
            'total_enrolled_students': total_enrolled_students,

            # 
            'questionbanks_count': questionbanks_count,

            # 
            'contacts_count': contacts_count,
            'reviews_count': reviews_count,
        })






# ******************************************************************************
# ==============================================================================
# *** Admin Dashboard Stats ***
class AdminDashboardStatsView(generics.GenericAPIView):
    def get(self, request):
        # 
        users_count = models.User.objects.count()
        superuser_count = models.User.objects.filter(is_superuser=True, is_staff=True).count()
        admins_count = models.User.objects.filter(is_admin=True).count()
        teachers_count = models.User.objects.filter(is_teacher=True).count()
        staffs_count = models.User.objects.filter(is_superuser=False, is_staff=True).count()
        students_count = models.User.objects.filter(is_student=True).count()

        #   
        categories_section_count = models.CategorySection.objects.count()
        sections_course_count = models.SectionCourse.objects.count()

        # 
        courses_count = models.Course.objects.count()
        sections_in_course_count = models.SectionInCourse.objects.count()
        lessons_count = models.LessonInCourse.objects.count()

        # 
        courses_is_live_count = models.Course.objects.filter(is_live=True).count()

        # 
        packages_course_count = models.PackageCourse.objects.count()
        
        # 
        categories_book_count = models.CategoryBook.objects.count()

        # 
        books_count = models.Book.objects.count()

        # 
        powerpoints_count = models.Powerpoint.objects.count()
 
        # 
        powerpointservice_count = models.PowerpointService.objects.count()
        powerpointservice_replay_count = models.PowerpointService.objects.filter(status="reply").count()

        # 
        proofreadingservices_count = models.ProofreadingService.objects.count()
        proofreadingservices_replay_count = models.ProofreadingService.objects.filter(status="reply").count()
  
        # 
        categories_blogs_count = models.CategoryBlog.objects.count()

        # 
        blogs_count = models.Blog.objects.count()

        # 
        youTubesuggestions_count = models.YouTubeSuggestionsBlog.objects.count()

        # 
        famoussayings_count = models.FamousSayings.objects.count()

        # 
        coupons_course_count = models.CouponCourse.objects.count()
        
        # 
        total_enrolled_students = models.StudentCourseEnrollment.objects.count()

        # 
        questionbanks_count = models.QuestionBank.objects.count()


        if 'user_id' in request.GET:
            user_id = request.GET['user_id']
            if user_id[-1] == "/":
                user_id = user_id[:-1]
            user_id = int(user_id)

            # 
            admin_categories_section_count = models.CategorySection.objects.filter(user=user_id).count()
            admin_sections_course_count = models.SectionCourse.objects.filter(user=user_id).count()
            
            # 
            admin_courses_count = models.Course.objects.filter(user=user_id).count()

            # 
            admin_courses_is_live_count = models.Course.objects.filter(user=user_id, is_live=True).count()
            
            # 
            admin_packages_course_count = models.PackageCourse.objects.filter(user=user_id).count()

            # 
            admin_categories_book_count = models.CategoryBook.objects.filter(user=user_id).count()
            
            # 
            admin_books_count = models.Book.objects.filter(user=user_id).count()
  
            # 
            admin_powerpoints_count = models.Powerpoint.objects.filter(user=user_id).count()
  
            # 
            admin_proofreadingservices_count = models.ProofreadingService.objects.filter(user=user_id).count()

            # 
            admin_categories_blogs_count = models.CategoryBlog.objects.filter(user=user_id).count()
  
            # 
            admin_blogs_count = models.Blog.objects.filter(user=user_id).count()
  
            # 
            admin_youTubesuggestions_count = models.YouTubeSuggestionsBlog.objects.filter(user=user_id).count()
  
            # 
            admin_famoussayings_count = models.FamousSayings.objects.filter(user=user_id).count()

            # 
            admin_coupon_course_count = models.CouponCourse.objects.filter(user=user_id).count()
            
            # 
            admin_banks_count = models.QuestionBank.objects.filter(user=user_id).count()
        else:
            # 
            admin_categories_section_count = 0
            admin_sections_course_count = 0
            admin_courses_count = 0

            # 
            admin_courses_is_live_count = 0

            # 
            admin_packages_course_count = 0

            # 
            admin_categories_book_count = 0
            admin_books_count = 0

            # 
            admin_powerpoints_count = 0

            # 
            admin_proofreadingservices_count = 0

            # 
            admin_categories_blogs_count = 0
            admin_blogs_count = 0
            admin_youTubesuggestions_count = 0

            # 
            admin_famoussayings_count = 0
            
            # 
            admin_coupon_course_count = 0
            admin_banks_count = 0

        contacts_count = models.ContactUsUser.objects.count()
        reviews_count = models.ReviewUser.objects.count()

        return Response({
            # 
            'users_count': users_count,
            'superuser_count': superuser_count,
            'admins_count': admins_count,
            'teachers_count': teachers_count,
            'staffs_count': staffs_count,
            'students_count': students_count,

            # 
            'categories_section_count': categories_section_count,
            'sections_course_count': sections_course_count,

            # 
            'courses_count': courses_count,
            'sections_in_course_count': sections_in_course_count,
            'lessons_count': lessons_count,
            
            # 
            'courses_is_live_count': courses_is_live_count,
            'admin_courses_is_live_count': admin_courses_is_live_count,

            # 
            'packages_course_count': packages_course_count,
            'admin_packages_course_count': admin_packages_course_count,

            # 
            'categories_book_count': categories_book_count,
            'admin_categories_book_count': admin_categories_book_count,

            # 
            'books_count': books_count,
            'admin_books_count': admin_books_count,
            
            # 
            'powerpoints_count': powerpoints_count,
            'admin_powerpoints_count': admin_powerpoints_count,

            # 
            'powerpointservice_count': powerpointservice_count,
            'powerpointservice_replay_count': powerpointservice_replay_count,
            
            # 
            'proofreadingservices_count': proofreadingservices_count,
            'proofreadingservices_replay_count': proofreadingservices_replay_count,
            'admin_proofreadingservices_count': admin_proofreadingservices_count,
            
            # 
            'categories_blogs_count': categories_blogs_count,
            'admin_categories_blogs_count': admin_categories_blogs_count,
            
            # 
            'blogs_count': blogs_count,
            'admin_blogs_count': admin_blogs_count,
            
            # 
            'youTubesuggestions_count': youTubesuggestions_count,
            'admin_youTubesuggestions_count': admin_youTubesuggestions_count,
            
            # 
            'famoussayings_count': famoussayings_count,
            'admin_famoussayings_count': admin_famoussayings_count,
            
            # 
            'coupons_course_count': coupons_course_count,

            # 
            'total_enrolled_students': total_enrolled_students,

            # 
            'questionbanks_count': questionbanks_count,

            # 
            "admin_categories_section_count": admin_categories_section_count,
            "admin_sections_course_count": admin_sections_course_count,
            "admin_courses_count": admin_courses_count,
            "admin_coupon_course_count": admin_coupon_course_count,
            "admin_banks_count": admin_banks_count,
            
            # 
            'contacts_count': contacts_count,
            'reviews_count': reviews_count,
        })





# ******************************************************************************
# ==============================================================================
# *** Teacher Dashboard Stats ***
class TeacherDashboardStatsView(generics.GenericAPIView):
    def get(self, request):
        if 'user_id' in request.GET:
            user_id = request.GET['user_id']
            if user_id[-1] == "/":
                user_id = user_id[:-1]
            user_id = int(user_id)

            # 
            teacher_courses_count = models.Course.objects.filter(user=user_id).count()
            teacher_banks_count = models.QuestionBank.objects.filter(user=user_id).count()
        else:
            # 
            teacher_courses_count = 0
            teacher_banks_count = 0

        contacts_count = models.ContactUsUser.objects.count()
        reviews_count = models.ReviewUser.objects.count()

        return Response({
            # 
            "teacher_courses_count": teacher_courses_count,
            "teacher_banks_count": teacher_banks_count,

            # 
            'contacts_count': contacts_count,
            'reviews_count': reviews_count,
        })






# ******************************************************************************
# ==============================================================================
# *** Student Dashboard Stats ***
class StudentDashboardStatsView(generics.GenericAPIView):
    def get(self, request):
        if 'user_id' in request.GET:
            user_id = request.GET['user_id']
            if user_id[-1] == "/":
                user_id = user_id[:-1]
            user_id = int(user_id)

            # 
            student_courses_enrollment_count = models.StudentCourseEnrollment.objects.filter(student=user_id).count()
            student_favorite_course_count = models.StudentFavoriteCourse.objects.filter(student=user_id).count()

            # 
            student_packages_course_count = models.PackageCourse.objects.filter(user=user_id).count()

            # 
            student_proofreadingservices_count = models.ProofreadingService.objects.filter(user=user_id).count()
            student_proofreadingservices_replay_count = models.ProofreadingService.objects.filter(user=user_id, status="reply").count()

            # 
            student_powerpoints_enrollment_count = models.StudentPowerpointEnrollment.objects.filter(student=user_id).count()

            # 
            student_powerpointservices_count = models.PowerpointService.objects.filter(user=user_id).count()
            student_powerpointservices_replay_count = models.PowerpointService.objects.filter(user=user_id, status="reply").count()

        else:
            # 
            student_courses_enrollment_count = 0
            student_favorite_course_count = 0

            # 
            student_packages_course_count = 0

            # 
            student_proofreadingservices_count = 0
            student_proofreadingservices_replay_count = 0

            # 
            student_powerpoints_enrollment_count = 0

            # 
            student_powerpointservices_count = 0
            student_powerpointservices_replay_count = 0
             

        return Response({
            # 
            "student_courses_enrollment_count": student_courses_enrollment_count,
            "student_favorite_course_count": student_favorite_course_count,

            # 
            "student_packages_course_count": student_packages_course_count,

            # 
            "student_proofreadingservices_count": student_proofreadingservices_count,
            "student_proofreadingservices_replay_count": student_proofreadingservices_replay_count,
      
            # 
            "student_powerpoints_enrollment_count": student_powerpoints_enrollment_count,

            # 
            "student_powerpointservices_count": student_powerpointservices_count,
            "student_powerpointservices_replay_count": student_powerpointservices_replay_count,

        })








# ******************************************************************************
# ==============================================================================
# ***  ***
