from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from crud.models import choice, question
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic

from . models import question, choice


# template = loader.get_template('crud/index.html')
    # context = {
    #     'question_list': question_list,
    # }
    # return HttpResponse(template.render(context, request))
class IndexView(generic.ListView):
    template_name = "crud/index.html"
    context_object_name = "question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return question.objects.all()


    # try:
    #     question_list = question.objects.get(pk=question_id)
    # except Exception as e:
    #         raise Http404('Question not exist')
    #
    # template = loader.get_template('crud/detail.html')
    # context = {
    #     'question_list': question_list
    # }
    # return HttpResponse(template.render(context, request))

class DetailView(generic.DetailView):
    model = question
    template_name = "crud/detail.html"

# q = get_object_or_404(question, pk=question_id)
#     return render(request, "crud/result.html", {"question": q})
class ResultsView(generic.DetailView):
    model = question
    template_name = "crud/result.html"

def votes(request, question_id):
    q = get_object_or_404(question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'crud/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('crud:results', args=(q.id,)))



