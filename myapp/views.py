from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult
# Create your views here.



# ---- assuming task with delay() method ---

def index(request):
      result = add.delay(10,20)
      return render(request, 'myapp/home.html', {'result': result })


def check_result(request, task_id):
      result = AsyncResult(task_id)
      return render(request, 'myapp/result.html', {'result': result})

# def index(request):
#       print("Result : ")
      
#       result1 = add.delay(10,20)
#       print("Result 1 : ", result1)

#       result2 = sub.delay(100,20)
#       print("Result 2 of sub : ", result2)

#       return render(request, 'myapp/home.html')


# --- Enqueue Tast Using apply_async() --- 

# def index(request):
#       print("Result : ")
      
#       result1 = add.apply_async(args=[10,20])
#       print("Result 1 : ", result1)

#       result2 = sub.apply_async(args=[100,20])
#       print("Result 2 of sub : ", result2)

#       return render(request, 'myapp/home.html')


def about(request):
      return render(request, 'myapp/about.html')

def contact(request):
      return render(request, 'myapp/contact.html')