from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Review
        fields = ('review', 'score',)
