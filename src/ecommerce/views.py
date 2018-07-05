from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate,login, get_user_model


def home_page(request):
    context={
        "title": "home_page",
        "content":"Welcome to the home page",
    }

    if request.user.is_authenticated:
        context["premium_content"]="Yeah"
    return render(request,"home_page.html", context)



def about_page(request):
    context= {
        "title": "about",
        "content":"Welcome to the about page"
    }
    return render(request, "home_page.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    print("User logged in")
    print(request.user.is_authenticated())

    context = {
        'form': form
    }
    if form.is_valid():
        context['form']=LoginForm()
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")
    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {
        'form': form
    }
    if form.is_valid():
        context['form'] = RegisterForm()
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)

    return render(request, "auth/register.html", context)


def contact_page(request):

    contact_form=ContactForm(request.POST or None)
    context = {
        "title": "contact",
        "content":" Welcome to the contact page",
        "form":contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
            errors = contact_form.errors.as_json()
            if request.is_ajax():
                return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))

    return render(request, "contact/view.html", context)

