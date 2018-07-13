from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    #每个通用视图需要知道它将作用于哪个模型,这由 model 属性提供
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        '''Excludes any questions that aren't published yet.
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #request.POST 类似字典的对象，包含所有给定的HTTP POST参数，前提是请求包含表单数据
        #The key 'choice' is from form's 'name' attribute
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button

        #reverse() 函数。这个函数避免了我们在视图函数中硬编码 URL
        return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))#args must be iterable,so it's a tuple

