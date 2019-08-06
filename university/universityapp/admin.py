from django.contrib import admin
# from .models import IndexBanner,MoreDiscoverMenu,IndexHeadOne,IndexHeadTwo,PopularCourses,UpcomingEvent,JobVacant,ImageGallery,Video,AboutUs,Admission,AdmissionPage,Award,AwardList,Blog,BlogComment,Contact,ContactUsForm,Facility,Department,CollegeExpo,EventRegister,Profile
from .models import *

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['banner_btn_name','banner_created_date','banner_updated_date','banner_status']

admin.site.register(IndexBanner,BannerAdmin)

class MoreMenuAdmin(admin.ModelAdmin):
    list_display = ['menu_btn','menu_created_date','menu_updated_date']

admin.site.register(MoreDiscoverMenu,MoreMenuAdmin)

class IndexHeadOneadmin(admin.ModelAdmin):
    list_display = ['index_head','index_created','index_updated']

admin.site.register(IndexHeadOne,IndexHeadOneadmin)


class IndexHeadTwoadmin(admin.ModelAdmin):
    list_display = ['index_head_two', 'index_created_two', 'index_updated_two']

admin.site.register(IndexHeadTwo, IndexHeadTwoadmin)

class PopularCourseAdmin(admin.ModelAdmin):
    list_display = ['pupular_course_head','popular_course_created','popular_course_updated']
    prepopulated_fields = {'slug': ('pupular_course_head',)}

admin.site.register(PopularCourses,PopularCourseAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ['event_title','event_from','event_time_from','event_location','event_create','event_updated']
    prepopulated_fields = {'slug': ('event_title',)}

admin.site.register(UpcomingEvent,EventAdmin)

class JobVacantAdmin(admin.ModelAdmin):
    list_display = ['job_title','job_location','job_create','job_updated']
    prepopulated_fields = {'slug':('job_title',)}

admin.site.register(JobVacant,JobVacantAdmin)

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['img_caption','img_created','img_updated']

admin.site.register(ImageGallery,ImageGalleryAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['video_title']

admin.site.register(Video,VideoAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ['about_title_one','about_created','about_updated']

admin.site.register(AboutUs,AboutAdmin)

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['name','phone_no','email_id','city','course']

admin.site.register(Admission,AdmissionAdmin)

class AdmissionPageAdmin(admin.ModelAdmin):
    list_display = ['admission_title']

admin.site.register(AdmissionPage,AdmissionPageAdmin)

class AwardAdmin(admin.ModelAdmin):
    list_display = ['award_title','award_date']

admin.site.register(Award,AwardAdmin)

class AwardListAdmin(admin.ModelAdmin):
    list_display = ['award_title','award_list_title']
    prepopulated_fields = {'slug': ('award_title',)}

admin.site.register(AwardList,AwardListAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title','publish','blog_created_date','blog_updated_date','blog_status']
    prepopulated_fields = {'slug':('blog_title',)}

admin.site.register(Blog,BlogAdmin)


class BlogCommentadmin(admin.ModelAdmin):
    list_display = ['comment','name','email','created','updated','active']

admin.site.register(BlogComment,BlogCommentadmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_email']

admin.site.register(Contact,ContactAdmin)

class ContactUsFormAdmin(admin.ModelAdmin):
    list_display = ['name','phone','city','email']

admin.site.register(ContactUsForm,ContactUsFormAdmin)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ['facility_title','publish','facility_created_date','facility_updated_date','facility_status']
    prepopulated_fields = {'slug':('facility_title',)}

admin.site.register(Facility,FacilityAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name','department_duration']

admin.site.register(Department,DepartmentAdmin)

class CollegeexpoAdmin(admin.ModelAdmin):
    list_display = ['expo_name','expo_topic','expo_location','expo_date']
    prepopulated_fields = {'slug':('expo_name',)}

admin.site.register(CollegeExpo,CollegeexpoAdmin)

class EventRegAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','city','country','created']

admin.site.register(EventRegister,EventRegAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student_id','user','student_mobile_no','created','updated']

admin.site.register(Profile,ProfileAdmin)

class ExamSemAdmin(admin.ModelAdmin):
    list_display = ['exam_sem']

admin.site.register(ExamSem,ExamSemAdmin)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ['user','user_semester']

admin.site.register(Semester,SemesterAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['course_name','subject_name','subject_active']

admin.site.register(Subject,SubjectAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ['user_semester','course_name','exam_date_from','created','updated']

admin.site.register(Exam,ExamAdmin)

class ExamSemByAdmin(admin.ModelAdmin):
    list_display = ['exam_semester','course_name','exam_date_from','created','updated']

admin.site.register(ExamSemBy,ExamSemByAdmin)

class shareCountAdmin(admin.ModelAdmin):
    list_display = ['blog_title']

admin.site.register(ShareCount,shareCountAdmin)

class coursecommentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(CoursComment,coursecommentAdmin)

class BlogEmailShareAdmin(admin.ModelAdmin):
    list_display = ['name','email_from','email_to','message','created','updated']
admin.site.register(BlogEmailShare,BlogEmailShareAdmin)