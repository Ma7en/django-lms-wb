# 
from django.urls import path, include
from django.urls import path, include



#
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers



#
from . import views




# =================================================================
# 
# router = DefaultRouter()
# router.register(r'', views.CourseViewSet)
# router.register(r'sections', views.SectionViewSet)
# router.register(r'items', views.ItemViewSet)
# router.register(r'files', views.FileViewSet)
# router.register(r'questions', views.QuestionViewSet)

# =================================================================
# 
# router = routers.DefaultRouter()
# router.register(r'courses', views.CourseViewSet)

# # Nested routers for course sections
# courses_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
# courses_router.register(r'sections', views.SectionViewSet, basename='course-sections')

# # Nested routers for section items
# sections_router = routers.NestedSimpleRouter(courses_router, r'sections', lookup='section')
# sections_router.register(r'items', views.ItemViewSet, basename='section-items')

# # Nested routers for item files
# items_router = routers.NestedSimpleRouter(sections_router, r'items', lookup='item')
# items_router.register(r'files', views.FileViewSet, basename='item-files')
 
# # Nested routers for files
# items_router = routers.NestedSimpleRouter(sections_router, r'files', lookup='files')
# items_router.register(r'questions', views.FileViewSet, basename='questions')
 
# # Nested routers for questions
# questions_router = routers.NestedSimpleRouter(sections_router, r'questions', lookup='questions')
# # questions_router.register(r'files', views.FileViewSet, basename='item-files')



# =================================================================
questionbank = DefaultRouter() 
# questionbank.register(r'', views.QuestionBankViewSet)
# questionbank.register(r'', views.QuestionInBankViewSet)



