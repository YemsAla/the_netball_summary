from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.db.models import Q 

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from match_reports.forms import MatchReportForm, CommentForm 

from .models import MatchReport, Comment


"""
List view for match reports, ordered by creation date.
Supports search by team name and filter by match type.
"""
def home(request):
    recent_reports = MatchReport.objects.all().order_by('-created_at')[:3]
    return render(request, 'match_reports/home.html', {
        'recent_reports': recent_reports,
    })

class ReportListView(ListView):
    model = MatchReport
    template_name = 'match_reports/report_list.html'
    context_object_name = 'reports'
    ordering = ['-created_at']
    paginate_by = 5    
    
    def get_queryset(self):
        queryset = MatchReport.objects.all().order_by('-created_at')
        query = self.request.GET.get('q')
        match_type = self.request.GET.get('match_type')

        if query:
            queryset = queryset.filter(
                Q(team_name__icontains=query) |
                Q(opponent_name__icontains=query)
            )
        if match_type:
            queryset = queryset.filter(match_type=match_type)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['match_type'] = self.request.GET.get('match_type', '')
        context['match_type_choices'] = MatchReport.MATCH_TYPE_CHOICES
        return context
    
"""
Detail view for a match report, including comments and comment form.
"""
class ReportDetailView(DetailView):
    model = MatchReport
    template_name = 'match_reports/report_detail.html'
    context_object_name = 'report'
    
    """
    Users can comment on an individual report, and the comments are displayed in reverse chronological order.
    """    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context
    
""" 
View for adding a comment to a match report. Only accessible to logged-in users.
"""
  
@login_required
def add_comment(request, pk):
    report = get_object_or_404(MatchReport, pk=pk)
        
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.match_report = report
            comment.save()
            messages.success(request, 'Your comment has been added.')
        else:
            messages.error(request, 'There was an error with your comment. Please try again.')
    return redirect('report_detail', pk=report.pk)
   

"""
View for creating a new match report. Only accessible to logged-in users.
When a report is successfully created, a success message is displayed.
"""  
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = MatchReport
    form_class = MatchReportForm
    template_name = 'match_reports/report_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your match report has been successfully created.')
        return super().form_valid(form)
    
    
"""
View for updating a match report - only accessible to report author"
"""
class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MatchReport
    form_class = MatchReportForm
    template_name = 'match_reports/report_form.html'

    def test_func(self):
        report = self.get_object()
        return report.user == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'You\'ve successfully updated your match report.')
        return super().form_valid(form)
    

"""
View for deleting a match report - only accessible to report author
"""
class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MatchReport
    template_name = 'match_reports/delete_report.html'
    success_url = '/reports/'
    
    def test_func(self):
        report = self.get_object()
        return report.user == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'You\'ve successfully deleted your match report.')
        return super().form_valid(form)
    
    
"""
View for registering a new user account
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to The Netball Summary, {user.username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
    
