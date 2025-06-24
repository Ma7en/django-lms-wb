#
import shortuuid
import json



#
from django.db import models
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator



# 
from accounts.models import *
# from backend2.accounts.models import *



# Create your models here.



# ******************************************************************************
# ==============================================================================
# *** Category Section *** #
class CategorySection(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='category_section',
    )

    title = models.CharField(max_length=1_000)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )
    
    image = models.ImageField(
        upload_to="categorysection/images", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    def total_section_course(self):
        return SectionCourse.objects.filter(category=self).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="1-1. Categories Sections"

    def __str__(self) :
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(CategorySection, self).save(*args, **kwargs)
    



# ******************************************************************************
# ==============================================================================
# *** Section Course *** #
class SectionCourse(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='section_course',
    )
    category = models.ForeignKey(
        CategorySection, 
        on_delete=models.CASCADE, 
        related_name='category_section_course',
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=1_000)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )
    grade = models.CharField(
        max_length=1_000,
        null=True, 
        blank=True,
    )
    
    image = models.ImageField(
        upload_to="sectioncourse", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_course(self):
        return Course.objects.filter(section=self).count()

    def total_question_bank(self):
        return QuestionBank.objects.filter(section=self).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="1-2. Section Course"

    def __str__(self):
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(SectionCourse, self).save(*args, **kwargs)




# ******************************************************************************
# ==============================================================================
# *** Course *** #
class Course(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses',
    )
    # admin_profile = models.ForeignKey(
    #     AdminProfile,
    #     on_delete=models.CASCADE,
    #     related_name="admin_profile_course",
    #     null=True,
    #     blank=True,
    # )
    # teacher_profile = models.ForeignKey(
    #     TeacherProfile,
    #     on_delete=models.CASCADE,
    #     related_name="teacher_profile_course",
    #     null=True,
    #     blank=True,
    # )
    section = models.ForeignKey(
        SectionCourse, 
        on_delete=models.CASCADE, 
        related_name='section_course',
    )

    STATUS_CHOICES = (
        ("in_progress", "جاري العمل"),
        ("updated", "يتم التحديث"),
        ("complete", "مكتمل"), 
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="in_progress",
        null=True,
        blank=True,
    )
    
    LEVEL_CHOICES = [
        ('beginner', 'مبتدئ'),
        ('intermediate', 'متوسط'),
        ('advanced', 'متقدم'),
    ]
    level = models.CharField(
        max_length=1_000,
        choices=LEVEL_CHOICES, # edithere
        default="beginner",
        null=True, 
        blank=True,
    )

    title = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)
    image = models.ImageField(upload_to="course/images", null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)

    # 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # 
    price_like_egypt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_like_egypt = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    price_like_saudi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_like_saudi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    price_like_america = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_like_america = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    # 
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reviews_count = models.PositiveIntegerField(default=0)
    students_count = models.PositiveIntegerField(default=0)
    
    # 
    # lesson_count = models.PositiveIntegerField(default=0)
    # students_count = models.PositiveIntegerField(default=0)

    # 
    # progress = models.PositiveIntegerField(default=0)
    # rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    # reviews_count = models.PositiveIntegerField(default=0)
    
    language = models.CharField(max_length=1_000, null=True, blank=True)
    tag = models.TextField(max_length=1_000, null=True, blank=True)
    techs = models.TextField(max_length=10_000, null=True, blank=True)

    # 
    table_contents  = models.JSONField(default=list)

    # 
    features = models.JSONField(default=list, null=True, blank=True)
    requirements = models.JSONField(default=list, null=True, blank=True)
    target_audience = models.JSONField(default=list, null=True, blank=True)

    # 
    is_live = models.BooleanField(default=False)
    start_data = models.DateTimeField(null=True, blank=True) 
    end_data = models.DateTimeField(null=True, blank=True) 
    time_at = models.CharField(max_length=1_000, null=True, blank=True)

    is_visible = models.BooleanField(default=True)
 
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    def teach_list(self):
        if self.techs:
            teach_list = self.techs.split(',')
            return teach_list
        return self.techs

    def total_section(self):
        return SectionInCourse.objects.filter(course=self).count()


    def total_lesson(self):
        return LessonInCourse.objects.filter(section__course=self).count()


    def total_enrolled_students(self):
        return StudentCourseEnrollment.objects.filter(course=self).count()


    def course_rating(self):
        course_rating = CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
        return course_rating['avg_rating']

    # 
    # old code 
    # @property
    # def lessons_count(self):
    #     count = 0
    #     for section in self.sections.all():
    #         count += section.items.count()
    #     return count
    # @property
    # def lessons_count(self):
    #     return sum(section.items.count() for section in self.sections.all())
    

    # @property
    # def students_count(self):
    #     return self.student_progress.count()
    
    # 
    # old code
    # @property
    # def price_after_discount(self):
    #     """Calculate original price before discount"""
    #     if self.discount > 0:
    #         original = self.price - self.discount
    #         return original
    #     return self.price
    # @property

    def price_after_discount(self):
        return self.price - self.discount

    def price_after_discount_egypt(self):
        return self.price_like_egypt - self.discount_like_egypt

    def price_after_discount_saudi(self):
        return self.price_like_saudi - self.discount_like_saudi

    def price_after_discount_america(self):
        return self.price_like_america - self.discount_like_america
    

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "1-3. Courses"

    def __str__(self):
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(Course, self).save(*args, **kwargs)



