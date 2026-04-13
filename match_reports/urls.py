from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('report/<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('report/<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('report/create/', views.ReportCreateView.as_view(), name='report-create'),
]