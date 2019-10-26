from django.shortcuts import render , redirect
from django.db.models import Count
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from polls.forms import PollForm ,EditPollForm,ChoiceForm
from .models import Choice,Poll,Vote
import datetime

# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from polls.models import Poll

@login_required
def polls_list(request):
    polls = Poll.objects.all()
    search_term=''
    if 'text' in request.GET:
        polls=polls.order_by('text')
    if 'pub_date' in request.GET:
        polls=polls.order_by('-pub_date')
    if 'num_vote' in request.GET:
        polls=polls.annotate(Count('vote')).order_by('vote__count')
    if 'search' in request.GET :
        search_term=request.GET['search']
        polls=polls.filter(text__icontains = search_term)   
                
    get_dict_copy=request.GET.copy()
    params=get_dict_copy.pop('page',True) and get_dict_copy.urlencode()    
    paginator = Paginator(polls,5)
    page = request.GET.get('page')
    polls=paginator.get_page(page)
    context = {'polls':polls,'params':params,'search_term':search_term}
    return render(request,'polls/polls_list.html',context)
@login_required
def add_poll(request):
    form=PollForm()
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.pub_date=datetime.datetime.now()
            new_form.owner=request.user
            new_form.save()
            choice1=Choice(poll=new_form,choice_text=form.cleaned_data['choice1']).save()
            choice2=Choice(poll=new_form,choice_text=form.cleaned_data['choice2']).save()
            messages.success(request,"Poll and Choices Added!!",extra_tags="alert alert-warning alert-dismissible fade show")
            return redirect('polls:list')
            

    return render(request,'polls/add_polls.html',{'form':form})


@login_required
def polls_detail(request,poll_id):    
    poll=Poll.objects.get(id=poll_id)
    vote=not poll.user_can_vote(request.user)
    result=poll.get_results_dict()
    context={ 'poll':poll,'user_can_not_vote':vote ,'results':result}
    return render(request,'polls/polls_detail.html',context)    

@login_required
def poll_vote(request,poll_id):
    poll=get_object_or_404(Poll,id=poll_id)
    if not poll.user_can_vote(request.user):
        messages.error(request, 'You have voted already to this Pole!!!')
        return HttpResponseRedirect(reverse('polls:detail',args=(poll_id,)))

    choice_id=request.POST.get('choice',None)
    if choice_id:
       choice=Choice.objects.get(id=choice_id)
       user=request.user
       vote=Vote(user=user,poll=poll,choice=choice)
       vote.save()
       return HttpResponseRedirect(reverse('polls:detail',args=(poll_id,)))
    else:
        messages.error(request, 'Bad choice!!!')
        return HttpResponseRedirect(reverse('polls:detail',args=(poll_id,)))

@login_required
def edit_poll(request,poll_id):
    poll=get_object_or_404(Poll,id=poll_id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method=='POST':
        form=EditPollForm(request.POST,instance=poll)
        if form.is_valid():
            form.save()
            messages.success(request,"Poll edited successfully!!",extra_tags="alert alert-warning alert-dismissible fade show")
            return redirect('polls:list')
    else:
        form=EditPollForm(instance=poll)
    return render(request,'polls/edit_poll.html',{'form':form,'poll':poll})    

@login_required
def add_choice(request,poll_id):
    
    poll=get_object_or_404(Poll,id=poll_id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method=='POST':
        form=ChoiceForm(request.POST)
        if form.is_valid():
            choice=form.save(commit=False)
            choice.poll=poll
            choice.save()
            messages.success(request,"Choice added successfully!!",extra_tags="alert alert-warning alert-dismissible fade show")
            return redirect('polls:list')
    else:
        form=ChoiceForm()
    return render(request,'polls/add_choice.html',{'form':form,'poll':poll}) 

def edit_choice(request,choice_id):
    choice=get_object_or_404(Choice,id=choice_id)
    poll=get_object_or_404(Poll,id=choice.poll.id)
    if request.user != poll.owner:
        return redirect('/')
    if request.method=='POST':
        form=ChoiceForm(request.POST,instance=choice)
        if form.is_valid():
            choice.save()
            messages.success(request,"Choice edited successfully!!",extra_tags="alert alert-warning alert-dismissible fade show")
            return redirect('polls:list')
    else:
        form=ChoiceForm(instance=choice)
    return render(request,'polls/add_choice.html',{'form':form,'poll':poll,'edit_mode':True,'choice':choice})

def delete_choice(request,choice_id):
    choice=get_object_or_404(Choice,id=choice_id)
    if request.method=='POST':
        choice.delete()
        messages.success(request,"Choice deleted successfully!!",extra_tags="alert alert-warning alert-dismissible fade show")
        return redirect('polls:list')

    return render(request,'polls/delete_choice_confirm.html',{'choice':choice})   

def delete_poll(request,poll_id):
    poll=get_object_or_404(Poll,id=poll_id)
    if request.method=='POST':
        poll.delete()
        messages.success(request,"Poll deleted successfully!!",extra_tags="alert alert-warning alert-dismissible fade show")
        return redirect('polls:list')

    return render(request,'polls/delete_poll_confirm.html',{'poll':poll})          

