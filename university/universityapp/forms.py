from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Admission, BlogComment, ContactUsForm, EventRegister,Profile,UpcomingEvent,JobVacant,ExamSemBy,BlogEmailShare


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email Address'}))
    first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    # username = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    # email = forms.EmailField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email Address'}))
    # first_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    # last_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    # password1 = forms.CharField(label='', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))
    # password2 = forms.CharField(label='', widget=forms.PasswordInput(
    #     attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name']

class ProfileForm(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all(), initial=1)
    # about_student = forms.CharField(label='',widget=forms.Textarea(attrs={'class':'form-control','placeholder':'About Student'}))
    # student_id = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'forms-control','placeholder':'Enter Student Id'}))
    # student_mobile_no = forms.IntegerField(label='',widget=forms.NumberInput({'class':'form-control','placeholder':'Enter Student Mobile Number'}))
    # date_of_birth = forms.DateField(label='',widget=forms.widgets.DateInput(format="%Y-%m-%d", attrs={'class':'form-control','placeholder':'yyyy-mm-dd'}))
    # student_address = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Address'}))
    # student_img = forms.ImageField(label='Image file input',
    #                          widget=forms.FileInput(attrs={'class': 'form-control-file', 'id': 'photoimg'}))
    # #student_img = forms.ImageField()
    # facebook_url = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Facebook URL'}))
    # google_url = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Student Google URL'}))
    # Twitter_url = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Enter Student Twitter URL'}))
    # terms_condition = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Terms & Condition'}))


    class Meta:
        model = Profile
        fields = ['user','about_student','student_id','student_mobile_no','date_of_birth','student_address','student_img','facebook_url','google_url','Twitter_url','terms_condition']

    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['user'].queryset = User.objects.all()


STATUS_CHOICES = (('Aerospace Engineering', 'Aerospace Engineering'), ('Agriculture Courses', 'Agriculture Courses'),
                  ('Fashion Technology', 'Fashion Technology'), ('Marine Engineering', 'Marine Engineering'),
                  ('Building, Construction Management', 'Building, Construction Management'),
                  ('Web Development', 'Web Development'), ('Accountant course', 'Accountant course'),
                  ('Dot Net Development', 'Dot Net Development'), ('Java Development', 'Java Development'),
                  ('Chemical Engineering', 'Chemical Engineering'))


class AdmissionForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Full Name'}))
    phone_no = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}))
    email_id = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email '}))
    city = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your City Name'}))
    education = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Education'}))
    course = forms.ChoiceField(label='', choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Admission
        fields = ['name', 'phone_no', 'email_id', 'city', 'education', 'course']


class BlogCommentForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'validate', 'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'validate', 'placeholder': 'Email'}))
    message = forms.CharField(label='',
                              widget=forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': 'Message'}))

    class Meta:
        model = BlogComment
        fields = ('name', 'email', 'message')


class EmailSenForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email_from = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    email_to = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email To'}))
    message = forms.CharField(label='', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))

    class Meta:
        model = BlogEmailShare
        fields = ('name', 'email_from', 'email_to', 'message')

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    phone = forms.IntegerField(label='',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    message = forms.CharField(label='',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = ContactUsForm
        fields = ('name', 'phone', 'email', 'city', 'message')


class EventForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    country = forms.CharField(label='',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}))

    class Meta:
        model = EventRegister
        fields = ('name', 'phone', 'email', 'city', 'country')


class UpcomingEventForm(forms.ModelForm):
    class Meta:
        model = UpcomingEvent
        fields = ['event_img','event_title','slug', 'event_desc', 'event_location', 'event_from','event_time_from','event_time_to']

class JobForm(forms.ModelForm):
    class Meta:
        model = JobVacant
        fields = ['job_img','job_title','slug','job_desc','job_location','job_opening','job_position','job_from','job_time_from','job_time_to']

class ExamSemByForm(forms.ModelForm):
    class Meta:
        model = ExamSemBy
        fields = ['exam_semester','course_name','subject_name','hall_title','exam_date_from','exam_date_to','exam_time_from','exam_time_to','exam_duration']


# class EmailSenForm(forms.Form):
#     name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}))
#     email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email'}))
#     to=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email To'}))
#     comment=forms.CharField(label='',required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Comment'}))