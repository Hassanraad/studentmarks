from django.urls import path
from .views  import grades,show,subjects,marks
from .views import login,signup
urlpatterns = [
    path('marks/',marks,name='marks'),
    path('show/',show,name='show'),
    path('subjects/',subjects,name='subjects'),
    path('grades/',grades,name='grades') ,     
    path('login/',login, name='login'),
    path('slider/',signup, name='slider')
]