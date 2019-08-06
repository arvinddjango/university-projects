from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class IndexBanner(models.Model):
    STATUS_CHOICES = (('active','Active'),('deactive','Deactive'))
    banner_img = models.ImageField(upload_to='banner_image/')
    banner_desc = models.CharField(max_length=256)
    banner_alt_txt = models.CharField(max_length=100)
    banner_img_txt1 = models.CharField(max_length=50)
    banner_img_txt2 = models.CharField(max_length=20)
    banner_btn_name =models.CharField(max_length=20)
    banner_created_date =models.DateTimeField(auto_now_add=True)
    banner_updated_date = models.DateTimeField(auto_now=True)
    banner_status = models.CharField(max_length=10,choices=STATUS_CHOICES,default=True)
    banner_active = models.BooleanField(default=True)

#To Delete image from folder
    def delete(self, *args, **kwargs):
        #self.name.delete()
        self.banner_img.delete()
        super().delete(*args, **kwargs)

class MoreDiscoverMenu(models.Model):
    menu_img = models.ImageField(upload_to='discover_menu_imgae/')
    menu_url = models.CharField(max_length=20)
    menu_btn = models.CharField(max_length=20)
    menu_created_date = models.DateTimeField(auto_now_add=True)
    menu_updated_date = models.DateTimeField(auto_now=True)

#To Delete image from folder
    def delete(self, *args,**kwargs):
        self.menu_img.delete()
        super().delete(*args, **kwargs)

class IndexHeadOne(models.Model):
    index_head = models.CharField(max_length=55)
    index_head_str = models.CharField(max_length=55)
    index_desc = models.CharField(max_length=200)
    index_created = models.DateTimeField(auto_now_add=True)
    index_updated = models.DateTimeField(auto_now=True)

class IndexHeadTwo(models.Model):
    index_head_two = models.CharField(max_length=55)
    index_head_two_str = models.CharField(max_length=55)
    index_desc_two = models.CharField(max_length=200)
    index_created_two = models.DateTimeField(auto_now_add=True)
    index_updated_two = models.DateTimeField(auto_now=True)




class PopularCourses(models.Model):
    popular_course_img = models.ImageField(upload_to='popular_course_images/')
    pupular_course_head = models.CharField(max_length=100)
    slug = models.SlugField(max_length=264, default='')
    pupular_course_subhead = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=20,default='')
    course_seat_total = models.CharField(max_length=10,default='')
    popular_course_desc = models.TextField(max_length=50000)
    popular_course_created = models.DateTimeField(auto_now_add=True)
    popular_course_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.pupular_course_head
    def get_absolute_url(self):
        return reverse('course_details', args=[self.slug])

#To Delete Image from folder
    def delete(self,*args,**kwargs):
        self.popular_course_img.delete()
        super().delete(*args,**kwargs)





class CoursComment(models.Model):
    popular_course = models.ForeignKey(PopularCourses,related_name='pcomments',on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# class Event(models.Model):
#     event_img = models.ImageField(upload_to='event_image/')
#     event_title = models.CharField(max_length=200)
#     event_desc = models.TextField(max_length=5000)
#     event_from = models.DateField(blank=True,default=True)
#     event_time_from = models.TimeField(blank=True,default=True)
#     event_time_to = models.TimeField(blank=True,default=True)
#     event_create = models.DateTimeField(auto_now_add=True)
#     event_updated = models.DateTimeField(auto_now_add=True)
#
# # To delete Image from folder
#     def delete(self, *args,**kwargs):
#         self.event_img.delete()
#         super().delete(*args,**kwargs)

class UpcomingEvent(models.Model):
    event_img = models.ImageField(upload_to='event_image/')
    event_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=264,default='')
    event_desc = models.TextField(max_length=5000)
    event_location = models.CharField(max_length=55,default='')
    event_from = models.DateField(blank=True, null=True)
    event_time_from = models.TimeField(blank=True, null=True)
    event_time_to = models.TimeField(blank=True, null=True)
    event_create = models.DateTimeField(auto_now_add=True)
    event_updated = models.DateTimeField(auto_now=True)

