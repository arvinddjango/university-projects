from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import AdmissionForm,BlogCommentForm,ContactForm,EventForm,UserRegisterForm,ProfileForm,UserUpdateForm,UpcomingEventForm,JobForm,ExamSemByForm,EmailSenForm
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.models import User
from urllib.parse import quote_plus
from django.db.models import Count
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index_view(request):
    banner_list = IndexBanner.objects.all()
    more_discover_menu = MoreDiscoverMenu.objects.all()
    index_head_one = IndexHeadOne.objects.all()
    index_head_two = IndexHeadTwo.objects.all()
    popular_course = PopularCourses.objects.all()
    event_list = UpcomingEvent.objects.all()
    job_list =JobVacant.objects.all()
    img_list = ImageGallery.objects.all()
    video_list = Video.objects.all()
    return render(request, 'html/index.html',{ 'banner_list':banner_list,'more_discover_menu':more_discover_menu,'index_head_one':index_head_one,'index_head_two':index_head_two,'popular_course':popular_course,'event_list':event_list,'job_list':job_list,'img_list':img_list,'video_list':video_list})

def about(request):
    about_list = AboutUs.objects.all()
    return render(request,'html/about.html',{'about_list':about_list})

def admission(request):
    admission_page = AdmissionPage.objects.all()
    if request.method=='POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.warning(request, 'Thanks for Submission, You will get reply soon!')
            return redirect('/admission')
    else:
        form = AdmissionForm(request.POST)

    #     if form.is_valid():
    #         form.save(commit=True)
    #         name = form.cleaned_data['name']
    #         phone_no = form.cleaned_data['phone_no']
    #         email_id = form.cleaned_data['email_id']
    #         city = form.cleaned_data['city']
    #         education = form.cleaned_data['education']
    #         course = form.cleaned_data['course']
    #         try:
    #             #send_mail('subject', 'body of the message', 'sender@example.com', ['receiver1@example.com', ])
    #             send_mail(name, email_id, phone_no,city,education,course, ['python6656@gmail.com'])
    #         except BadHeaderError:
    #             return HttpResponse('Invalid header found.')
    #
    #         messages.warning(request, 'Thanks for Submission, You will get reply soon!')
    #         return redirect('/admission')
    # else:
    #     form = AdmissionForm(request.POST)


    return render(request,'html/admission.html',{'form':form,'admission_page':admission_page})

def allcourses(request):
    popular_course = PopularCourses.objects.all()

    return render(request,'html/all-courses.html',{'popular_course':popular_course})

def course_details(request,slug):
    event_list = UpcomingEvent.objects.all()
    popular_course = PopularCourses.objects.get(slug=slug)
    cour_con = CoursComment.objects.filter(popular_course=popular_course)
    return render(request,'html/course-details.html',{'event_list':event_list,'popular_course':popular_course,'cour_con':cour_con})

def awards(request):
    awar_list = Award.objects.all()
    award_detail = AwardList.objects.all()
    return render(request,'html/awards.html',{'awar_list':awar_list,'award_detail':award_detail})

def blog(request):
    blog_list = Blog.objects.all()
    #comment = Blog.objects.get(slug=slug)
    #predefined pagination code
    share_comments = BlogEmailShare.objects.all()
    paginator=Paginator(blog_list,4)
    page_number=request.GET.get('page')
    try:
        blog_list=paginator.page(page_number)
    except PageNotAnInteger:
        blog_list=paginator.page(1)
    except EmptyPage:
        blog_list=paginator.page(paginator.num_pages)
        #end predefined pagination code
    return render(request,'html/blog.html',{'blog_list':blog_list,'share_comments':share_comments})



#Email Share blog contenttypes
from django.core.mail import send_mail
def shareby(request,id):
    comment =Blog.objects.get(id=id)
    sent = False
    if request.method=='POST':
        form = EmailSenForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comment = comment
            new_comment.save()
            cd = form.cleaned_data
            subject = '{} ({}) recomends To Read "{}"'.format(cd['name'],cd['email_from'],comment.blog_title)
            post_url = request.build_absolute_uri(comment.get_absolute_url())
            message = 'Read Post At \n {}\n\n{}\s Comments:\n{}'.format(post_url, cd['name'], cd['message'])
            send_mail(subject, message, 'arvind@blog.com', [cd['email_to']])
            sent = True
    else:
        form = EmailSenForm()

    return render(request,'html/shareby.html',{'form':form,'comment':comment,'sent':sent})

