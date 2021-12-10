from django.contrib import admin
from django.urls import path

from app.views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('blogs/', blogs, name='blogs'),
    path('addBlog/', addBlog, name='addBlog'),
    path('blogDetails/<int:blog_id>', blogDetails, name='blogDetails'),

    
    path('approve/<int:user_id>', approve, name='approve'),
    path('refuse/<int:user_id>', refuse, name='refuse'),

]
