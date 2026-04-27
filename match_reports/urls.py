from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('reports/', views.ReportListView.as_view(), name='report_list'),  
    path('reports/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('reports/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('reports/create/', views.ReportCreateView.as_view(), name='report-create'),
    path('reports/<int:pk>/update/', views.ReportUpdateView.as_view(), name='report-update'),
]