# To delete Image from folder
    def delete(self, *args,**kwargs):
        self.event_img.delete()
        super().delete(*args,**kwargs)
    def __str__(self):
        return self.event_title

    def get_absolute_url(self):
        return reverse('events_deatils', args=[self.slug])



class JobVacant(models.Model):
    job_img = models.ImageField(upload_to='job_image/')
    job_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=264,default='')
    job_desc = models.TextField(max_length=5000)
    job_location = models.CharField(max_length=50)
    job_opening = models.CharField(max_length=20,default='')
    job_position = models.CharField(max_length=100, default='')
    job_from = models.DateField(blank=True)
    job_time_from = models.TimeField(blank=True)
    job_time_to = models.TimeField(blank=True)
    job_create = models.DateTimeField(auto_now_add=True)
    job_updated = models.DateTimeField(auto_now=True)

# To delete Image from folder
    def delete(self, *args,**kwargs):
        self.job_img.delete()
        super().delete(*args,**kwargs)
    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('jobs_details', args=[self.slug])

class ImageGallery(models.Model):
    img_gallery = models.ImageField(upload_to='Image_Gallery/')
    img_caption = models.CharField(max_length=50)
    img_created = models.DateTimeField(auto_now_add=True)
    img_updated = models.DateTimeField(auto_now=True)

class Video(models.Model):
    video_title = models.CharField(max_length=50)
    video_desc = models.TextField(max_length=5000)
    videofile = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.video_title + ": " + str(self.videofile)

class AboutUs(models.Model):
    about_title_one = models.CharField(max_length=20)
    about_title_two = models.CharField(max_length=20)
    about_desc = models.TextField(max_length=5000)
    about_created = models.DateTimeField(auto_now_add=True)
    about_updated = models.DateTimeField(auto_now=True)

class Admission(models.Model):
    STATUS_CHOICES = (('Aerospace Engineering','Aerospace Engineering'),('Agriculture Courses','Agriculture Courses'),('Fashion Technology','Fashion Technology'),('Marine Engineering','Marine Engineering'),('Building, Construction Management','Building, Construction Management'),('Web Development','Web Development'),('Accountant course','Accountant course'),('Dot Net Development','Dot Net Development'),('Java Development','Java Development'),('Chemical Engineering','Chemical Engineering'))
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=13)
    email_id = models.EmailField()
    city = models.CharField(max_length=20)
    education = models.CharField(max_length=30)
    course = models.CharField(max_length=100,choices=STATUS_CHOICES,default='')

class AdmissionPage(models.Model):
    admission_title = models.CharField(max_length=30)
    admission_desc = models.TextField()
    admission_help =models.CharField(max_length=30)
    admission_help_no= models.CharField(max_length=15)

class Award(models.Model):
    award_title = models.CharField(max_length=30)
    award_desc = models.TextField()
    award_img = models.ImageField(upload_to='award_img/')
    award_date = models.DateField(blank=True)

    def __str__(self):
        return self.award_title

class AwardList(models.Model):
    award_title = models.ForeignKey(Award,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=264, default='')
    award_list_title = models.CharField(max_length=55)
    award_time_from = models.TimeField(blank=True)
    award_time_to = models.TimeField(blank=True)
    award_list_img = models.ImageField(upload_to='award_img/')
    award_list_desc = models.TextField()
    award_list_desc1 = models.TextField()

# stoping draft list in list.html
# class CustomManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='published')

class Blog(models.Model):
    STATUS_CHOICE = (('draft','Draft'),('published','published'))
    blog_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    blog_img = models.ImageField(upload_to='blog_imgage/')
    blog_desc = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    blog_created_date = models.DateTimeField(auto_now_add=True)
    blog_updated_date = models.DateTimeField(auto_now=True)
    blog_status = models.CharField(max_length=15,choices=STATUS_CHOICE,default='draft')
    #objects = CustomManager()

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blog_details',args=[self.slug])

