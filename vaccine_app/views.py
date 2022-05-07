from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from vaccine_app.forms import LoginRegister, UserRegistration, Vaccine_Add, NurseRegistration, HospitalRegistration
from vaccine_app.models import Vaccine, User, Nurse, Hospital


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_user:
                return redirect('user_home')
            elif user.is_nurse:
                return redirect('nurse_home')
        else:
            messages.info(request,'invalid credentials')
    return render(request, 'login.html')


def nurse_registration(request):
    login_form=LoginRegister()
    nurse_form=NurseRegistration()
    if request.method=='POST':
        login_form=LoginRegister(request.POST)
        nurse_form=NurseRegistration(request.POST)
        if login_form.is_valid and nurse_form.is_valid():
            user=login_form.save(commit=False)
            user.is_nurse=True
            user.save()
            nurse = nurse_form.save(commit=False)
            nurse.user = user
            nurse.save()
            messages.info(request,'nurse registration successful')
            return redirect('login_view')
    return render(request, 'nurse_registration.html',{'login_form':login_form,'nurse_form':nurse_form})


def user_registration(request):
    login_form = LoginRegister()
    user_form = UserRegistration()
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = UserRegistration(request.POST)
        if login_form.is_valid and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            u = user_form.save(commit=False)
            u.user = user
            u.save()
            messages.info(request, 'user register successful')
            return redirect('login_view')
    return render(request, 'user_registration.html', {'login_form': login_form, 'user_form': user_form})


def admin_home(request):
    return render(request, 'admin_home.html')


def nurse_home(request):
    return render(request, 'nurse_home.html')


def user_home(request):
    return render(request, 'user_home.html')


def vaccine_add(request):
    form = Vaccine_Add()
    if request.method == 'POST':
        form = Vaccine_Add(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'vaccine added successfully')
            return redirect('vaccine_add')
    return render(request, 'vaccine_add.html', {'form': form})


def vaccine_view(request):
    dataset = Vaccine.objects.all()
    print(dataset)
    context = {
        'data': dataset
    }
    return render(request, 'vaccine_view.html', context)


def vaccine_update(request, id):
    obj = Vaccine.objects.get(id=id)
    form = Vaccine_Add(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('vaccine_view')
    else:
        form=Vaccine_Add(instance=obj)
    return render(request, 'vaccine_update.html', {'form': form})


def vaccine_delete(request,id):
    obj=get_object_or_404(Vaccine,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('vaccine_view')
    return render(request,'vaccine_delete.html')

def user_view(request):
    u=User.objects.all()
    print(u)
    context={
        'u':u
    }
    return render(request,'user_view.html',context)

def nurse_view(request):
    dataset=Nurse.objects.all()
    print(dataset)
    context={
        'data':dataset
    }
    return render(request,'nurse_view.html',context)


def hospital_add(request):
    form=HospitalRegistration()
    if request.method=='POST':
        form=HospitalRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'hospital registration successful')
            return redirect('hospital_add')
    return render(request,'hospital_add.html',{'form':form})

def hospital_view(request):
    h=Hospital.objects.all()
    print(h)
    context={
        'h':h
    }
    return render(request,'hospital_view.html',context)

def hospital_update(request, id):
    obj = Hospital.objects.get(id=id)
    form = HospitalRegistration(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('hospital_view')
    else:
        form=HospitalRegistration(instance=obj)
    return render(request, 'hospital_update.html', {'form': form})

def hospital_delete(request,id):
    obj=get_object_or_404(Hospital,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('hospital_view')
    return render(request,'hospital_delete.html')

