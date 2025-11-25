from django.urls import path
from . import views

urlpatterns= [
    
    path("login/", views.login_view, name="login"),

    path("register/", views.select_register, name="select_register"),

    path("register/student/", views.register_student, name="student_register"),
    
    path("register/psy/", views.register_psychologist, name="psy_register"),
    
    path("register/patient/", views.patient_register, name="patient_register"),
    
    path("logged/homepage/", views.Homepage, name="homepage"),
        
    path("logged/forget_password/", views.Forget_password, name="forget_password"),
    
    path("logged/consulta/", views.Consulta, name="consulta"),

    path("registered/", views.confirmacao_registro, name="registered"),

    path("logged/psychologist-dashboard/", views.psicologo_dashboard, name="psychologist-dashboard"),

    path("logged/consultas-marcadas/", views.consultas_marcadas, name="consultas-marcadas"),

    path("logged/psicologo-agenda/", views.psicologo_agenda, name="psicologo-agenda"),

    path("logged/psicologo-anotacoes/", views.psicologo_anotacoes, name="psicologo-anotacoes"),

    path("logged/psicologo-configuracoes", views.configuracoes, name="configuracoes"),
    
    path("logged/historico/", views.historico, name="historico"),

    path("logged/delete-account/", views.delete_account, name="delete_account"),

    path("logged/reclamacoes/", views.reclamacoes, name="reclamacoes"),


]