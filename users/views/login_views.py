from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        print("POST recebido:", request.POST)

        email = request.POST.get("email")
        password = request.POST.get("senha_custom") 

        print(f"Email recebido: {email}")
        print(f"Senha recebida: {password}")

        user = authenticate(request, username=email, password=password)
        print("Resultado do authenticate:", user)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            print("Login bem-sucedido:", user)

            if user.user_type == "PAT":
                  return redirect("homepage")
            elif user.user_type == "STD" or user.user_type == "PSY":
                return redirect("psychologist-dashboard")
        else:
            messages.error(request, "E-mail ou senha incorretos.")
            print("Falha no login.")

    return render(request, "users/login.html")
