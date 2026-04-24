from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.
class MatchReport(models.Model):
    MATCH_TYPE_CHOICES = [
        ('league', 'League'),
        ('friendly', 'Friendly'),
        ('tournament', 'Tournament'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    team_name = models.CharField(max_length=100)
    opponent_name = models.CharField(max_length=100)
    team_score = models.IntegerField()
    opponent_score = models.IntegerField()
    match_report = models.TextField()
    image = models.ImageField(upload_to='match_reports/', blank=True, null=True)
    player_of_match = models.CharField(max_length=100, blank=True, null=True)
    opponent_player_of_match = models.CharField(max_length=100, blank=True, null=True)
    match_date = models.DateField()
    match_type = models.CharField(max_length=50, choices=MATCH_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('report_detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match_report = models.ForeignKey(MatchReport, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.match_report}'
