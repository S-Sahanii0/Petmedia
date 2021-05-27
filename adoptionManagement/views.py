from django.shortcuts import render, redirect
from .models import Requests
from account.models import Account
from .forms import DogForm, RegForm
from django.contrib.auth.models import User
from adoptionManagement.models import Dog, AdoptionQueue
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage

@login_required(login_url='login')
def uploadDog(request):

    form = DogForm()
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'adoptionManagement/upload.html', context)

def displayDog(request):

    dog = Dog.objects.all()
    if request.GET:
        query = request.GET['q']
        dog = get_dog_queryset(str(query))
        
    context = {'dog': dog}
    
    return render(request, 'adoptionManagement/home.html', context)

@login_required(login_url='login')
def updateDog(request, pk):

    dog = Dog.objects.get(id=pk)
    form = DogForm(instance=dog)
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES, instance=dog)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'adoptionManagement/upload.html', context)

@login_required(login_url='login')
def deleteDog(request, pk):
    dog = Dog.objects.get(id=pk)
    if request.method == 'POST':
        dog.delete()
        return redirect('/')
    context = {'dog': dog}
    return render (request, 'adoptionManagement/delete.html', context)

# def requestDog(request, pk):
#     dog = Dog.objects.filter(id=pk)[0]
#     if dog.status ==True:
#         dog.status = False
#         dog.save()
#         r = Requests(user = request.user)
#         r.dog = request.dog
#         r.is_requested = True
#         r.save()
#         return redirect('/')
    
#     return render (request, 'adoptionManagement/home.html', {})

@login_required(login_url='login')
def registerDog(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST, request.FILES)
        if form.is_valid():
            queue = form.save(commit=False)
            queue.user = request.user
            queue.save()
            return redirect('/')
    context = {'regform': form}
    return render(request, 'adoptionManagement/adoptionQueue.html', context)

@login_required(login_url='login')
def displayRegistration(request):
    queue = AdoptionQueue.objects.all()
    
    context = {'registrations':queue}
    return render(request, 'adoptionManagement/registrations.html', context)

@login_required(login_url='login')
def acceptRegistration(request, pk):
    queue = AdoptionQueue.objects.get(id=pk)
    if request.method == 'POST':
        # queue = AdoptionQueue.objects.get(id=pk)
        email = queue.user.email
        send_mail(
            'Pet Registration Info',
            'Your request for registering the dog at the center has been accepted',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False

        )
        queue.delete()
        return redirect('/')
    context = {'queue':queue}
    return render(request, 'adoptionManagement/accept.html', context)

@login_required(login_url='login')
def requestDog(request, pk=None):
    dog = Dog.objects.filter(id=pk)[0]
    
    
    r = Requests()
    r.user = request.user
    r.dog = dog
    r.is_requested = True
    try:
        r.save()
        messages.info(request, 'Your request has been sent!')
        
    except IntegrityError as e:
        messages.info(request, 'This dog has already been booked!')

    return redirect('/')
    dog = Dog.objects.filter(id=pk)
    
    return render(request, "adoptionManagement/home.html", {'dog':dog})

@login_required(login_url='login')
def cancelRequest(request, pk = None):
    req = Requests.objects.filter(id=pk)[0]
    dog_id = req.dog.id
    dog = Dog.objects.filter(id = dog_id)[0]
    if request.method == 'POST':
        
           
            req.save()
            print(dog.breed_name)
            req.delete()
           
           
            return redirect('/')

        
    
    return render(request, "adoptionManagement/cancelReq.html", {'req':req})


@login_required(login_url='login')
def displayRequest(request):
    
    requested = Requests.objects.all()
    context = {'requests': requested}
    return render(request, "adoptionManagement/requests.html", context)

@login_required(login_url='login')
def clientRequest(request):
    user = request.user
    try:
        
        requested = Requests.objects.filter(user = user)

    except Requests.DoesNotExist:
        requested = None
        
    
    context = {'requests': requested}
    return render(request, "adoptionManagement/client_req.html", context)

@login_required(login_url='login')
def acceptRequest(request, pk):
    req = Requests.objects.filter(id=pk)[0]
    if request.method == 'POST':
        # queue = AdoptionQueue.objects.get(id=pk)
        email = req.user.email
        send_mail(
            'Pet Adoption Acceptance',
            'Your request for adopting the dog has been accepted. You may now come to pick the dog.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False

        )
        req.delete()
        name = req.dog.breed_name
        dog = Dog.objects.filter(breed_name = name)
        dog.delete()
        return redirect('/')
    context = {'req':req}
    return render(request, 'adoptionManagement/reqAccept.html', context)

@login_required(login_url='login')
def declineRequest(request, pk):
    req = Requests.objects.filter(id=pk)[0]
    if request.method == 'POST':
        # queue = AdoptionQueue.objects.get(id=pk)
        email = req.user.email
        send_mail(
            'Pet Adoption Acceptance',
            'Sorry, Your request for adopting the dog has been declined.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False

        )
        req.delete()
        return redirect('/')
    context = {'req':req}
    return render(request, 'adoptionManagement/reqDecline.html', context)


def get_dog_queryset(query = None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        dogs = Dog.objects.filter(
            Q(breed_name__icontains = q)
        ).distinct()

        for dog in dogs:
            queryset.append(dog)

    return list(set(queryset)) #unique list

def searchResult(request):
    query = ""
    # context = {}
    if request.GET:
        query = request.GET['q']
        
    dog = get_dog_queryset(str(query))
    context = {'dog': dog}

    return render(request, "adoptionManagement/searchResult.html", context)

# def scanner(request):
#     print('this view called')

#     if request.method == 'POST':
#         print("please")
#         print(request.FILES)
#         fileObj = request.FILES.get('dog')
#         print("please" +fileObj.name)
#         fs = FileSystemStorage()
#         filePathName = fs.save(fileObj.name, fileObj)
#         filePathName = fs.url(filePathName)
#         print(filePathName)
#         context = {'filePathName': filePathName}
#         return render(request, 'adoptionManagement/scanner.html', context)
#     else:
#         return render(request, 'adoptionManagement/scanner.html')

# def prediction(request):
#     if request.method == 'POST':
#         print("please")
#         fileObj = request.FILES['dog']
#         print("please" +fileObj.name)
#         fs = FileSystemStorage()
#         filePathName = fs.save(fileObj.name, fileObj)
#         filePathName = fs.url(filePathName)
#         print(filePathName)
#         context = {'filePathName': filePathName}
#         return render(request, 'adoptionManagement/scanner.html', context)