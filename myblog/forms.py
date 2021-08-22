from django import forms
from .models import Post , Category ,  Comment 


#choices = [('coding','coding'),('sports', 'sports'),('enteretainment', 'entertainment'),]

choices = Category.objects.all().values_list('name','name')
#
choices_list=[]
for item in choices:
    choices_list.append(item)

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', "title_tag", "author", "category", "body" ,"snipped" ,"header_image")

        widgets = {
            'title': forms.TextInput(attrs={ 'class':"form-control" , "placeholder":"This is Titel Placeholder "}),
            'title_tag': forms.TextInput(attrs={ 'class':"form-control"}),
            'author': forms.TextInput(attrs={ 'class':"form-control", 'value':'' ,'id':'elder','type':'hidden'}),
            #'author': forms.Select(attrs={ 'class':"form-control"}),
            'category': forms.Select(choices=choices_list, attrs={ 'class':"form-control"}),
            'body': forms.Textarea(attrs={ 'class':"form-control"}),
            'snipped': forms.Textarea(attrs={ 'class':"form-control"}),     
             
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', "title_tag","body" , "snipped")

        widgets = {
            'title': forms.TextInput(attrs={ 'class':"form-control" , "placeholder":"This is Titel Placeholder "}),
            'title_tag': forms.TextInput(attrs={ 'class':"form-control"}),
            'body': forms.Textarea(attrs={ 'class':"form-control"}),
            'snipped': forms.Textarea(attrs={ 'class':"form-control"}),
        
             
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ('name','body')


        widgets = {
            'name': forms.TextInput(attrs={ 'class':"form-control" , "placeholder":"This is name User  "}),
            'body': forms.Textarea(attrs={ 'class':"form-control"}),


        } 

class AdminLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control ",}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control",}))