class SectionInCourse(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='course_sections',
    )

    title = models.CharField(max_length=1_000)

    is_visible = models.BooleanField(default=True) #
    is_free = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "1-4. Section In Course"
    
    def total_lesson(self):
        return LessonInCourse.objects.filter(section=self).count()

    def __str__(self):
        return f"{self.id}): ({self.title}) - ({self.is_visible})"



class LessonInCourse(models.Model):
    section = models.ForeignKey(
        SectionInCourse,
        on_delete=models.CASCADE,
        related_name='section_lesson',
    )

    LESSON_TYPES_CHOICES = (
        ('video', 'Video'),
        ('assessment', 'Assessment'),
        ('document', 'Document'),
    )
    type = models.CharField(
        max_length=1_000, 
        choices=LESSON_TYPES_CHOICES,
        default="video",
        null=True,
        blank=True,
    )
   
    title = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)
    duration = models.CharField(max_length=1_000, null=True, blank=True)

    # 
    warning_message_user =  models.CharField(max_length=1_000, null=True, blank=True)
    rush_watch_lessons =  models.CharField(max_length=1_000, null=True, blank=True)


    # For Video Lessons
    video_file = models.FileField(upload_to="course/lesson/videos", null=True, blank=True)
    video_url = models.URLField(max_length=10_000, null=True, blank=True)

    # For Question Lessons
    questions = models.JSONField(default=list)

    # For Question Google Form
    questions_google_iframe = models.TextField(max_length=10_000, null=True, blank=True)
    questions_google_url = models.URLField(max_length=10_000, null=True, blank=True)

    # For Document Lessons
    content = models.TextField(max_length=10_000, null=True, blank=True)

    # For Files Lessons
    uploaded_files  = models.JSONField(default=list)

    # Answer form
    answer_form_pdf = models.FileField(upload_to="course/lesson/answer/pdf", null=True, blank=True)
    answer_form_pdf_url = models.URLField(max_length=10_000, null=True, blank=True)

    is_visible = models.BooleanField(default=True) #
    is_free = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "1-5. Lesson In Course"

    def __str__(self):
        return f"{self.id}): [{self.section.course.title}] - [{self.section.title}] - ({self.title}) - ({self.is_visible})"



class StudentAnswerInCourse(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_answer_in_course_student',
    )
    lesson = models.ForeignKey(
        LessonInCourse,
        on_delete=models.CASCADE,
        related_name='student_answer_in_course_lesson',
    )
    
    STATUS_CHOICES = (
        ("new", "جديد"),
        ("under-processing", "قيد المعالجة"),
        ("reply", "تم الرد"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="new",
    )
    
    # Answer form
    # answer = models.FileField(upload_to="course/lesson/studentanswer", null=True, blank=True)
    # answer_url = models.URLField(max_length=10_000, null=True, blank=True) 

    uploaded_files  = models.JSONField(default=list)
    degree = models.CharField(max_length=1_000, null=True, blank=True)

    is_visible = models.BooleanField(default=True)
 
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True) 


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "1-6. Student Answer In Course"

    def __str__(self):
        return f"{self.id}): [{self.student}] - [{self.lesson}]- ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.created_at) + "-" + shortuuid.uuid()[:2]
        super(StudentAnswerInCourse, self).save(*args, **kwargs)




