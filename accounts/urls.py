from . import views
from django.urls import path
urlpatterns=[
    path("login/",views.LoginUserView.as_view(),name="login_page"),
    path("register/",views.register_view,name="register_page"),
    path("logout/",views.LogoutUserView.as_view(),name="logout"),
    path("change_password/",views.ChangePasswordView.as_view(),name="passwordchange"),
]