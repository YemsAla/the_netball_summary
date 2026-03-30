from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MatchReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    team_name = models.CharField(max_length=100)
    opponent_name = models.CharField(max_length=100)
    team_score = models.IntegerField()
    opponent_score = models.IntegerField()
    match_report = models.TextField()
    player_of_match = models.CharField(max_length=100)
    opponent_player_of_match = models.CharField(max_length=100)
    match_date = models.DateField()
    match_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match_report = models.ForeignKey(MatchReport, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user}'