class FileInCourse(models.Model):
    lesson = models.ForeignKey(
        LessonInCourse,
        on_delete=models.CASCADE,
        related_name='file_in_course_lesson',
    )

    name = models.CharField(max_length=1_000, null=True, blank=True)
    file = models.FileField(upload_to="course/lesson/file", null=True, blank=True)
    size = models.PositiveIntegerField(default=0, null=True, blank=True)
    file_type = models.CharField(max_length=1_000, null=True, blank=True)
    
    title = models.CharField(max_length=1_000)
    file_url = models.URLField(null=True, blank=True)

    type = models.CharField(max_length=1_000, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "1-7. File In Course"

    def __str__(self):
        return f"{self.id}): ({self.name})"


class QuestionInCourse(models.Model):
    lesson = models.ForeignKey(
        LessonInCourse,
        on_delete=models.CASCADE,
        related_name='lesson_question',
    )

    QUESTION_TYPES_CHOICES = (
        ('text', 'نص'),
        ('image-url', 'صورة من رابط'),
        ('image-upload', 'صورة مرفوعة'),
    )
    question_type = models.CharField(
        max_length=100, 
        choices=QUESTION_TYPES_CHOICES,
        default="text",
    )
    
    text = models.TextField(max_length=10_000, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to="course/question/images", null=True, blank=True)

    # image_file = models.JSONField(null=True, blank=True)
    
    choices = models.JSONField(default=list)
    correct_answer = models.PositiveIntegerField(default=0)
    
    order = models.PositiveIntegerField(default=0)
    
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_options(self):
        if isinstance(self.options, str):
            return json.loads(self.options)
        return self.options or []

    class Meta:
        ordering = ['created_at']
        verbose_name_plural="1-8. Question In Course"

    def __str__(self):
        return f"{self.id}): ({self.lesson.title}) - ({self.text[:50]})"




# ******************************************************************************
# ==============================================================================
# ***   *** #

 




# ******************************************************************************
# ==============================================================================
# *** Coupon Course *** #
class CouponCourse(models.Model):
    """Coupon model for course discounts"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='coupon_course',
    )

    name = models.CharField(max_length=1_000, unique=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )

    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="1-8. Coupon Course"

    def __str__(self):
        return f"{self.id}): ({self.name}) - ({self.discount}) - ({self.is_visible})"






# ******************************************************************************
# ==============================================================================
# ***  Packages Course  *** #
class PackageCourse(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='package_course_user',
    )

    title = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    price_after_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    courses = models.JSONField(default=list)    
    
    image = models.ImageField(
        upload_to="packagecourse/images", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
 
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "1-9. Package Course"

    def __str__(self):
        return f"{self.id}): ({self.title})  - [{self.user}] - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(PackageCourse, self).save(*args, **kwargs)




# ******************************************************************************
# ==============================================================================
# *** PackageCourseDiscount *** #
class PackageCourseDiscount(models.Model):
    # number = models.IntegerField(default=0)
    number = models.PositiveIntegerField(default=0)

    class Meta: 
        verbose_name_plural = "1-10. Package Course Discount"

    def __str__(self):
        return f"{self.id}): ({self.number})"




# ******************************************************************************
# ==============================================================================
# *** Student Course Enrollment *** #
class StudentCourseEnrollment(models.Model):
    student = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='enrolled_student',
    )
    course = models.ForeignKey(
        Course,
        null=True,
        on_delete=models.CASCADE,
        related_name='enrolled_courses',
    )

    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        null=True,
        blank=True,
    )

    enrolled_time = models.DateTimeField(auto_now_add=True)

    payment_id = models.CharField(max_length=1_000, null=True, blank=True)
    
    completed = models.BooleanField(default=False)  # إضافة حقل للإكمال
    completion_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # تاريخ الإكمال
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True) # unique=True

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        ordering = ['-created_at']
        verbose_name_plural="1-9. Student Enrolled Courses"

    def __str__(self) :
        return f"{self.id}): ({self.course.title}) - ({self.student})"







# ******************************************************************************
# ==============================================================================
# *** Course Rating *** #
class CourseRating(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
    )

    STATUS_CHOICES = (
        ("unacceptable", "مرفوض"), 
        ("under-processing", "قيد المعالجة"),
        ("publication", "منشور"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="unacceptable",
    )

    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(max_length=10_000, null=True, blank=True)
    review_time = models.DateTimeField(auto_now_add=True)

    is_visible = models.BooleanField(default=True)
    

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        ordering = ['-created_at']
        verbose_name_plural="1-10-. Course Ratings"

    def __str__(self):
        return f"{self.id}): ({self.course}) - ({self.student}) - ({self.rating})"







# ******************************************************************************
# ==============================================================================
# *** Student Favorite Course *** #
class StudentFavoriteCourse(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    is_visible = models.BooleanField(default=True)

    
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="1-11. Student Favorite Course"

    def __str__(self):
        return f"{self.id}): ({self.course}) - ({self.student})"






# ******************************************************************************
# ==============================================================================
# *** Teacher Student Chat *** #
class TeacherStudentChat(models.Model):
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_chats'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_chats'
    )

    msg_to=models.TextField()
    msg_from=models.CharField(max_length=10_000)
    msg_time=models.DateTimeField(auto_now_add=True)
    
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="1-12. Teacher Student ChatBot"

    def __str__(self):
        return f"{self.id}): [{self.teacher}] - [{self.student}]"







# ******************************************************************************
# ==============================================================================
# *** Student Progress Course *** #
# class StudentProgressCourse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='user_progress')
#     section = models.ForeignKey(SectionInCourse, on_delete=models.CASCADE, null=True, blank=True)
#     lesson = models.ForeignKey(LessonInCourse, on_delete=models.CASCADE, null=True, blank=True)
    
#     # حالة الإكمال
#     is_completed = models.BooleanField(default=False)
#     completed_at = models.DateTimeField(null=True, blank=True)
    
#     # تتبع المشاهدة/القراءة
#     progress_percentage = models.PositiveIntegerField(default=0)
#     last_accessed = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         unique_together = ('user', 'course', 'lesson')
#         ordering = ['-last_accessed']

#     def __str__(self):
#         return f"{self.user.email} - {self.course.title} ({self.progress_percentage}%)"



# ->
class LessonInCourseCompletion(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    lesson = models.ForeignKey(
        LessonInCourse, 
        on_delete=models.CASCADE,
    )

    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_accessed = models.DateTimeField(auto_now=True)
        
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name_plural="1-14. Lesson In Course Completion"
        
    def __str__(self):
        return f"{self.user.email} - {self.lesson.title}"


class CourseProgress(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
    )

    progress_percentage = models.FloatField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
        
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'course')
        verbose_name_plural="1-13. Course Progress"
         
    def update_progress(self):
        total_lessons = self.course.lessons_count()
        completed_lessons = LessonInCourseCompletion.objects.filter(
            user=self.user,
            lesson__section__course=self.course,
            is_completed=True
        ).count()
        
        self.progress_percentage = (completed_lessons / total_lessons) * 100 if total_lessons > 0 else 0
        self.save()





# ******************************************************************************
# ==============================================================================
# *** Student Certificate *** #
class StudentCertificate(models.Model):
    enrollment = models.OneToOneField(
        StudentCourseEnrollment,
        on_delete=models.CASCADE,
        related_name='certificate'
    )

    issued_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='course/certificates/', null=True, blank=True)
    
    issue_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(auto_now_add=True)
    certificate_pdf = models.FileField(upload_to='course/certificates/', null=True, blank=True)
    certificate_url = models.URLField(null=True, blank=True)
    verification_code = models.CharField(max_length=16, unique=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural="1-15. Student Certificate"
         
    def generate_verification_code(self):
        return str(uuid.uuid4().hex)[:16].upper()

    def __str__(self):
        return f"{self.id}): ({self.enrollment.student}) - ({self.enrollment.course})"
    
    def save(self, *args, **kwargs):
        if not self.verification_code:
            self.verification_code = self.generate_verification_code()
        super().save(*args, **kwargs)





# ******************************************************************************
# ==============================================================================
# *** Questions Banks *** #
class QuestionBank(models.Model):
    """Question bank model containing groups of questions"""
    # section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='question_banks')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='question_banks',
    )
    # admin_profile = models.ForeignKey(
    #     AdminProfile,
    #     on_delete=models.CASCADE,
    #     related_name="admin_profile_question_bank",
    #     null=True,
    #     blank=True,
    # )
    # teacher_profile = models.ForeignKey(
    #     TeacherProfile,
    #     on_delete=models.CASCADE,
    #     related_name="teacher_profile_question_bank",
    #     null=True,
    #     blank=True,
    # )
    section = models.ForeignKey(
        SectionCourse, 
        on_delete=models.CASCADE, 
        related_name='section_course_question_bank',
    )
    
    title = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)
    
    image = models.ImageField(upload_to='questionsbanks/banks/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def total_question_in_bank(self):
        return QuestionInBank.objects.filter(question_bank=self).count()


    def total_student_result(self):
        return StudentQuestionBankResult.objects.filter(question_bank=self).count()

    @property
    def question_count(self):
        return self.questions.count()
    
    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url
    

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="2-1) Questions Banks"
    
    
    def __str__(self):
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"
    


class QuestionInBank(models.Model):
    """Question model with text or image"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='question_in_bank',
    )
    question_bank = models.ForeignKey(
        QuestionBank, 
        on_delete=models.CASCADE, 
        related_name='questions_question_in_bank'
    )

    text = models.TextField(max_length=10_000, null=True, blank=True)
    
    image = models.ImageField(upload_to='questionsbanks/questions/', null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
        
    choices = models.JSONField(default=list)
    correct_answer = models.PositiveIntegerField(default=0)
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="2-2) Question In Bank"
    
    def __str__(self):
        return f"{self.id}): ({self.text[:50]}) - ({self.is_visible})"
    



class ChoiceQuestionInBank(models.Model):
    """Answer choices for questions"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='choice_question_in_bank',
    )
    question = models.ForeignKey(
        QuestionInBank, 
        on_delete=models.CASCADE, 
        related_name='choices_question_in_bank',
        # null=True,
        # blank=True,
    )

    text = models.CharField(max_length=1_000)
    is_correct = models.BooleanField(default=False)
        
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="2-3) Choice Question In Bank"

    def __str__(self):
        return f"{self.id}): ({self.text[:30]}) - ({self.is_correct})"














# ******************************************************************************
# ==============================================================================
# class StudentQuestionBankResult(models.Model):
#     user = models.ForeignKey(
#         User, 
#         on_delete=models.CASCADE,
#         related_name='student_question_bank_results',
#     )
#     question_bank = models.ForeignKey(
#         QuestionBank, 
#         on_delete=models.CASCADE,
#         related_name='question_bank_bank_result',
#     )

#     answered_questions = models.PositiveIntegerField()
#     correct_answers = models.PositiveIntegerField()
#     percentage = models.FloatField()
#     total_questions = models.PositiveIntegerField()


#     slug = models.SlugField(unique=True, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True)


#     class Meta:
#         ordering = ['-created_at']
#         verbose_name_plural="2-4) Student Question Bank Result"
   

#     def __str__(self):
#         return f"{self.id}): ({self.user}) - ({self.question_bank})"
    

# class StudentQuestionBankAnswer(models.Model):
#     question_bank_result = models.ForeignKey(
#         StudentQuestionBankResult, 
#         on_delete=models.CASCADE,
#         related_name='question_bank_answers', 
#     )

#     question_id = models.PositiveIntegerField()
#     question_text = models.TextField()

#     is_answered = models.BooleanField()
    
#     selected_choice_id = models.PositiveIntegerField(null=True, blank=True)
#     selected_choice_text = models.TextField(null=True, blank=True)
#     correct_choice_id = models.PositiveIntegerField(null=True, blank=True)
#     correct_choice_text = models.TextField(null=True, blank=True)
    
#     is_correct = models.BooleanField(null=True, blank=True)
#     all_choices = models.JSONField(default=list)

#     slug = models.SlugField(unique=True, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-created_at']
#         verbose_name_plural="2-5) Student Question Bank Answer"
   
#     def __str__(self):
#         return f"{self.id}): ({self.question_text})" 







# ******************************************************************************
# ==============================================================================
# ***  Student Question Bank Result  *** // 
class StudentQuestionBankResult(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='student_question_bank_results',
    )
    question_bank = models.ForeignKey(
        QuestionBank, 
        on_delete=models.CASCADE,
        related_name='question_bank_bank_result',
    )

    # answered_questions = models.PositiveIntegerField()
    
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    percentage = models.FloatField()

    results = models.JSONField(default=list)


    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="2-4) Student Question Bank Result"
   

    def __str__(self):
        return f"{self.id}): ({self.user}) - ({self.question_bank}) - [{self.user}]"
    


# ******************************************************************************
# ==============================================================================
# ***  Famous Sayings  *** #
class FamousSayings(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='famous_sayings_user',
    ) 


    title = models.CharField(max_length=1_000, null=True, blank=True)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )

    image = models.ImageField(
        upload_to="famoussayings/images", 
        null=True, 
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

   
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "5-1) Famous Sayings"

    def __str__(self):
        return f"{self.id}): ({self.title}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title)[:50] + "-" + shortuuid.uuid()[:2]
        super(FamousSayings, self).save(*args, **kwargs)








# ******************************************************************************
# ==============================================================================
# ***  Books  *** #
class CategoryBook(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='category_book_user',
    )

    title = models.CharField(max_length=1_000)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )
    
    image = models.ImageField(
        upload_to="categorybook/images", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    def total_book(self):
        return Book.objects.filter(category=self).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="6-1] Categories Books"

    def __str__(self) :
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(CategoryBook, self).save(*args, **kwargs)
    


class Book(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='book_user',
    )
    category = models.ForeignKey(
        CategoryBook, 
        on_delete=models.CASCADE, 
        related_name='book_category_book',
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=1_000, null=True, blank=True)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )

    image = models.ImageField(
        upload_to="books/images", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    file_word = models.FileField(upload_to="books/files/word", null=True, blank=True)
    file_word_url = models.URLField(max_length=10_000, null=True, blank=True)

    file_pdf = models.FileField(upload_to="books/files/pdf", null=True, blank=True)
    file_pdf_url = models.URLField(max_length=10_000, null=True, blank=True)


    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="6-2] Books"

    def __str__(self):
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(Book, self).save(*args, **kwargs)








# ******************************************************************************
# ==============================================================================
# ***   Proofreading Service   *** #
class ProofreadingService(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='proofreading_service_user',
    )
    
    STATUS_CHOICES = (
        ("new", "جديد"),
        ("under-processing", "قيد المعالجة"),
        ("reply", "تم الرد"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="new",
    )

    PROOFREADING_CHOICES = (
        ("total_formation", "تشكيل كلي"),
        ("end_words", "اواخر الكلمات"), 
    )
    type_proofreading = models.CharField(
        max_length=1_000, 
        choices=PROOFREADING_CHOICES, 
        default="total_formation",
    )

    number_page = models.PositiveIntegerField(default=0)
    receipt_period = models.CharField(max_length=1_000, null=True, blank=True)

    # EG 
    # phone_number = models.CharField(
    #     max_length=11,
    #     validators=[
    #         RegexValidator(
    #             regex="^01[0|1|2|5][0-9]{8}$",
    #             message="Phone must be start 010, 011, 012, 015 and all number contains 11 digits",
    #         )
    #     ],
    #     null=True,
    #     blank=True,
    # )
    # SR
    # phone_number = models.CharField(
    #     max_length=10,  # الأرقام السعودية تتكون من 10 أرقام (بدون +966)
    #     validators=[
    #         RegexValidator(
    #             regex=r'^(05)(5|0|3|6|4|9|1|8|7|2)([0-9]{7})$',
    #             message='يجب أن يبدأ رقم الهاتف بـ 05 ويحتوي على 10 أرقام صحيحة'
    #         )
    #     ],
    #     # verbose_name="رقم الجوال السعودي",
    #     null=True, 
    #     blank=True,
    # )
    # All
    phone_number = models.CharField(
        max_length=100,
        null=True, 
        blank=True,
    )

    # title = models.CharField(max_length=1_000)
    state = models.CharField(max_length=1_000)
    field_study = models.CharField(max_length=10_000)
 
    
    quick_reply = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="7-1. Proofreading Services"

    def __str__(self) :
        return f"{self.id}): [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.type_proofreading) + "-" + shortuuid.uuid()[:2]
        super(ProofreadingService, self).save(*args, **kwargs)
    




# ******************************************************************************
# ==============================================================================
# ***   Powerpoint   *** #
class Powerpoint(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='powerpoint_user',
    )

    # 
    title = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)
    image = models.ImageField(upload_to="powerpoint/images", null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    # 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # 
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reviews_count = models.PositiveIntegerField(default=0)
    students_count = models.PositiveIntegerField(default=0)

    # 
    file_powerpoint = models.FileField(upload_to="powerpoint/files", null=True, blank=True)
    file_powerpoint_url = models.URLField(max_length=10_000, null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def total_enrolled_students(self):
        return StudentPowerpointEnrollment.objects.filter(powerpoint=self).count()


    # def course_rating(self):
    #     course_rating = CourseRating.objects.filter(course=self).aggregate(avg_rating=models.Avg('rating'))
    #     return course_rating['avg_rating']
   
    
    def price_after_discount(self):
        return self.price - self.discount
    

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "8-1. Powerpoint"

    def __str__(self):
        return f"{self.id}): ({self.title}) - [{self.user}] - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug is None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(Powerpoint, self).save(*args, **kwargs)



class StudentPowerpointEnrollment(models.Model):
    student = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='student_Powerpoint_enrollment_user',
    )
    powerpoint = models.ForeignKey(
        Powerpoint,
        null=True,
        on_delete=models.CASCADE,
        related_name='student_powerpoint_enrollment_powerpoint',
    )

    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0,
        null=True,
        blank=True,
    )

    enrolled_time = models.DateTimeField(auto_now_add=True)

    payment_id = models.CharField(max_length=1_000, null=True, blank=True)
    
    completed = models.BooleanField(default=False)  # إضافة حقل للإكمال
    completion_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  # تاريخ الإكمال
    certificate_id = models.UUIDField(default=uuid.uuid4, editable=False, null=True, blank=True) # unique=True

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:        
        ordering = ['-created_at']
        verbose_name_plural="8-2. Student Powerpoint Enrollment"

    def __str__(self) :
        return f"{self.id}): ({self.powerpoint}) - ({self.student})"






# ******************************************************************************
# ==============================================================================
# ***   Powerpoint Service   *** #
class PowerpointService(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='powerpoint_service_user',
    )
    
    STATUS_CHOICES = (
        ("new", "جديد"),
        ("under-processing", "قيد المعالجة"),
        ("reply", "تم الرد"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="new",
    )

    mold_shape = models.CharField(max_length=1_000)
    description = models.TextField(max_length=10_000, null=True, blank=True)


    number_page = models.PositiveIntegerField(default=0)
    receipt_period = models.CharField(max_length=1_000, null=True, blank=True)

    phone_number = models.CharField(
        max_length=100,
        null=True, 
        blank=True,
    ) 
    
    quick_reply = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural="8-3. Proofreading Services"

    def __str__(self) :
        return f"{self.id}): [{self.user}] - ({self.is_visible})"
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.mold_shape) + "-" + shortuuid.uuid()[:2]
        super(PowerpointService, self).save(*args, **kwargs)
    





# ******************************************************************************
# ==============================================================================
# ***     *** #









# ******************************************************************************
# ==============================================================================
# ***  ContactUs  *** #
class ContactUsUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,        
        related_name='contactus_user',
        null=True,
        blank=True,
    )

    STATUS_CHOICES = (
        ("new", "جديد"),
        ("under-processing", "قيد المعالجة"),
        ("reply", "تم الرد"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="new",
    )

    full_name = models.CharField(max_length=1_000)
    email = models.EmailField()

    # EG
    # phone_number = models.CharField(
    #     max_length=11,
    #     validators=[
    #         RegexValidator(
    #             regex="^01[0|1|2|5][0-9]{8}$",
    #             message="Phone must be start 010, 011, 012, 015 and all number contains 11 digits",
    #         )
    #     ],
    #     null=True,
    #     blank=True,
    # )
    # SR
    # phone_number = models.CharField(
    #     max_length=10,  # الأرقام السعودية تتكون من 10 أرقام (بدون +966)
    #     validators=[
    #         RegexValidator(
    #             regex=r'^(05)(5|0|3|6|4|9|1|8|7|2)([0-9]{7})$',
    #             message='يجب أن يبدأ رقم الهاتف بـ 05 ويحتوي على 10 أرقام صحيحة'
    #         )
    #     ],
    #     # verbose_name="رقم الجوال السعودي",
    #     null=True, 
    #     blank=True,
    # )
    # All
    phone_number = models.CharField(
        max_length=100,
        null=True, 
        blank=True,
    )

    titleofmessage = models.CharField(max_length=1_000)
    message = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )

    quick_reply = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}): ({self.titleofmessage}) - ({self.status}) - ({self.is_visible})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "3-1] ContactUs"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.titleofmessage) + "-" + shortuuid.uuid()[:2]
        super(ContactUsUser, self).save(*args, **kwargs)







# ******************************************************************************
# ==============================================================================
# ***  Review  *** #
class ReviewUser(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviewuser_user',
    )
    profile = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='reviewuser_profile',
    )

    STATUS_CHOICES = (
        ("unacceptable", "مرفوض"), 
        ("under-processing", "قيد المعالجة"),
        ("publication", "منشور"),
    )
    status = models.CharField(
        max_length=1_000, 
        choices=STATUS_CHOICES, 
        default="publication",
        null=True,
        blank=True,
    )

    first_name = models.CharField(max_length=1_000)
    message = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )
    rating = models.PositiveBigIntegerField(default=0)
    # rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}): ({self.first_name}) - ({self.status}) - ({self.is_visible})"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "3-2] Review User"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.first_name) + "-" + shortuuid.uuid()[:2]
        super(ReviewUser, self).save(*args, **kwargs)










# ******************************************************************************
# ==============================================================================
# ***  Blogs  *** #
class CategoryBlog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='category_post',
    ) 

    title = models.CharField(max_length=1_000)
    description = models.TextField(
        max_length=10_000, 
        null=True, 
        blank=True,
    )

    image = models.ImageField(
        upload_to="categoryblog/images", 
        null=True, 
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    # view = models.IntegerField(default=0)
    view = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(
        User, 
        related_name="likes_category", 
        blank=True,
    )

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_blog(self):
        return Blog.objects.filter(category=self).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-1: Category Blog"

    def __str__(self):
        return f"{self.id}): ({self.title}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super(CategoryBlog, self).save(*args, **kwargs)



class Blog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='blog_user',
    )
    category = models.ForeignKey(
        CategoryBlog,
        on_delete=models.SET_NULL,
        null=True,
        related_name="blog_category",
    )

    title = models.CharField(max_length=1_000)
    summary = models.TextField(
        max_length=10_000,
        null=True,
        blank=True,
    )
    description = models.TextField(
        max_length=100_000,
        null=True,
        blank=True,
    )

    image = models.ImageField(
        upload_to="blogs/images", 
        null=True,
        blank=True,
    )
    image_url = models.URLField(null=True, blank=True)

    file_word = models.FileField(upload_to="blogs/files/word", null=True, blank=True)
    file_word_url = models.URLField(max_length=10_000, null=True, blank=True)

    file_pdf = models.FileField(upload_to="blogs/files/pdf", null=True, blank=True)
    file_pdf_url = models.URLField(max_length=10_000, null=True, blank=True)

    techs = models.TextField(max_length=10_000, null=True, blank=True)

    is_visible = models.BooleanField(default=True)

    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(
        User, 
        related_name='likes_blogs_user', 
        blank=True,
    )

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def teach_list(self):
        if self.techs:
            teach_list = self.techs.split(',')
            return teach_list
        return self.techs


    def total_comment(self):
        return CommentBlog.objects.filter(blog=self).count()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-2: Blog"

    def __str__(self):
        return f"{self.id}): ({self.title}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + shortuuid.uuid()[:2]
        super().save(*args, **kwargs)




class CommentBlog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comment_blog_user',
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE, 
        related_name='comment_blog_blog',
    )

    text = models.TextField(max_length=10_000)
    likes = models.ManyToManyField(
        User, 
        related_name='liked_comments', 
        blank=True,
    )
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-3: Comment Blog"

    def __str__(self):
        return f"{self.id}): ({self.user}) - ({self.text}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)




class ReplyBlog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='replies_blog_user',
    )
    comment = models.ForeignKey(
        CommentBlog, 
        on_delete=models.CASCADE, 
        related_name='replies_comment_blog',
    )

    text = models.TextField(max_length=10_000)
    likes = models.ManyToManyField(
        User, 
        related_name='liked_replies', 
        blank=True,
    )

    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "4-4: Reply Blog"

    def __str__(self):
        return f"{self.id}): ({self.user}) - ({self.text}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)




class NotificationBlog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications_blog_user',
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE, 
        related_name='notifications_blog_blog', 
        null=True, 
        blank=True,
    )
    comment = models.ForeignKey(
        CommentBlog, 
        on_delete=models.CASCADE, 
        related_name='notifications_blog_comment_blog', 
        null=True, 
        blank=True,
    )
    reply = models.ForeignKey(
        ReplyBlog, 
        on_delete=models.CASCADE, 
        related_name='notifications_blog_reply_blog', 
        null=True, 
        blank=True,
    )

    NOTIFICATION_TYPES = [
        ('like_post', 'أعجبني المقالاة'),
        ('like_comment', 'أعجبني التعليق'),
        ('like_reply', 'أعجبني الرد'),
        ('comment', 'تعليق'),
        ('reply', 'رد'),
        ('report', 'تقرير'),
    ]
    notification_type = models.CharField(
        max_length=100, 
        choices=NOTIFICATION_TYPES,
        null=True, 
        blank=True,
    )

    message = models.CharField(max_length=1_000)
    is_read = models.BooleanField(default=False)
    
    is_visible = models.BooleanField(default=True)

    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-5: Notification Blog"
    
    def __str__(self):
        return f"{self.id}): ({self.message}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)




class ReportBlog(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='reports_blog_user',
    )
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE, 
        related_name='reports_blog_blog',
    )

    REPORT_REASONS = [
        ('spam', 'رسائل إلكترونية مزعجة'),
        ('inappropriate', 'محتوى غير لائق'),
        ('harassment', 'مضايقة'),
        ('other', 'آخر'),
    ]
    reason = models.CharField(
        max_length=100, 
        choices=REPORT_REASONS,
    )

    details = models.TextField(max_length=10_000, blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
 
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-6: Report Blog"

    def __str__(self):
        return f"{self.id}): ({self.details}) - ({self.is_visible})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)







# ******************************************************************************
# ==============================================================================
# ***  YouTube Suggestions Blog *** #
class YouTubeSuggestionsBlog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='youTube_suggestions_user',
    )

    title = models.CharField(max_length=1_000)
    video_url = models.URLField(max_length=10_000, null=True, blank=True)
    
    is_visible = models.BooleanField(default=True)
 
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "4-7: YouTube Suggestions"

    def __str__(self):
        return f"{self.id}): ({self.title}) - ({self.is_visible})"






# ==============================================================================
# ***  *** #