def blog_details(request,slug):
    comment = Blog.objects.get(slug=slug) #comment name comming from model fields, same name will appear here
    share_string = quote_plus(comment.blog_desc) # for social Share code
    blog_comments = BlogComment.objects.filter(comment=comment) # comment against comment variable slug
    share_comments = BlogEmailShare.objects.filter(comment=comment)
    comment_submit = False
    if request.method=='POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.comment=comment
            new_comment.save()
            #comment_submit=True
            return redirect('blog_details', slug=slug)

    else:
        form = BlogCommentForm()
    return render(request,'html/blog-details.html',{'comment':comment,'blog_comments':blog_comments,'form':form,'comment_submit':comment_submit,'share_string':share_string,'share_comments':share_comments})

# from django.core.mail import send_mail
#
# def mail_send_view(request,slug):
#     comment = Blog.objects.get(slug=slug)
#     sent = False
#     if request.method=='POST':
#         form=EmailSenForm(request.POST)
#         if form.is_valid():
#             cd=form.cleaned_data
#             subject='{}({}) Important Student Post "{}"'.format(cd['name'],cd['email'],comment.blog_title)
#             post_url=request.build_absolute_uri(comment.get_absolute_url())
#             message='Read Student Post At \n {}\n\n{}\s Comments:\n{}'.format(post_url,cd['name'],cd['blog_comments'])
#             send_mail(subject,message,'kumar@blog.com',[cd['to']])
#             sent=True
#     else:
#         form=EmailSenForm()
#     return render(request,'html/sharemail.html',{'form':form,'comment':comment,'sent':sent})

def contact_us(request):
    contact_details = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.info(request, 'Thanks for Contacting!')
            return redirect('/contact-us')
    else:
        form = ContactForm(request.POST)

    return render(request,'html/contact-us.html',{'contact_details':contact_details,'form':form})

def user_register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =  UserRegisterForm()

    return render(request,'html/register.html',{'form':form})

def dashboard(request):
    return render(request,'html/dashboard.html')

def db_course(request):
    return render(request,'html/db-courses.html')

# from collections import defaultdict
# users = defaultdict(list)
# for result in Exam.objects.values('company', 'user').order_by('company', 'user'):
#     users[result['company']].append(result['user'])

def db_exams(request):
    exam_list = Exam.objects.filter(user=request.user)
    semester_list = Semester.objects.filter(user=request.user)
    #exam_list = Semester.objects.prefetch_related('user_semester').all()
    #exam_list = Exam.objects.values('user_semester__user')
    #semester_list = Semester.objects.all()
    return render(request,'html/db-exams.html',{'semester_list':semester_list,'exam_list':exam_list})

def db_profile(request):
    student_profile =Profile.objects.all()
    return render(request,'html/db-profile.html',{'student_profile':student_profile})

# def log_view(request):
#     return render(request,'html/login.html')

def db_time_line(request):
    return render(request,'html/db-time-line.html')

def departments(request):
    facilities_list = Facility.objects.all()
    department_list = Department.objects.all()
    department_count = Department.objects.all().count()
    course_count = PopularCourses.objects.all().count()
    facilities_count = Facility.objects.all().count
    # predefined pagination code
    paginator = Paginator(facilities_list, 3)
    page_number = request.GET.get('page')
    try:
        facilities_list = paginator.page(page_number)
    except PageNotAnInteger:
        facilities_list = paginator.page(1)
    except EmptyPage:
        facilities_list = paginator.page(paginator.num_pages)
        # end predefined pagination code
    return render(request,'html/departments.html',{'facilities_list':facilities_list,'department_list':department_list,'department_count':department_count,'course_count':course_count,'facilities_count':facilities_count})

def events_deatils(request,slug):
    event_list = UpcomingEvent.objects.filter(slug=slug)
    return render(request,'html/event-details.html',{'event_list':event_list})

def events_register(request):
    expo_list = UpcomingEvent.objects.all().order_by('-id')
    if request.method=='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.warning(request, 'Thanks for Apply, You will get reply soon!')
            return redirect('/event-register')
    else:
        form = EventForm(request.POST)
    return render(request,'html/event-register.html',{'expo_list':expo_list,'form':form})

def events(request):
    event_list = UpcomingEvent.objects.all()
    return render(request,'html/events.html',{'event_list':event_list})

def jobs(request):
    job_list = JobVacant.objects.all()
    return render(request,'html/job-vacant.html',{'job_list':job_list})

def jobs_details(request,slug):
    job_list = JobVacant.objects.filter(slug=slug)
    return render(request,'html/job-vacants-details.html',{'job_list':job_list})

def facilities(request):
    facilities_list = Facility.objects.all()
    #predefined pagination code
    paginator=Paginator(facilities_list,4)
    page_number=request.GET.get('page')
    try:
        facilities_list=paginator.page(page_number)
    except PageNotAnInteger:
        facilities_list=paginator.page(1)
    except EmptyPage:
        facilities_list=paginator.page(paginator.num_pages)
        #end predefined pagination code
    return render(request,'html/facilities.html',{'facilities_list':facilities_list})

