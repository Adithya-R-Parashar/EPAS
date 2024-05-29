from email import message
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmpForm, MetricForm
from django.http import HttpResponseRedirect
from .models import Employee, Metric
from django.urls import reverse
from .logic import start_sequence
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form (request):
    submitted = False
    if request.method == "POST":
        form = EmpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing')
    else:
        form = EmpForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'from.html', {'form' : form, 'submitted': submitted})

def datas(request):
    submitted = False
    if request.method == "POST":
        form = MetricForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form?submitted=True')
    else:
        form = MetricForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'data.html', {'form' : form, 'submitted': submitted})


def output(request):
    output = Employee.objects.all()
    context = {'output' : output}
    return render(request, 'output.html', context)


def emp_details(request, empno):
    employee = get_object_or_404(Employee, pk=empno)
    submitted = False
    if request.method == 'POST':
        form = MetricForm(request.POST)
        if form.is_valid():
            metric = form.save(commit=False)
            metric.empno = employee
            metric.save()
            return HttpResponseRedirect(str(reverse('empno', args=[empno])) + '?submitted=True')
    else:
        form = MetricForm()
        if 'submitted' in request.GET:
         submitted = True
    context = {'employee': employee, 'form': form, 'submitted': submitted}
    return render(request, 'emp.html', context)


def rating(request, empno):
    employee = get_object_or_404(Employee, empno=empno)
    metrics = Metric.objects.filter(empno=employee.empno)
    data = Metric.objects.filter(empno=employee.empno)
    im = Employee.objects.filter(empno=empno)
    ind_rating = []
    for metric in metrics:
        check_in = metric.check_in
        check_out = metric.check_out
        error_rate = metric.error_rate
        submission_status = metric.submission_status
        rating = start_sequence(check_in, check_out, error_rate, submission_status)
        ind_rating.append(rating)


    if ind_rating:
        average_rating = sum(ind_rating)/len(ind_rating)
    else:
        average_rating = 0
    context = {'average_rating' : average_rating, 'employee': employee, 'ind_rating': ind_rating, 'data': data, 'img': im}
    return render(request, 'rating.html', context)

def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'you are now registered ')
                return redirect('login')
        else:
            messages.error(request, 'Passwords did not match ')
    return render(request, 'registration/register.html')

def login_pg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request, 'Invalid username or password ')
    return render(request, 'registration/login.html')
        

def landing(request):
     if request.method == 'GET':
        queryset = Employee.objects.all()
        content = Employee.objects.all()
        query = request.GET.get('search')
        print(query)
        if query:
            queryset=queryset.filter(empno__icontains= query)
            context = {'employee' : queryset}
            return render(request, 'res.html', context)
        else:
            context = {'employee' : content}
            return render(request, 'landing.html', context)