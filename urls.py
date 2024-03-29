from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse

app_name = 'initiatives'
urlpatterns = [
    # /initiatives/

    path('user_login/', views.user_login, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.IndexView.as_view(), name='home'),
    path('initiatives/', views.InitiativesView.as_view(), name='initiatives'),
    path('leaders/', views.LeadersView.as_view(), name='leaders'),
    path('messages/', views.EnquiryView.as_view(), name='messages'),
    path('initiatives/<int:pk>/', views.WeekReportView.as_view(), name='reports'),
    path('initiatives/<int:id>/<week_no>/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('initiatives/<int:id>/<week_no>/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment-add',

         ),
]