def facilities_details(request,slug):
    facilities_list = Facility.objects.get(slug=slug)

    return render(request,'html/facilities-detail.html',{'facilities_list':facilities_list})

def gallery_photo(request):
    img_list = ImageGallery.objects.all()
    return render(request,'html/gallery-photo.html',{'img_list':img_list})

def research(request):
    department_list = Department.objects.all()
    # predefined pagination code
    paginator = Paginator(department_list, 8)
    page_number = request.GET.get('page')
    try:
        department_list = paginator.page(page_number)
    except PageNotAnInteger:
        department_list = paginator.page(1)
    except EmptyPage:
        department_list = paginator.page(paginator.num_pages)
        # end predefined pagination code
    return render(request,'html/research.html',{'department_list':department_list})


''' .... Admin Page View Start Here....'''

def admin(request):
    student_profile = Profile.objects.all()
    popular_course = PopularCourses.objects.all()
    event_list = UpcomingEvent.objects.all()
    job_list = JobVacant.objects.all()
    exam_list = Exam.objects.all()
    student_count = Profile.objects.all().count()
    course_count = PopularCourses.objects.all().count()
    admission_count = Admission.objects.all().count()
    enquiry_count = ContactUsForm.objects.all().count()
    return render(request,'html/admin.html',{'student_profile':student_profile,'popular_course':popular_course,'event_list':event_list,'job_list':job_list,'exam_list':exam_list,'student_count':student_count,'course_count':course_count,'admission_count':admission_count,'enquiry_count':enquiry_count})

def admin_about_menu(request):
    return render(request,'html/admin-about-menu.html')

def admin_add_courses(request):
    return render(request,'html/admin-add-courses.html')

def admin_admission_enquiry(request):
    admission_enquiry_list = Admission.objects.all().order_by('-id')
    return render(request,'html/admin-admission-enquiry.html',{'admission_enquiry_list':admission_enquiry_list})

def admin_admission_menu(request):
    return render(request,'html/admin-admission-menu.html')

def admin_all_courses(request):
    return render(request,'html/admin-all-courses.html')

def admin_all_enquiry(request):
    return render(request,'html/admin-all-enquiry.html')

def admin_all_menu(request):
    return render(request,'html/admin-all-menu.html')

def admin_common_enquiry(request):
    contact_enquiry = ContactUsForm.objects.all()
    return render(request,'html/admin-common-enquiry.html',{'contact_enquiry':contact_enquiry})

def admin_course_details(request):
    return render(request,'html/admin-course-details.html')

def admin_course_enquiry(request):
    return render(request,'html/admin-course-enquiry.html')

def admin_event_add(request):
    if request.method=='POST':
        form = UpcomingEventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-event-all')
    else:
        form = UpcomingEventForm()
    return render(request,'html/admin-event-add.html',{'form':form})

def admin_event_all(request):
    event_list = UpcomingEvent.objects.all().order_by('-id')
    return render(request,'html/admin-event-all.html',{'event_list':event_list})

def admin_event_edit(request,id):
    event_edit=UpcomingEvent.objects.get(id=id)
    if request.method == 'POST':
        form = UpcomingEventForm(request.POST,request.FILES, instance=event_edit)
        if form.is_valid():
            form.save()
            return redirect('/admin-event-all')
    else:
        form = UpcomingEventForm(request.POST,instance=event_edit)

    return render(request,'html/admin-event-edit.html',{'event_edit':event_edit,'form':form})

def event_delete(request,id):
    event_del = UpcomingEvent.objects.get(id=id)
    event_del.delete()
    return redirect('/admin-event-all')


def admin_event_enquiry(request):
    event_enquiry = EventRegister.objects.all().order_by('-id')
    return render(request,'html/admin-event-enquiry.html',{'event_enquiry':event_enquiry})

def admin__exam_add(request):
    if request.method=='POST':
        form = ExamSemByForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin-exam-all')
    else:
        form = ExamSemByForm()
    return render(request,'html/admin-exam-add.html',{'form':form})

def admin__exam_all(request):
    exam_all = ExamSemBy.objects.all()
    return render(request,'html/admin-exam-all.html',{'exam_all':exam_all})

def admin__exam_edit(request,id):
    exam_edit = ExamSemBy.objects.get(id=id)
    if request.method=='POST':
        form = ExamSemByForm(request.POST,instance=exam_edit)
        if form.is_valid():
            form.save()
            return redirect('/admin-exam-all')
    else:
        form = ExamSemByForm(request.POST,instance=exam_edit)
    return render(request,'html/admin-exam-edit.html',{'exam_edit':exam_edit,'form':form})

