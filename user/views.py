from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


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

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.info(request, "Kullanıcı adı veya parola hatalı!")
            return render(request, "login.html", context)
        messages.success(request, "Başarıyla giriş yaptınız!")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız!")
    return redirect("index")