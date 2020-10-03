from django.urls import path

from grades import views

app_name = 'grades'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('reports/', views.reports, name='reports'),
    path(
        'student-detail/<int:student_id>',
        views.student_detail,
        name='student_detail'
    ),
    path(
        'student',
        views.student_delete,
        name='student_delete'
    )
]
