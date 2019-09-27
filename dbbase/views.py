# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from .models import Hdb
from .forms import Tform, SearchForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DateDetailView, CreateView, DeleteView
from django.db.models import Q
from django.views.generic.edit import FormView
#from django.core.urlresolvers import reverse_lazy
#from django.core.urlresolvers import reverse
from django.urls import reverse, reverse_lazy
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as django_logout
from django.template import RequestContext
from django.http import HttpResponse



def homep(request):
    return render(request, 'home.html')

def index(request):
    lists = Hdb.objects.all()
    context ={'lists':lists}
    return render(request, 'dblist.html', context)
    
def lists_topics(request, pk):
    hlists = get_object_or_404(Hdb, pk=pk)
  
    return render(request, 'dblistView.html', {'hlists': hlists})
    
def inputdb(request):
    #form =Tform()
    if request.method =="POST":
        form = Tform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
        
    else:
        form =Tform()
        
    return render(request, 'dbinput.html', {'form':form})
    

class IndexView(ListView):
    model=Hdb
    template_name = 'dblistView.html' # 디폴트 템플릿명: <app_label>/<model_name>_list.html
    context_object_name = 'hdb_list' # 디폴트 컨텍스트 변수명 :  object_list
    paginate_by=5
    #queryset = Hdb.objects.all()
    #def get_queryset(self): # 컨텍스트 오버라이딩
    #  return Hdb.objects.ordered_by(int('created_date'))
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Hdb.objects.filter(ntext__icontains=query)
        else:
            return Hdb.objects.all().order_by('-ntext')
    
    
class HdbdetailView(DetailView):
    model= Hdb
    form_class = Tform
    #success_url = reverse_lazy('detail')
    template_name = 'dbdetail.html'
    #context_object_name = 'ntext'
    
    
    
    #def get_context_data(self, **kwargs):
    #    context = super(HdbdetailView, self).get_context_data(**kwargs)
        # for_user = self.request.user
    #    user_form = Tform(data=self.request.GET)

    #    if user_form.is_valid():
   #        for_user = user_form.cleaned_data['user']
    #    else:
     #       for_user = None

    #    context.update(
     #       categories=Hdb.objects.all(),
    #        for_user=for_user,
    #        user_form=user_form,
    #       # VARIANCE_CUTOFF=defaults.VARIANCE_CUTOFF
    #    )
    #    return context 
        



class HdbUpdateView(UpdateView):
    model = Hdb
    fields = ('__all__')
   # template_name = 'dbdetail.html'
   # pk_url_kwarg = 'hdb_pk'
   # context_object_name = 'hdb_list'

    #def form_valid(self, form):
    #    hdb = form.save(commit=False)
    #    hdb.updated_by = self.request.user
    #    hdb.updated_at = timezone.now()
    #    hdb.save()
     #   return redirect('indexview', pk=hdb.hdb_list.board.pk, hdb_pkc_pk=hdb.hdb_list.pk)
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})  
        
      
class SearchFormView(FormView):
    form_class = SearchForm 
    template_name = 'dbdetail.html' 
    
    def form_valid(self,form): # post method로 값이 전달 됬을 경우 
        word = '%s' %self.request.POST['word'] # 검색어 
        post_list = Hdb.objects.filter( 
            Q(title__icontains=word) | Q(content__icontains=word) # Q 객체를 사용해서 검색한다. # title,context 칼럼에 대소문자를 구분하지 않고 단어가 포함되어있는지 (icontains) 검사 
        ).distinct() #중복을 제거한다. 
        context = {} 
        context['object_list'] = post_list # 검색된 결과를 컨텍스트 변수에 담는다. 
        context['search_word']= word # 검색어를 컨텍스트 변수에 담는다. 
        return render(self.request, self.template_name, context)
        
        
class HdbCreateView(CreateView):
    model = Hdb
    fields = ('__all__')
    
    
class HdbDeleteView(DeleteView):
    model = Hdb
    success_url = reverse_lazy('indexview')
    
class HdbprintView(DetailView):
    model= Hdb
   # form_class = Tform
    template_name = 'dbprint.html'
    
    
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
        
def logout(request):
    django_logout(request)
    return render(request,'logged_out.html')
   