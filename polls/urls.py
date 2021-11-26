from django.urls import path
from . import views

app_name='polls'

urlpatterns = [
  path('', views.index, name = 'index'),
  path('<int:question_id>/', views.detail, name = 'detail'),
  path('<int:question_id>/results/', views.results, name = 'results'),
  path('<int:question_id>/vote/', views.vote, name = 'vote'),
  path('signin/', views.signin, name = 'signin'),
  path('signup/', views.signup, name = 'signup'),
  path('book/', views.book, name = 'book'),
  path('book/list/', views.bookList, name = 'list'),
  path('book/detail/<int:book_id>/', views.bookDetail, name = 'detail'),
  path('book/create/', views.bookCreate, name = 'create'),
  path('book/update/', views.bookUpdate, name = 'update'),
  path('book/delete/', views.bookDelete, name = 'delete'),
  path("addbeast/", views.addbeast,  name='addbeast'),
  # path("success/", views.success,  name='success')
]