urlpatterns = [
    # =================================================================
    # *** Category Section *** #
    # (List)
    path(
        "category-section/list/",
        views.CategorySectionList.as_view(),
        name="category-section-list",
    ),
    # (List App)
    path(
        "category-section/list-app/",
        views.CategorySectionListApp.as_view(),
        name="category-section-list",
    ),
    # (List App)
    path(
        "category-section/list-admin/",
        views.CategorySectionListAdmin.as_view(),
        name="category-section-list",
    ),
    # (List Result)
    path(
        "category-section/result/", #?result=9
        views.CategorySectionResultList.as_view(),
        name="course-result-list",
    ),
    # (PK)
    path(
        "category-section/<int:pk>/",
        views.CategorySectionPK.as_view(),
        name="category-section-pk",
    ),
    # (Search)
    path(
        'category-section/search/<str:searchstring>/', 
        views.CategorySectionSearchList.as_view(),
        name="category-section-search-list",
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Section Course *** #
    # (List)
    path(
        "section-course/list/",
        views.SectionCourseList.as_view(),
        name="section-course-list",
    ),
    # (List App)
    path(
        "section-course/list-app/",
        views.SectionCourseListApp.as_view(),
        name="section-course-list",
    ),
    # (List Admin)
    path(
        "section-course/list-admin/",
        views.SectionCourseListAdmin.as_view(),
        name="section-course-list",
    ),
    # (List Result)
    path(
        "section-course/result/", #?result=9
        views.SectionCourseResultList.as_view(),
        name="course-result-list",
    ),
    # (PK)
    path(
        "section-course/<int:pk>/",
        views.SectionCoursePK.as_view(),
        name="section-course-pk",
    ),
    # (Search)
    path(
        'section-course/search/<str:searchstring>/', 
        views.SectionCourseSearchList.as_view(),
        name="section-course-search-list",
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # +++
    path(
        "section-course/category/list/",
        views.SectionCourseCategoriesList.as_view(),
        name="section-course-list",
    ),
    # (Category PK)
    path(
        "section-course/category/<int:pk>/",
        views.SectionCourseCategoryList.as_view(),
        name="section-course-category-pk",
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Course *** #
    # (List)
    path(
        "course/list/",
        views.CourseList.as_view(),
        name="course-list",
    ),
    # (List App)
    path(
        "course/list-app/",
        views.CourseListApp.as_view(),
        name="course-list",
    ),
    # (List Admin)
    path(
        "course/list-admin/",
        views.CourseListAdmin.as_view(),
        name="course-list-admin",
    ),
    # (List Is Free App)
    path(
        "course-isfree/list-app/",
        views.CourseIsFreeListApp.as_view(),
        name="course-isfree-list-app",
    ),
    # (List Is Live)
    path(
        "course-islive/list/",
        views.CourseIsLiveList.as_view(),
        name="course-islive-list",
    ),
    # (List Is Live App)
    path(
        "course-islive/list-app/",
        views.CourseIsLiveListApp.as_view(),
        name="course-islive-list-app",
    ),
    # (List Is Live Admin)
    path(
        "course-islive/list-admin/",
        views.CourseIsLiveListAdmin.as_view(),
        name="course-islive-list-admin",
    ),
    # (List Ids)
    path(
        "course-ids/list/", # ?ids=1,2,5
        views.CourseIdsList.as_view(),
        name="course-ids-list",
    ),
    # (List Result)
    path(
        "course/result/", #?result=9
        views.CourseResultList.as_view(),
        name="course-result-list",
    ),
    # (PK)
    path(
        "course/<int:pk>/",
        views.CoursePK.as_view(),
        name="course-pk",
    ),
    # (All PK)
    path(
        "course/all/<int:pk>/",
        views.CourseDetailAll.as_view(),
        name="course-all-pk",
    ),
    # +++
    path(
        "course/",
        views.CourseListAPI.as_view(),
        name="course-list-api",
    ),
    # +++
    path(
        'courses/search/<str:searchstring>/', 
        views.CourseListAPI.as_view(),
        name="course-list-search",
    ),


    # Course URLs
    path(
        'courses/', 
        views.CourseListCreate.as_view(), 
        name='course-list',
    ),
    # +++
    path(
        'courses/<int:pk>/', 
        views.CourseRetrieveUpdateDestroy.as_view(), 
        name='course-detail',
    ),
    # +++
    path(
        'public/courses/', 
        views.PublicCourseList.as_view(), 
        name='public-course-list',
    ),
    # (Search)
    path(
        'courses/search/<str:searchstring>/', 
        views.CoursesSearchList.as_view(),
        name="courses-search-list",
    ),
    # (Search Is Live)
    path(
        'courses-islive/search/<str:searchstring>/', 
        views.CoursesIsLiveSearchList.as_view(),
        name="courses-islive-search-list",
    ),

   


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Section PK)
    path(
        "course/section-course/<int:pk>/",
        views.CourseSectionCourseList.as_view(),
        name="course-section-course-pk",
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ), 
    # Section In Course URLs (nested under courses)
    path(
        'courses/sections/list/', 
        views.SectionInCourseList.as_view(), 
        name='sections-in-course-list',
    ),
    # (PK)
    path(
        'courses/sections/<int:pk>/', 
        views.SectionInCoursePK.as_view(), 
        name='section-in-course-pk',
    ),
    # ()
    path(
        'courses/<int:course_id>/sections/', 
        views.SectionInCourseListCreate.as_view(), 
        name='section-in-course-list',
    ),
    # 
    path(
        'courses/<int:course_id>/sections/<int:pk>/', 
        views.SectionInCourseRetrieveUpdateDestroy.as_view(), 
        name='section-in-course-detail',
    ),

   

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ), 
    # Lesson In Course URLs (nested under sections)
    path(
        'courses/sections/lessons/list/',
        views.LessonInCourseList.as_view(), 
        name='lesson-in-course-list',
    ),
    path(
        'courses/sections/lessons/<int:pk>/',
        views.LessonInCoursePK.as_view(), 
        name='lesson-in-course-pk',
    ),

    path(
        'courses/sections/<int:section_id>/lessons/', 
        views.LessonInCourseListCreate.as_view(), 
        name='lesson-list',
    ),

    path(
        'courses/sections/<int:section_id>/lessons/<int:pk>/', 
        views.LessonInCourseRetrieveUpdateDestroy.as_view(), 
        name='lesson-detail',
    ),
    path(
        'courses/sections/list/<int:section_id>/lessons/', 
        views.LessonInCourseCreateView.as_view(), 
        name='lesson-create',
    ),

   

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ), 
    # Student Answer In Course studentanswer
    # ()
    path(
        'courses/sections/lessons/student-answer/list/',
        views.StudentAnswerInCourseList.as_view(), 
        name='student-in-answer-list',
    ),
    # ()
    path(
        'courses/sections/lessons/student-answer/<int:pk>/',
        views.StudentAnswerInCoursePK.as_view(), 
        name='student-in-answer-pk',
    ),
    # ()
    path(
        'fetch-student-answer-in-course-status/<int:student_id>/<int:lesson_id>/', 
        # views.fetch_enroll_status,
        views.FetchStudentAnswerInCourseStatus.as_view(),
        name="fetch-student-answer-in-course-status-student_id-lesson_id",
    ),
    # 
    # path(
    #     'courses/sections/<int:section_id>/lessons/', 
    #     views.LessonInCourseListCreate.as_view(), 
    #     name='lesson-list',
    # ),
    # 
    # path(
    #     'courses/sections/<int:section_id>/lessons/<int:pk>/', 
    #     views.LessonInCourseRetrieveUpdateDestroy.as_view(), 
    #     name='lesson-detail',
    # ),
    # 
    # path(
    #     'courses/sections/list/<int:section_id>/lessons/', 
    #     views.LessonInCourseCreateView.as_view(), 
    #     name='lesson-create',
    # ),





    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # File In Course URLs (nested under lessons)
    path(
        'courses/sections/lessons/files/list/', 
        views.FileInCourseList.as_view(), 
        name='lesson-file-in-course-list',
    ),
    path(
        'courses/sections/lessons/files/<int:pk>/', 
        views.FileInCoursePK.as_view(), 
        name='lesson-file-in-course-pk',
    ),

    path(
        'courses/sections/lessons/list/<int:lesson_id>/files/', 
        views.FileInCourseListCreate.as_view(), 
        name='lesson-file-list',
    ),

    path(
        'courses/sections/lessons/<int:lesson_id>/files/<int:pk>/', 
        views.FileInCourseRetrieveUpdateDestroy.as_view(), 
        name='lesson-file-detail',
    ),
    path(
        'courses/sections/lessons/<int:lesson_id>/files/', 
        views.FileInCourseCreateView.as_view(), 
        name='lesson-file-create',
    ),


    
    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # Question In Course URLs (nested under lessons)
    path(
        'courses/sections/lessons/questions/list/', 
        views.QuestionInCourseList.as_view(), 
        name='question-in-cours-list',
    ),
    path(
        'courses/sections/lessons/questions/<int:pk>/', 
        views.QuestionInCoursePK.as_view(), 
        name='question-in-cours-pk',
    ),

    path(
        'courses/sections/lessons/list/<int:lesson_id>/questions/', 
        views.QuestionInCourseListCreate.as_view(), 
        name='question-list',
    ),

    path(
        'courses/sections/lessons/<int:lesson_id>/questions/<int:pk>/', 
        views.QuestionInCourseRetrieveUpdateDestroy.as_view(), 
        name='question-detail',
    ),
    path(
        'courses/sections/lessons/<int:lesson_id>/questions/', 
        views.QuestionCreateView.as_view(), 
        name='question-create',
    ),


    
    # =================================================================
    # ***  *** #
    # path('courses/', include(router.urls)),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Package Course *** #
    # (List)
    path(
        'package-course/list/', 
        views.PackageCourseList.as_view(), 
        name='package-course-list',
    ),
    # (List App)
    path(
        'package-course/list-app/', 
        views.PackageCourseListApp.as_view(), 
        name='package-course-list-app',
    ),
    # (List Admin)
    path(
        'package-course/list-admin/', 
        views.PackageCourseListAdmin.as_view(), 
        name='package-course-list-admin',
    ),
    # (List Result)
    path(
        'package-course/result/',  #?result=9
        views.PackageCourseResultList.as_view(), 
        name='package-course-result-list',
    ),
    # (PK)
    path(
        'package-course/<int:pk>/', 
        views.PackageCoursePk.as_view(), 
        name='package-course-pk',
    ),
    # (Search)
    path(
        'package-courses/search/<str:searchstring>/', 
        views.PackageCoursesSearchList.as_view(),
        name="package-courses-search-list",
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Package Course Discount *** #
    path(
        'package-course-discount/', 
        views.PackageCourseDiscountView.as_view(),
        name="package-course-discount",
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Coupon Course *** #
    # (List)
    path(
        "coupon-course/list/",
        views.CouponCourseList.as_view(),
        name="coupon-course-list",
    ),
    # (List App)
    path(
        "coupon-course/list-app/",
        views.CouponCourseListApp.as_view(),
        name="coupon-course-list",
    ),
    # (PK)
    path(
        "coupon-course/<int:pk>/",
        views.CouponCoursePK.as_view(),
        name="coupon-course-pk",
    ),
    # (Search)
    path(
        "coupon-course/search/<str:searchstring>/",
        views.CouponCourseSearch.as_view(),
        name="coupon-course-search",
    ),
    # (Search App)
    path(
        "coupon-course/search-app/<str:searchstring>/",
        views.CouponCourseSearchApp.as_view(),
        name="coupon-course-search",
    ),
    



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Course Payment Checkout *** #
    # (checkout)
    path(
        'create-checkout/', 
        views.CourseCreateCheckoutView.as_view(), 
        name='create-checkout',
    ),
    # (payment)
    path(
        'payment-result/', 
        views.CoursePaymentResultView.as_view(), 
        name='payment-result',
    ),




    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Student Enroll Course *** #
    path(
        'student-enroll-course/list/', 
        views.StudentEnrollCourseList.as_view(),
        name="student-enroll-course-list",
    ),
    path(
        'student-enroll-course/<int:pk>/', 
        views.StudentEnrollCoursePK.as_view(),
        name="student-enroll-course-pk",
    ),

    path(
        'student-enroll-course/', 
        views.StudentEnrollCourseList.as_view(),
        name="student-enroll-course",
    ),
    
    path(
        'fetch-enroll-status/<int:student_id>/<int:course_id>/', 
        # views.fetch_enroll_status,
        views.FetchEnrollStatusView.as_view(),
        name="fetch-enroll-status-student_id-course_id",
    ),

    #- 
    path(
        'fetch-enrolled-students/<int:course_id>/', 
        views.EnrolledStuentCourseList.as_view(),
        name="fetch-enrolled-students-course_id",
    ),

    path(
        'fetch-all-enrolled-students/<int:teacher_id>/', 
        views.EnrolledAllStuentList.as_view(),
        name="fetch-all-enrolled-students-teacher_id",
    ),

    path(
        'fetch-enrolled-courses/<int:student_id>/', 
        views.EnrolledStuentPkList.as_view(),
        name="fetch-enrolled-courses-student_id",
    ),

    path(
        'fetch-recomemded-courses/<int:student_id>/', 
        views.EnrolledRecomemdedStuentList.as_view(),
        name="fetch-recomemded-courses-student_id",
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Course Rating *** #
    path(
        'course-rating/list/', 
        views.CourseRatingList.as_view(),
        name="course-rating-list",
    ),
    path(
        'course-rating/<int:pk>/', 
        views.CourseRatingPK.as_view(),
        name="course-rating-pk",
    ),


    path(
        'course-rating/', 
        views.CourseRatingListAPI.as_view(),
        name="course-rating",
    ),
    path(
        'popular-courses-rating/', 
        views.CourseRatingListAPI.as_view(),
        name="popular-courses",
    ),

    path(
        'fetch-rating-status/<int:student_id>/<int:course_id>/',
        # views.fetch_rating_status, 
        views.FetchRatingStatusView.as_view(),
        name="fetch-rating-status-student_id-course_id",
    ),

        
    # path(
    #     'course-rating/search/<str:searchstring>/', 
    #     views.CourseRatingSearchList.as_view(),
    #     name="courses-rating-search-list",
    # ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Student Favorite Course *** #
    path(
        'student-add-favorte-course/list/', 
        views.StudentFavoriteCourseList.as_view(),
        name="student-add-favorte-course-list",
    ),
    path(
        'student-favorite-coourses/<int:pk>/', 
        views.StudentFavoriteCoursePK.as_view(),
        name="student-favorite-coourses-pk",
    ),

    path(
        'student-add-favorte-course/', 
        views.StudentFavoriteCourseListAPI.as_view(),
        name="student-add-favorte-course-list",
    ),
    path(
        'fetch-favorite-coourses/<int:student_id>/', 
        views.StudentFavoriteCourseListAPI.as_view(),
        name="fetch-favorite-coourses-student_id",
    ),

    path(
        'student-remove-favorite-course/<int:course_id>/<int:student_id>/', 
        # views.remove_favorite_course,
        views.RemoveFavoriteCourseView.as_view(),
        name="student-remove-favorite-course-course_id-student_id",
    ),

    
    # path(
    #     'student-favorite-course/search/<str:searchstring>/', 
    #     views.StudentFavoriteCourseSearchList.as_view(),
    #     name="student-favorite-course-search-list",
    # ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** Teacher Student Chat *** #
    path(
        'get-message-teacher-student-chat/list/', 
        views.TeacherStudentChatList.as_view(), 
        name="message-List-teacher-student-chat",
    ),
    path(
        'get-message-teacher-student-chat/<int:pk>/', 
        views.TeacherStudentChatPK.as_view(), 
        name="message-details-pk",
    ),


    # path(
    #     'send-message-teacher-student-chat/<int:teacher_id>/<int:student_id>/', 
    #     views.TeacherStudentChatBot, 
    #     name="Chat-Bot",
    # ),
    path(
        'send-message-teacher-student-chat/<int:teacher_id>/<int:student_id>/', 
        views.TeacherStudentChatBot.as_view(), 
        name="Chat-Bot",
    ),

    path(
        'get-message-teacher-student-chat/<int:teacher_id>/<int:student_id>/', 
        views.TeacherStudentChatListAPI.as_view(), 
        name="Message-List",
    ),

    path(
        'send-group-message-teacher-student-chat/<int:teacher_id>/', 
        views.GroupTeacherStudentChatBot, 
        name="Group-Chat-Bot",
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # ================================================================
    # *** ) Student Progress Course *** #
    path(
        'track-progress/<int:lesson_id>/', 
        views.TrackLessonProgressView.as_view(), 
        name='track-progress',
    ),
    path(
        'user-progress/', 
        views.GetUserProgressView.as_view(), 
        name='user-progress',
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # ================================================================
    # *** ) Student Certificate *** #
    path(
        'certificate/<int:enrollment_id>/', 
        views.student_generate_certificate, 
        name='generate_certificate',
    ),

    path(
        'certificates/generate/<int:course_id>/', 
        views.StudentGenerateCertificateView.as_view(), 
        name='generate-certificate'
    ),
    path(
        'certificates/my-certificates/', 
        views.StudentCertificatesView.as_view(), 
        name='user-certificates'
    ),
    path(
        'certificates/verify/<str:verification_code>/', 
        views.StudentVerifyCertificateView.as_view(), 
        name='verify-certificate'
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # ================================================================
    # *** ) Questions Banks *** #
    # (List)
    path(
        'question-bank/list/', 
        views.QuestionBankList.as_view(), 
        name='questionbank-list',
    ),
    # (List Admin)
    path(
        'question-bank/list-admin/', 
        views.QuestionBankListAdmin.as_view(), 
        name='questionbank-list',
    ),
    # (List App)
    path(
        'question-bank/list-app/', 
        views.QuestionBankListApp.as_view(), 
        name='questionbank-list',
    ),
    # (List Result)
    path(
        "question-bank/result/", #?result=9
        views.QuestionBankResultList.as_view(),
        name="course-result-list",
    ),
    # (PK)
    path(
        'question-bank/<int:pk>/', 
        views.QuestionBankRetrieveUpdateDestroyView.as_view(), 
        name='questionbank-detail',
    ),
    
    
    

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Search)
    path(
        'question-bank/search/<str:searchstring>/', 
        views.QuestionBankSearchList.as_view(),
        name="question-bank-search-list",
    ),    
    # (Pk Section)
    path(
        "question-bank/section-course/<int:pk>/",
        views.QuestionBankSectionList.as_view(),
        name="question-bank-section-course-pk",
    ),
    



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # Get all questions for a specific bank
    # (Questions)
    path(
        'question-bank/<int:bank_id>/questions/', 
        views.BankQuestionsListView.as_view(), 
        name='bank-questions-list',
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # *** ) Question In Banks *** #
    # (List)
    path(
        'question-bank/questions/list/', 
        views.QuestionListCreate.as_view(), 
        name='question-list',
    ),
    # (Pk)
    path(
        'question-bank/questions/<int:pk>/', 
        views.QuestionRetrieveUpdateDestroyView.as_view(), 
        name='question-detail',
    ),
    


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # *** ) Question In Banks *** # 
    path(
        'question-bank/questions/search/<str:searchstring>/', 
        views.QuestionInBankSearchList.as_view(),
        name="question-in-bank-search-list",
    ),
    # (Pk Search)
    path(
        'question-bank/<int:bank_id>/questions/search/<str:searchstring>/', 
        views.BanksQuestionInBankSearchList.as_view(),
        name="question-in-bank-search-list",
    ),
    
    # path(
    #     '---------------------------------------------------------------------------------------------------------------/', 
    #     views.Space.as_view(),
    # ),
    # Choice URLs
    # path(
    #     'question-bank/questions/choices/list/', 
    #     views.ChoiceListCreateView.as_view(), 
    #     name='choice-list',
    # ),
    # path(
    #     'question-bank/questions/choices/<int:pk>/', 
    #     views.ChoiceRetrieveUpdateDestroyView.as_view(), 
    #     name='choice-detail',
    # ),


    
    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # *** ) Student Questions Banks Result *** #
    # (List)
    path(
        "student-questionbank/result/list-app/",
        views.StudentQuestionBankResultListApp.as_view(),
        name="student-question-bank-result-list",
    ),
    # (PK)
    path(
        "student-questionbank/result/<int:pk>/",
        views.StudentQuestionBankResultPK.as_view(),
        name="student-question-bank-result-pk",
    ),
    # (Pk Results)
    path(
        'question-bank/<int:bank_id>/results/', 
        views.StudentQuestionBankResultBankList.as_view(), 
        name="student-question-bank-result-bank-list",
    ),
    # (Pk User)
    path(
        'question-bank/results/<int:user_id>/', 
        views.StudentQuestionBankResultUserList.as_view(), 
        name="student-question-bank-result-bank-list",
    ),

    
 

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 5) Famous Sayings *** #
    # (List)
    path(
        'famous-saying/list/', 
        views.FamousSayingsList.as_view(), 
        name='famous-saying-list',
    ),
    # (List App)
    path(
        'famous-saying/list-app/', 
        views.FamousSayingsListApp.as_view(), 
        name='famous-saying-list-app',
    ),
    # (List Admin)
    path(
        'famous-saying/list-admin/', 
        views.FamousSayingsListAdmin.as_view(), 
        name='famous-saying-list-admin',
    ),
    # (List Result)
    path(
        'famous-saying/result/',  #?result=9
        views.FamousSayingsResultList.as_view(), 
        name='famous-saying-result-list',
    ),
    # (List Random Result)
    path(
        'famous-saying/random/result/',  #?result=9
        views.FamousSayingsRandomResultList.as_view(), 
        name='famous-saying-random-result-list',
    ),
    # (PK)
    path(
        'famous-saying/<int:pk>/', 
        views.FamousSayingsPk.as_view(), 
        name='famous-saying-pk',
    ),
    # (Search)
    path(
        'famous-sayings/search/<str:searchstring>/', 
        views.FamousSayingsSearchList.as_view(),
        name="famous-sayings-search-list",
    ),
 
    
    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 4) Categories Books *** #
    # (List) -book
    path(
        'category-book/list/', 
        views.CategoryBookList.as_view(), 
        name='category-book-list',
    ),
    # (List App)
    path(
        'category-book/list-app/', 
        views.CategoryBookListApp.as_view(), 
        name='category-book-list-app',
    ),
    # (List Admin)
    path(
        'category-book/list-admin/', 
        views.CategoryBookListAdmin.as_view(), 
        name='category-book-list-admin',
    ),
    # (List Result)
    path(
        'category-book/result/',  #?result=9
        views.CategoryBookResultList.as_view(), 
        name='category-book-result-list',
    ),
    # (PK)
    path(
        'category-book/<int:pk>/', 
        views.CategoryBookPK.as_view(), 
        name='category-book-pk',
    ),
    # (Search)
    path(
        'category-book/search/<str:searchstring>/', 
        views.CategoryBookSearchList.as_view(), 
        name='category-book-search-list',
    ),
   
    


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Book)
    # (List)
    path(
        'book/list/', 
        views.BookList.as_view(), 
        name='book-list',
    ),
    # (List App)
    path(
        'book/list-app/', 
        views.BookListApp.as_view(), 
        name='book-list-app',
    ),
    # (List Admin)
    path(
        'book/list-admin/', 
        views.BookListAdmin.as_view(), 
        name='book-list-admin',
    ),
    # (List Result)
    path(
        'book/result/',  #?result=9
        views.BookResultList.as_view(), 
        name='book-result-list',
    ),
    # (PK)
    path(
        'book/<int:pk>/', 
        views.BookPk.as_view(), 
        name='book-pk',
    ),
    # (Search)
    path(
        'book/search/<str:searchstring>/', 
        views.BooksSearchList.as_view(),
        name="book-search-list",
    ),

    
 

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 7) Proofreading Service *** #
    # (List) 
    path(
        'proofreading-service/list/', 
        views.ProofreadingServiceList.as_view(), 
        name='proofreading-service-list',
    ),
    # (List App)
    path(
        'proofreading-service/list-app/', 
        views.ProofreadingServiceListApp.as_view(), 
        name='proofreading-service-list-app',
    ),
    # (List Admin)
    path(
        'proofreading-service/list-admin/', 
        views.ProofreadingServiceListAdmin.as_view(), 
        name='proofreading-service-list-admin',
    ),
    # (List Result)
    path(
        'proofreading-service/result/',  #?result=9
        views.ProofreadingServiceResultList.as_view(), 
        name='proofreading-service-result-list',
    ),
    # (PK)
    path(
        'proofreading-service/<int:pk>/', 
        views.ProofreadingServicePK.as_view(), 
        name='proofreading-service-pk',
    ),
    # (Search)
    path(
        'proofreading-services/search/<str:searchstring>/', 
        views.ProofreadingServicesSearchList.as_view(),
        name="proofreading-services-search-list",
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 8) Powerpoint *** #
    # (List) 
    path(
        'powerpoint/list/', 
        views.PowerpointList.as_view(), 
        name='powerpoint-list',
    ),
    # (List App)
    path(
        'powerpoint/list-app/', 
        views.PowerpointListApp.as_view(), 
        name='powerpoint-list-app',
    ),
    # (List Admin)
    path(
        'powerpoint/list-admin/', 
        views.PowerpointListAdmin.as_view(), 
        name='powerpoint-list-admin',
    ),
    # (List Result)
    path(
        'powerpoint/result/',  #?result=9
        views.PowerpointResultList.as_view(), 
        name='powerpoint-result-list',
    ),
    # (PK)
    path(
        'powerpoint/<int:pk>/', 
        views.PowerpointPk.as_view(), 
        name='powerpoint-pk',
    ),
    # (Search)
    path(
        'powerpoints/search/<str:searchstring>/', 
        views.PowerpointsSearchList.as_view(),
        name="powerpoint-search-list",
    ),


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 9) Powerpoint  *** #
    path(
        'student-enroll-powerpoint/list/', 
        views.StudentEnrollPowerpointList.as_view(),
        name="student-enroll-powerpoint-list",
    ),
    path(
        'student-enroll-powerpoint/<int:pk>/', 
        views.StudentEnrollPowerpointPK.as_view(),
        name="student-enroll-powerpoint-pk",
    ),

    path(
        'student-enroll-powerpoint/', 
        views.StudentEnrollPowerpointList.as_view(),
        name="student-enroll-powerpoint",
    ),
    
    path(
        'fetch-enroll-status/<int:student_id>/<int:powerpoint_id>/', 
        # views.fetch_enroll_status,
        views.FetchEnrollStatusPowerpointView.as_view(),
        name="fetch-enroll-status-student_id-powerpoint_id",
    ),

    #- 
    path(
        'fetch-enrolled-students/<int:powerpoint_id>/', 
        views.EnrolledStuentPowerpointList.as_view(),
        name="fetch-enrolled-students-powerpoint_id",
    ),

    path(
        'fetch-all-enrolled-students/<int:teacher_id>/', 
        views.EnrolledAllStuentPowerpointList.as_view(),
        name="fetch-all-enrolled-students-teacher_id",
    ),

    path(
        'fetch-enrolled-powerpoints/<int:student_id>/', 
        views.EnrolledStuentPowerpointPkList.as_view(),
        name="fetch-enrolled-powerpoints-student_id",
    ),

    path(
        'fetch-recomemded-powerpoints/<int:student_id>/', 
        views.EnrolledRecomemdedStuentPowerpointList.as_view(),
        name="fetch-recomemded-powerpoints-student_id",
    ),

    
    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 7) Powerpoint Service *** #
    # (List) 
    path(
        'powerpoint-service/list/', 
        views.PowerpointServiceList.as_view(), 
        name='powerpoint-service-list',
    ),
    # (List App)
    path(
        'powerpoint-service/list-app/', 
        views.PowerpointServiceListApp.as_view(), 
        name='powerpoint-service-list-app',
    ),
    # (List Admin)
    path(
        'powerpoint-service/list-admin/', 
        views.PowerpointServiceListAdmin.as_view(), 
        name='powerpoint-service-list-admin',
    ),
    # (List Result)
    path(
        'powerpoint-service/result/',  #?result=9
        views.PowerpointServiceResultList.as_view(), 
        name='powerpoint-service-result-list',
    ),
    # (PK)
    path(
        'powerpoint-service/<int:pk>/', 
        views.PowerpointServicePK.as_view(), 
        name='powerpoint-service-pk',
    ),
    # (Search)
    path(
        'powerpoints-services/search/<str:searchstring>/', 
        views.PowerpointsServicesSearchList.as_view(),
        name="powerpoints-services-search-list",
    ),

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** 4) Category Blogs *** #
    # (List)
    path(
        'category-blog/list/', 
        views.CategoryBlogListView.as_view(), 
        name='category-blog-list',
    ),
    # (List App)
    path(
        'category-blog/list-app/', 
        views.CategoryBlogListApp.as_view(), 
        name='category-blog-list-app',
    ),
    # (List Admin)
    path(
        'category-blog/list-admin/', 
        views.CategoryBlogListAdmin.as_view(), 
        name='category-blog-list-admin',
    ),
    # (List Result)
    path(
        'category-blog/result/',  #?result=9
        views.CategoryBlogResultList.as_view(), 
        name='category-blog-result-list',
    ),
    # (PK)
    path(
        'category-blog/<int:pk>/', 
        views.CategoryBlogPkAPIView.as_view(), 
        name='category-blog-pk',
    ),
    # (PK Like)
    path(
        'category-blog/<int:pk>/like/', 
        # views.CategoryBlogPkAPIView.as_view({'post': 'like'}),
        views.CategoryBlogPKLike.as_view(),
        name='category-blog-pk-like',
    ),
    # (Search)
    path(
        'category-blogs/search/<str:searchstring>/', 
        views.CategoryBlogSearchList.as_view(),
        name="category-blogs-search-list",
    ),




    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Blog)
    # (List)
    path(
        'blog/list/', 
        views.BlogListView.as_view(), 
        name='blog-list',
    ),
    # (List App)
    path(
        'blog/list-app/', 
        views.BlogListApp.as_view(), 
        name='blog-list-app',
    ),
    # (List Admin)
    path(
        'blog/list-admin/', 
        views.BlogListAdmin.as_view(), 
        name='blog-list-admin',
    ),
    # (List Result)
    path(
        'blog/result/',  #?result=9
        views.BlogResultList.as_view(), 
        name='blog-result-list',
    ),
    # (PK)
    path(
        'blog/<int:pk>/', 
        views.BlogPkAPIView.as_view(), 
        name='blog-pk',
    ),
    # (Pk Like)
    path(
        'blog/<int:pk>/like/', 
        # views.BlogPkAPIView.as_view({'post': 'like'}),
        views.BlogPKLike.as_view(),
        name='blog-pk-like',
    ),
    # (Search)
    path(
        'blogs/search/<str:searchstring>/', 
        views.BlogsSearchList.as_view(),
        name="blogs-search-list",
    ), 


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Comment)
    # (List)
    path(
        'comment-blog/list/', 
        views.CommentBlogListView.as_view(), 
        name='comment-blog-list',
    ),
    # (PK)
    path(
        'comment-blog/<int:pk>/', 
        views.CommentBlogPKAPIView.as_view(), 
        name='comment-blog-pk',
    ),
    # (PK Like)
    path(
        'comment-blog/<int:pk>/like/', 
        # views.CommentBlogPKAPIView.as_view({'post': 'like'}),
        views.CommentBlogPKLike.as_view(),
        name='comment-blog-pk-like',
    ),
    


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Reply)
    # (List)
    path(
        'replies-blog/list/', 
        views.ReplyBlogListView.as_view(), 
        name='reply-blog-list',
    ),
    # (PK)
    path(
        'replies-blog/<int:pk>/', 
        views.ReplyBlogPKAPIView.as_view(), 
        name='reply-blog-pk',
    ),
    # (PK Like)
    path(
        'replies-blog/<int:pk>/like/',
        # views.ReplyBlogPKAPIView.as_view({'post': 'like'}),
        views.ReplyBlogPKLike.as_view(),
        name='reply-blog-pk-like',
    ),
    
    

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Notifications)
    # (List)
    path(
        'notifications-blog/list/', 
        views.NotificationBlogListView.as_view(), 
        name='notification-blog-list',
    ),
    # (PK)
    path(
        'notifications-blog/<int:pk>/', 
        views.NotificationBlogPKAPIView.as_view(), 
        name='notification-blog-pk',
    ),
    


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (Reports)
    # (List)
    path(
        'reports-blog/list/', 
        views.ReportBlogListView.as_view(), 
        name='report-blog-list',
    ),
    # (PK)
    path(
        'reports-blog/<int:pk>/', 
        views.ReportBlogListView.as_view(), 
        name='report-blog-pk',
    ),



    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # (YouTube Suggestions Blog)
    # (List)
    path(
        'youTube-suggestions-blog/list/', 
        views.YouTubeSuggestionsBlogList.as_view(), 
        name='youTube-suggestions-blog-list',
    ),
    # (List Appp)
    path(
        'youTube-suggestions-blog/list-app/', 
        views.YouTubeSuggestionsBlogListApp.as_view(), 
        name='youTube-suggestions-blog-list-app',
    ),
    # (List Admin)
    path(
        'youTube-suggestions-blog/list-admin/', 
        views.YouTubeSuggestionsBlogListAdmin.as_view(), 
        name='youTube-suggestions-blog-list-admin',
    ),
    # (PK)
    path(
        'youTube-suggestions-blog/<int:pk>/', 
        views.YouTubeSuggestionsBlogPK.as_view(), 
        name='youTube-suggestions-blog-pk',
    ),
    # (List Result)
    path(
        'youTube-suggestions-blog/result/',  #?result=9
        views.YouTubeSuggestionsBlogResultList.as_view(), 
        name='blog-result-list',
    ),
    # (Search)
    path(
        'youTube-suggestions-blog/search/<str:searchstring>/', 
        views.YouTubeSuggestionsBlogSearchList.as_view(),
        name="blogs-search-list",
    ), 

    

    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # ================================================================
    # *** 1) ContactUs *** #
    # (List)
    path(
        "contactus-user/list/",
        views.ContactUsListAPIView.as_view(),
        name="contactus-list",
    ),
    # (PK)
    path(
        "contactus-user/<int:pk>/",
        views.ContactUsPKAPIView.as_view(),
        name="contactus-details-pk",
    ),
    # (Search)
    path(
        'contactus-user/search/<str:searchstring>/', 
        views.ContactusUserSearchList.as_view(),
        name="contactus-user-search-list",
    ),




    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # ================================================================
    # *** 2) Review *** #
    # (List)
    path(
        "review-user/list/",
        views.ReviewUserListAPIView.as_view(),
        name="review-user-list",
    ),
    # (List App)
    path(
        "review-user/list-app/",
        views.ReviewUserListApp.as_view(),
        name="review-user-list",
    ),
    # (List Result)
    path(
        "review-user/result/", #?result=5
        views.ReviewUserResultList.as_view(),
        name="review-user-list",
    ),
    # (PK)
    path(
        "review-user/<int:pk>/",
        views.ReviewUserPKAPIView.as_view(),
        name="review-user-details-pk",
    ),
    # (Search)
    path(
        'review-user/search/<str:searchstring>/', 
        views.ReviewUserSearchList.as_view(),
        name="review-user-search-list",
    ),




    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================
    # *** ) Stats *** #
    # (App)
    path(
        'app-stats/',
        views.AppStatsView.as_view(), 
        name='app-stats',
    ),
    # (Admin)
    path(
        'admin-dashboard-stats/', # ?user_id=1/
        views.AdminDashboardStatsView.as_view(), 
        name='admin-dashboard-stats',
    ),
    # (Teacher)
    path(
        'teacher-dashboard-stats/', # ?user_id=1/
        views.TeacherDashboardStatsView.as_view(), 
        name='teacher-dashboard-stats',
    ),
    # (Student)
    path(
        'student-dashboard-stats/', # ?user_id=1/
        views.StudentDashboardStatsView.as_view(), 
        name='student-dashboard-stats',
    ),


 


    path(
        '---------------------------------------------------------------------------------------------------------------/', 
        views.Space.as_view(),
    ),
    # =================================================================

 


]
