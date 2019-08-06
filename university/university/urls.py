"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from universityapp import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # media
from django.conf.urls.static import static  # media
from django.contrib.auth import views as auth_views


# from university.universityapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index_view'),
    path('about/', views.about, name='about'),
    path('admission/', views.admission, name='admission'),
    path('allcourses/', views.allcourses, name='allcourses'),
    path('awards/', views.awards, name='awards'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/<slug:slug>/', views.blog_details, name='blog_details'),
    # path('details/<slug:slug>/', views.mail_send_view),
    # path('mail-share/<slug:slug>/',views.mail_send_view),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('course-details/<slug:slug>/', views.course_details, name='course_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('db-course/', views.db_course, name='db_course'),
    path('db-exams/', views.db_exams, name='db_exams'),
    path('db-profile/', views.db_profile, name='db_profile'),
    path('db-time-line/', views.db_time_line, name='db_time_line'),
    path('departments/', views.departments, name='departments'),
    path('event-details/<slug:slug>/', views.events_deatils, name='events_deatils'),
    # path('(?P<pk>\d+)/$/',views.events_deatils,name='events_deatils'),
    path('event-register/', views.events_register, name='events_register'),
    path('events/', views.events, name='events'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs-details/<slug:slug>/', views.jobs_details, name='jobs_details'),
    path('facilities/', views.facilities, name='facilities'),
    path('facilities-details/<slug:slug>/', views.facilities_details, name='facilities_details'),
    path('gallery-photo/', views.gallery_photo, name='gallery_photo'),
    path('research/', views.research, name='research'),
path('shareby/<slug:id>/', views.shareby, name='shareby'),
# path('login/', views.log_view, name='log_view'),
path('register/', views.user_register, name='user_register'),
    path('login/', auth_views.LoginView.as_view(template_name='html/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='html/logout.html'),
        name='logout'),

    # ''' Admin Page URL Start Here....''',

    path('adminpanel/', views.admin, name='admin'),
    path('admin-about-menu/', views.admin_about_menu, name='admin_about_menu'),
    path('admin-add-courses/', views.admin_add_courses, name='admin_add_courses'),
    path('admin-admission-enquiry/', views.admin_admission_enquiry, name='admin_admission_enquiry'),
    path('admin-admission-menu/', views.admin_admission_menu, name='admin_admission_menu'),
    path('admin-all-courses/', views.admin_all_courses, name='admin_all_courses'),
    path('admin-all-enquiry/', views.admin_all_enquiry, name='admin_all_enquiry'),
    path('admin-all-menu/', views.admin_all_menu, name='admin_all_menu'),
    path('admin-common-enquiry/', views.admin_common_enquiry, name='admin_common_enquiry'),
    path('admin-course-details/', views.admin_course_details, name='admin_course_details'),
    path('admin-course-enquiry/', views.admin_course_enquiry, name='admin_course_enquiry'),
    path('admin-event-add/', views.admin_event_add, name='admin_event_add'),
    path('admin-event-all/', views.admin_event_all, name='admin_event_all'),
    path('admin-event-edit/<int:id>/', views.admin_event_edit, name='admin_event_edit'),
path('admin-event-delete/<int:id>/', views.event_delete, name='admin_event_delete'),
    path('admin-event-enquiry/', views.admin_event_enquiry, name='admin_event_enquiry'),
    path('admin-exam-add/', views.admin__exam_add, name='admin__exam_add'),
    path('admin-exam-all/', views.admin__exam_all, name='admin__exam_all'),
    path('admin-exam-edit/<int:id>/', views.admin__exam_edit, name='admin__exam_edit'),
path('admin-exam-delete/<int:id>/', views.exam_delete, name='exam_delete'),
    path('admin-exam-group-add/', views.admin_exam_group_add, name='admin_exam_group_add'),
    path('admin-export-data/', views.admin_export_data, name='admin_export_data'),
    path('admin-forgot/', views.admin_forgot, name='admin_forgot'),
    path('admin-import-data/', views.admin_import_data, name='admin_import_data'),
    path('admin-job-add/', views.admin_job_add, name='admin_job_add'),
    path('admin-job-all/', views.admin_job_all, name='admin_job_all'),
    path('admin-job-edit/<int:id>/', views.admin_job_edit, name='admin_job_edit'),
path('job-list-view/<int:id>/', views.admin_job_view, name='admin_job_view'),
path('admin-job-delete/<int:id>/', views.job_delete, name='job_delete'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-main-menu/', views.admin_main_menu, name='admin_main_menu'),
    path('admin-page-add/', views.admin_page_add, name='admin_page_add'),
    path('admin-page-all/', views.admin_page_all, name='admin_page_all'),
    path('admin-page-edit/', views.admin_page_edit, name='admin_page_edit'),
    path('admin-panel-setting/', views.admin_panel_setting, name='admin_panel_setting'),
    path('admin-quick-link/', views.admin_quick_link, name='admin_quick_link'),
    path('admin-seminar-add/', views.admin_seminar_add, name='admin_seminar_add'),
    path('admin-seminar-all/', views.admin_seminar_all, name='admin_seminar_all'),
    path('admin-seminar-edit/', views.admin_seminar_edit, name='admin_seminar_edit'),
    path('admin-seminar-enquiry/', views.admin_seminar_enquiry, name='admin_seminar_enquiry'),
    path('admin-setting/', views.admin_setting, name='admin_setting'),
    path('admin-slider/', views.admin_slider, name='admin_slider'),
    path('admin-slider-edit/', views.admin_slider_edit, name='admin_slider_edit'),
    path('admin-student-details/<int:id>/', views.admin_student_details, name='admin_student_details'),
path('user-delete/<int:id>/', views.user_delete, name='user_delete'),
path('user-view/<int:id>/', views.admin_user_view, name='user_view'),
    path('admin-trash-courses/', views.admin_trash_courses, name='admin_trash_courses'),
    path('admin-user-add/', views.admin_user_add, name='admin_user_add'),
    path('admin-user-all/', views.admin_user_all, name='admin_user_all'),
path('admin-add-user-add/', views.admin_add_user_add, name='admin_add_user_add'),
    path('admin-user-list/', views.admin_user_list, name='admin_user_list'),
path('admin-user-edit/<int:id>/', views.admin_user_edit, name='admin_user_edit'),
path('admin-user-details/<int:id>/', views.admin_user_details, name='admin_user_details'),
path('admin-user-delete/<int:id>/', views.adminuser_delete, name='adminuser_delete'),
    path('admin-view-enquiry/', views.admin_view_enquiry, name='admin_view_enquiry'),

    # path('universityapp/', include('universityapp.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
