from django import forms
from .models import MatchReport, Comment


"""
Form fields for adding a match report
"""

class MatchReportForm(forms.ModelForm):
    class Meta:
        model = MatchReport
        fields = ['title', 'team_name', 'opponent_name', 'team_score', 
                  'opponent_score', 'match_report', 'image', 'player_of_match', 
                  'opponent_player_of_match', 'match_date', 'match_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'team_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'opponent_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'team_score': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'opponent_score': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'match_report': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'required': False}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'player_of_match': forms.TextInput(attrs={'class': 'form-control'}),
            'opponent_player_of_match': forms.TextInput(attrs={'class': 'form-control'}),
            'match_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': False}),
            'match_type': forms.Select(attrs={'class': 'form-select', 'required': True}),
        }


"""
Comment form for adding comments to a match report
""" 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
        
