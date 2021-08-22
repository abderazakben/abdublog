from django.shortcuts import render , get_object_or_404 , redirect 
from django.contrib.auth import authenticate , login , logout
from django.views.generic import View, TemplateView , ListView, DetailView ,CreateView , UpdateView , DeleteView , FormView
from .models import Post , Category , Comment , Admin
from .forms import PostForms ,EditForm , CommentForm ,AdminLoginForm
from members.forms import  ProfilePageForm
from django.urls import reverse_lazy
from django.urls import  reverse_lazy , reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

#def home(request):
#   post=Post.objects.all()
#    return render(request,'home.html',{'post:post'})
def likeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
         post.likes.add(request.user)
         liked = True
    return HttpResponseRedirect(reverse('myblog:article_detaile', args=[str(pk)]))


class HomeView(ListView):

    model= Post
    template_name = 'home.html'
    paginate_by = 4
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context 

def CategorylistView(request):
    cat_menu_list= Category.objects.all()  
    return render(request, 'category_list.html' , {'cat_menu_list':cat_menu_list})


def CategoryView(request,cats):
    category_posts = Post.objects.filter(category=cats.replace('-' , ' ', ))
    return render(request, 'categories.html' ,{'cats':cats.title().replace('-' , ' ') , 'category_posts':category_posts})


class AboutView(TemplateView ):

    template_name = "about.html"

class ArticleDetalView(DetailView):
    model = Post
    #form_class  = PostForms
    template_name = 'articl_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetalView, self).get_context_data(*args, **kwargs)

        stuff= get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True 

        context['cat_menu'] = cat_menu
        context["total_likes"]= total_likes
        context["liked"] = liked
        return context      

class AddPostView(CreateView):
    model = Post
    form_class  = PostForms
    template_name = 'add_post.html'
    #hadi ila gay3amar post kalala o bkolchi lihadatih f jadwal d post 
    #fields = '__all__'
    #hadi  gay3amar dikchi ligathaddlo nta hna bla b jadwal li model
    #fields = ('title', 'body')

class AddCommentView(CreateView):
    model = Comment
    form_class  = CommentForm 
    #fields = '__all__'  
    template_name = 'add_comment.html'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('myblog:home')
      
class AddCategorView(CreateView):
    model = Category
    #form_class  = PostForms
    template_name = 'add_category.html'
    #hadi ila gay3amar post kalala o bkolchi lihadatih f jadwal d post 
    fields = '__all__'
    #hadi  gay3amar dikchi ligathaddlo nta hna bla b jadwal li model
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class  = EditForm
    #fields = ['title' , 'title_tag','body']    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('myblog:home') 


######## view admin ######

class AdminLoginView(FormView):
    template_name = "adminpage/adminlogin.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("myblog:adminhome")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request,usr)
        else:
             return render(self.request , self.template_name , {"form":self.form_class,"error":"Invalid credentails"})

        return super().form_valid(form)     

class AdminHome(TemplateView):

    template_name = "adminpage/adminhome.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request,*args ,**kwargs)

    def get_context_data(self, *args, **kwargs):
        cat_menu_admin = Post.objects.all()
        context = super(AdminHome, self).get_context_data(*args, **kwargs)
        context['cat_menu_admin'] = cat_menu_admin
        return context

def courMView(request):
    context = []
    return render(request, 'adminpage/motaki_dris.html' ,{})




##### 19:44