def exam_delete(request,id):
    exam_del = ExamSemBy.objects.get(id=id)
    exam_del.delete()
    return redirect('/admin-exam-all')

def admin_exam_group_add(request):
    return render(request,'html/admin-exam-group-add.html')

def admin_export_data(request):
    return render(request,'html/admin-export-data.html')

def admin_forgot(request):
    return render(request,'html/admin-forgot.html')

def admin_import_data(request):
    return render(request,'html/admin-import-data.html')

def admin_job_add(request):
    if request.method=='POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-job-all')
    else:
        form = JobForm()
    return render(request,'html/admin-job-add.html',{'form':form})

def admin_job_all(request):
    job_list = JobVacant.objects.all().order_by('-id')
    return render(request,'html/admin-job-all.html',{'job_list':job_list})

def admin_job_edit(request,id):
    job_edit = JobVacant.objects.get(id=id)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job_edit)
        if form.is_valid():
            form.save()
            return redirect('/admin-job-all')
    else:
        form = JobForm(request.POST, instance=job_edit)
    return render(request,'html/admin-job-edit.html',{'job_edit':job_edit,'form':form})

def admin_job_view(request,id):
    job_list_view = JobVacant.objects.get(id=id)

    return render(request,'html/admin-job-view.html',{'job_list_view':job_list_view})

def job_delete(request,id):
    job_del = JobVacant.objects.get(id=id)
    job_del.delete()
    return redirect('/admin-job-all')

def admin_login(request):
    return render(request,'html/admin-login.html')

def admin_main_menu(request):
    return render(request,'html/admin-main-menu.html')

def admin_page_add(request):
    return render(request,'html/admin-page-add.html')

def admin_page_all(request):
    return render(request,'html/admin-page-all.html')

def admin_page_edit(request):
    return render(request,'html/admin-page-edit.html')

def admin_panel_setting(request):
    return render(request,'html/admin-panel-setting.html')

def admin_quick_link(request):
    return render(request,'html/admin-quick-link.html')

def admin_seminar_add(request):
    return render(request,'html/admin-seminar-add.html')

def admin_seminar_all(request):
    return render(request,'html/admin-seminar-all.html')

def admin_seminar_edit(request):
    return render(request,'html/admin-seminar-edit.html')

def admin_seminar_enquiry(request):
    return render(request,'html/admin-seminar-enquiry.html')

def admin_setting(request):
    return render(request,'html/admin-setting.html')

def admin_slider(request):
    return render(request,'html/admin-slider.html')

def admin_slider_edit(request):
    return render(request,'html/admin-slider-edit.html')

def admin_student_details(request,id):
    student_edit = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=student_edit)
        if form.is_valid():
            form.save()
            return redirect('/admin-user-all')
    else:
        form = ProfileForm(request.POST,instance=student_edit)

    return render(request,'html/admin-student-details.html',{'form':form,'student_edit':student_edit})

def user_delete(request,id):
    username = Profile.objects.get(id=id)
    username.delete()
    return redirect('/admin-user-all')

def admin_user_view(request,id):
    user_view = Profile.objects.get(id=id)

    return render(request,'html/admin-user-view.html',{'user_view':user_view})

def admin_trash_courses(request):
    return render(request,'html/admin-trash-courses.html')

def admin_user_add(request):
    usr_list = User.objects.all()
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/admin-user-all')
    else:
        form = ProfileForm()

    return render(request,'html/admin-user-add.html',{'usr_list':usr_list,'form':form})

def admin_user_all(request):
    student_profile = Profile.objects.all().order_by('-id')
    return render(request,'html/admin-user-all.html',{'student_profile':student_profile})

def admin_add_user_add(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin-user-list')
    else:
        form = UserRegisterForm()

    return render(request,'html/admin-adduser-add.html',{'form':form})


def admin_user_list(request):
    user_profile = User.objects.all().order_by('-id')
    return render(request,'html/admin-user-list.html',{'user_profile':user_profile})

def admin_user_edit(request,id):
    user_edit = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user_edit)
        if form.is_valid():
            form.save()
            return redirect('/admin-user-list')
    else:
        form = UserUpdateForm(request.POST,instance=user_edit)

    return render(request,'html/admin-user-edit.html',{'form':form,'user_edit':user_edit})



def admin_user_details(request,id):
    user_details = User.objects.get(id=id)

    return render(request,'html/admin-user-details.html',{'user_details':user_details})

def adminuser_delete(request,id):
    user_del = User.objects.get(id=id)
    user_del.delete()
    return redirect('/admin-user-list')

def admin_view_enquiry(request):
    contact_enquiry = ContactUsForm.objects.all().order_by('-id')
    return render(request,'html/admin-view-enquiry.html',{'contact_enquiry':contact_enquiry})