class BlogComment(models.Model):
    comment = models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class BlogEmailShare(models.Model):
    comment = models.ForeignKey(Blog,related_name='blogshare',on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email_from = models.EmailField(default='')
    email_to = models.EmailField(default='')
    message = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class ShareCount(models.Model):
    blog_title = models.ForeignKey(Blog, related_name='commentcount', on_delete=models.CASCADE)
    nocount = models.PositiveIntegerField()



class Contact(models.Model):
    contact_title = models.CharField(max_length=200)
    contact_address = models.CharField(max_length=200)
    contact_phone = models.IntegerField()
    contact_mobile = models.IntegerField()
    contact_email = models.EmailField()
    contact_website = models.CharField(max_length=50,blank=True)
    contact_facebook = models.CharField(max_length=50,blank=True)
    contact_blog = models.CharField(max_length=50,blank=True)

class ContactUsForm(models.Model):
    name = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=25)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Facility(models.Model):
    STATUS_CHOICE = (('draft','Draft'),('published','published'))
    facility_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    facility_img = models.ImageField(upload_to='facility_imgage/')
    facility_desc = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    facility_created_date = models.DateTimeField(auto_now_add=True)
    facility_updated_date = models.DateTimeField(auto_now=True)
    facility_status = models.CharField(max_length=15,choices=STATUS_CHOICE,default='draft')
    #objects = CustomManager()

    def __str__(self):
        return self.facility_title

    def get_absolute_url(self):
        return reverse('facilities_details',args=[self.slug])

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_img = models.ImageField(upload_to='department_image/')
    department_icon_img = models.ImageField(upload_to='department_image/icon/')
    department_duration =models.CharField(max_length=10)

class CollegeExpo(models.Model):
    expo_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    expo_desc = models.TextField()
    expo_topic =models.CharField(max_length=100)
    expo_location = models.CharField(max_length=55)
    expo_date = models.DateField(blank=True)
    expo_time = models.TimeField(blank=True)
    expo_created = models.DateTimeField(auto_now_add=True)
    expo_updated = models.DateTimeField(auto_now=True)

class EventRegister(models.Model):
    name = models.CharField(max_length=25)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_student =models.TextField()
    student_id = models.CharField(max_length=20)
    student_mobile_no = models.IntegerField()
    date_of_birth = models.DateField(blank=True)
    student_address = models.CharField(max_length=200)
    student_img = models.ImageField(default='default.jpg',upload_to='student_profile_image/')
    facebook_url = models.CharField(max_length=100,blank=True)
    google_url = models.CharField(max_length=100, blank=True)
    Twitter_url = models.CharField(max_length=100, blank=True)
    terms_condition = models.CharField(max_length=300)
    #user_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class ExamSem(models.Model):
    exam_sem = models.CharField(max_length=30)

    def __str__(self):
        return self.exam_sem

class Semester(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_semester = models.ForeignKey(ExamSem,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user_semester

# class SemesterList(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     exam_sem = models.ForeignKey(ExamSem,on_delete=models.CASCADE,default='')


class Subject(models.Model):
    course_name = models.ForeignKey(PopularCourses,on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    subject_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject_name

class Exam(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user_semester = models.ForeignKey(Semester,on_delete=models.CASCADE)
    user_semester = models.ForeignKey(ExamSem, on_delete=models.CASCADE)
    course_name = models.ForeignKey(PopularCourses, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    hall_title = models.CharField(max_length=30)
    exam_date_from = models.DateField()
    exam_date_to = models.DateField(blank=True)
    exam_time_from = models.TimeField()
    exam_time_to = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #exam_active = models.BooleanField(default=True)

class ExamSemBy(models.Model):
    exam_semester = models.ForeignKey(ExamSem, on_delete=models.CASCADE)
    course_name = models.ForeignKey(PopularCourses, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    hall_title = models.CharField(max_length=30)
    exam_date_from = models.DateField()
    exam_date_to = models.DateField(blank=True)
    exam_time_from = models.TimeField()
    exam_time_to = models.TimeField()
    exam_duration = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


