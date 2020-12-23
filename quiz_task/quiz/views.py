from django.shortcuts import render
from .models import questions
from .forms import questionForm
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


# Entry.objects.get(pk=1)
def home_view(request):
    available_quizes=questions.objects.all()
    topics=set()
    for i in available_quizes:
        topics.add(i.__dict__["quiz_name"])
    print(topics)

    return render(request,"index.html",{"topics":topics})

def take_quiz(request,name):
    qns=questions.objects.filter(quiz_name=name)
    
    data=[]
    for i in qns:
        data.append(i.__dict__)
    print()

    print(data,"--------------------------------------------------------------")
    return render(request,"take_quiz.html",{"qns":data})
def add_question(request,name=""):
    form=questionForm()
    if request.method=='POST':
        print("in post adding question")
        temp=questionForm(request.POST)
        qn=temp.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/")
    else:
        return render(request,"add_question.html",{"form":form,"name":name})
    return render(request,"add_question.html",{"form":form,"name":name})