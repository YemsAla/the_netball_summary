from django import forms
from .models import MatchReport, Comment


"""
Form fields for adding a match report
"""
class MatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ['title', 'team_name', 'opponent_name', 'team_score', 'opponent_score', 'match_report', 'image', 'player_of_match', 'opponent_player_of_match', 'match_date', 'match_type']
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'}),
        }

"""
Comment form for adding comments to a match report
"""
        
class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
        
