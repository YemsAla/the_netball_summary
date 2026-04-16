from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),  # this becomes /reports/
    path('<int:pk>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('<int:pk>/comment/', views.add_comment, name='add-comment'),
    path('create/', views.ReportCreateView.as_view(), name='report-create'),
]