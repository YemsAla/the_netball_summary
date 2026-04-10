from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import messages 
# from django import Q 

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import MatchReport, Comment

class ReportListView(ListView):
    model = MatchReport
    template_name = 'match_reports/report_list.html'
    context_object_name = 'reports'
    ordering = ['-created_at']
    paginate_by = 5

