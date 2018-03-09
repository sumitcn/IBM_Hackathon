
from django.conf.urls import url
from views import recordAudio ,main ,home 


urlpatterns = [
  url(r'^$',home,name="hm"),
  #url(r'^post/',postmodel,name='postmodel'),
  url(r'^record/',recordAudio,name='record'),
  url(r'^emotion/',main,name='main'),
 
]