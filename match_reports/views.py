from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import messages 
# from django import Q 

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from match_reports.forms import MatchReportForm, commentForm

from .models import MatchReport, Comment


"""
List view for match reports, ordered by creation date and paginated
to show 5 reports per page.
"""
class ReportListView(ListView):
    model = MatchReport
    template_name = 'match_reports/report_list.html'
    context_object_name = 'reports'
    ordering = ['-created_at']
    paginate_by = 5
    
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
        context['comment_form'] = commentForm()
        return context
    
""" 
View for adding a comment to a match report. Only accessible to logged-in users.
"""
  
@login_required
def add_comment(request, pk):
    report = get_object_or_404(MatchReport, pk=pk)
        
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.match_report = report
            comment.save()
            messages.success(request, 'Your comment has been added.')
        else:
            messages.error(request, 'There was an error with your comment. Please try again.')
    return redirect('report-detail', pk=report.pk)
   

"""
View for creating a new match report. Only accessible to logged-in users.
When a report is successfully created, a success message is displayed to the user.
"""  
class ReportCreateView(LoginRequiredMixin, CreateView):
    model = MatchReport
    form_class = MatchReportForm
    template_name = 'match_reports/report_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your match report has been successfully created.')
        return super().form_valid(form)