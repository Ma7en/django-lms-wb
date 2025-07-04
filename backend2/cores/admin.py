# 
from django.contrib import admin


# 
# from backend2.cores import models
# from cores import models
from . import models




# ******************************************************************************
# ==============================================================================
# *** Category & Section *** #
admin.site.register(models.CategorySection)
admin.site.register(models.SectionCourse)




# ******************************************************************************
# ==============================================================================
# *** Course *** #
admin.site.register(models.Course)
admin.site.register(models.SectionInCourse)
admin.site.register(models.LessonInCourse)
admin.site.register(models.StudentAnswerInCourse)
admin.site.register(models.FileInCourse)
admin.site.register(models.QuestionInCourse)



# ******************************************************************************
# ==============================================================================
# *** Coupon Course *** #
admin.site.register(models.CouponCourse)



# ******************************************************************************
# ==============================================================================
# *** Package Course *** #
admin.site.register(models.PackageCourse)
admin.site.register(models.PackageCourseDiscount)





# ******************************************************************************
# ==============================================================================
# *** Student Course *** #
admin.site.register(models.StudentCourseEnrollment)
admin.site.register(models.CourseRating)
admin.site.register(models.StudentFavoriteCourse)




# ******************************************************************************
# ==============================================================================
# *** Teacher Student Chat *** #
admin.site.register(models.TeacherStudentChat)






# ******************************************************************************
# ==============================================================================
# *** Student Progress Course *** #
admin.site.register(models.LessonInCourseCompletion)
admin.site.register(models.CourseProgress)






# ******************************************************************************
# ==============================================================================
# *** Student Certificate *** #
admin.site.register(models.StudentCertificate)





# ******************************************************************************
# ==============================================================================
# *** Question Bank *** #
# admin.site.register(models.QuestionBank)
# admin.site.register(models.QuestionInBank)
# admin.site.register(models.ChoiceQuestionInBank) 

# 
class ChoiceInline(admin.TabularInline):
    model = models.ChoiceQuestionInBank
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text', 'question_bank')
    search_fields = ('text',)
    list_filter = ('question_bank',)

class QuestionInline(admin.TabularInline):
    model = models.QuestionInBank
    extra = 0
    show_change_link = True

class QuestionBankAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('title', 'section', 'question_count', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('section',)
 
# admin.site.register(models.QuestionBank, QuestionBankAdmin)
# admin.site.register(models.QuestionInBank, QuestionAdmin)
admin.site.register(models.QuestionBank)
admin.site.register(models.QuestionInBank)
admin.site.register(models.ChoiceQuestionInBank)
admin.site.register(models.StudentQuestionBankResult)
# admin.site.register(models.StudentQuestionBankAnswer)




# ******************************************************************************
# ==============================================================================
# *** Famous Sayings *** #
admin.site.register(models.FamousSayings)




# ******************************************************************************
# ==============================================================================
# *** Books *** #
admin.site.register(models.CategoryBook)
admin.site.register(models.Book)




# ******************************************************************************
# ==============================================================================
# *** ProofreadingService *** #
admin.site.register(models.ProofreadingService)




# ******************************************************************************
# ==============================================================================
# *** Powerpoint *** #
admin.site.register(models.Powerpoint)
admin.site.register(models.StudentPowerpointEnrollment)
admin.site.register(models.PowerpointService)




# ******************************************************************************
# ==============================================================================
# *** Blogs *** #
admin.site.register(models.CategoryBlog)
admin.site.register(models.Blog)
admin.site.register(models.CommentBlog)
admin.site.register(models.ReplyBlog)
admin.site.register(models.NotificationBlog)
admin.site.register(models.ReportBlog) 




# ******************************************************************************
# ==============================================================================
# *** Quran School *** #
admin.site.register(models.InterviewDate)

admin.site.register(models.QuranPath)

admin.site.register(models.ClassRoom)
admin.site.register(models.ReviewLevel)

admin.site.register(models.ChapterInQuran)

admin.site.register(models.QuranCircle)
admin.site.register(models.DegreeQuranCircle)

admin.site.register(models.LiveQuranCircle)

admin.site.register(models.QuranExam)
admin.site.register(models.DegreeQuranExam)

admin.site.register(models.PresenceAndAbsence)
admin.site.register(models.DegreePresenceAndAbsence)

admin.site.register(models.FileAndLibrary)
admin.site.register(models.TeacherNote)
admin.site.register(models.CertificateQuran)

admin.site.register(models.StudentQuranSchoolEnrollment)







# ******************************************************************************
# ==============================================================================
# *** Contact & Review *** #
admin.site.register(models.ContactUsUser)
admin.site.register(models.ReviewUser)






# ******************************************************************************
# ==============================================================================
# admin.site.register(models.Post)
# admin.site.register(models.Comment)
# admin.site.register(models.Reply)
# admin.site.register(models.Notification)
# admin.site.register(models.Report)






# ******************************************************************************
# ==============================================================================