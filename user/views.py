from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def register(request):
    # POST request: Bir web sunucusuna yeni bilgiler göndermek için kullanılan request türüdür.
    # GET request: Bir web sunucusundan belirli bir kaynağı almak için kullanılan request türüdür.
    form = RegisterForm(request.POST or None)
    if form.is_valid(): # Eğer form validasyonu(şifre ve kullancı adı girildi mi? şifreler eşleşiyor mu?) sağlanırsa aşağıdaki kodları çalıştır.
        username = form.cleaned_data.get("username") # POST request olursa kullanıcının forma girdiği kullanıcı adını çekiyoruz.
        password = form.cleaned_data.get("password") # Aynı şekilde şifreyi de çekiyoruz.

        newUser = User(username = username) # User class'ından bir kullanıcı oluşturduk.
        newUser.set_password(password) # Kullanıcının şifresi veritabanına şifrelenerek kaydedildi.
        newUser.save() # Kullanıcının kaydedilmesi.
        login(request, newUser) # Kayıt olduktan sonra login işlemi otomatik olarak gerçekleşecek.
        messages.info(request, "Başarıyla kayıt oldunuz.")
        return redirect("index")  # Kayıt olduktan sonra kullanıcı otomatik olarak anasayfaya yönlendirilecek.
    context = {
            "form": form
        }
    return render(request, "register.html", context)

    """if request.method == "POST": # Eğer gelen request POST ise aşağıdaki kodları çalıştır. 
        form = RegisterForm(request.POST) # RegisterForm class'ından form objesi oluşturduk.
        if form.is_valid(): # Eğer form validasyonu(şifre ve kullancı adı girildi mi? şifreler eşleşiyor mu?) sağlanırsa aşağıdaki kodları çalıştır.
            username = form.cleaned_data.get("username") # POST request olursa kullanıcının forma girdiği kullanıcı adını çekiyoruz.
            password = form.cleaned_data.get("password") # Aynı şekilde şifreyi de çekiyoruz.

            newUser = User(username = username) # User class'ından bir kullanıcı oluşturduk.
            newUser.set_password(password) # Kullanıcının şifresi veritabanına şifrelenerek kaydedildi.
            newUser.save() # Kullanıcının kaydedilmesi.
            login(request, newUser) # Kayıt olduktan sonra login işlemi otomatik olarak gerçekleşecek.
            return redirect("index")  # Kayıt olduktan sonra kullanıcı otomatik olarak anasayfaya yönlendirilecek.
        context = {
            "form": form
        }
        return render(request, "register.html", context)

    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "register.html", context)"""

def loginUser(request):
    return render(request, 'login.html')

def logoutUser(request):
    pass