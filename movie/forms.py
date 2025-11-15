from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    desc = forms.CharField(widget=forms.Textarea)
    genre = forms.CharField(max_length=50)
    date = forms.CharField(max_length=16)
    image = forms.FileField()
    author = forms.CharField(max_length=100)
    duration = forms.CharField(max_length=10)
    class Meta():
        pass
