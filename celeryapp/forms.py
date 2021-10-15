from django import forms
from .tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(label_suffix="",
        label='First Name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3','id': 'form-firstname'}))
    email = forms.EmailField(label="E-mail",label_suffix="",
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'id': 'form-email'}))
    review = forms.CharField(label="Your Review/Message",label_suffix="",
         widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    def send_email(self):
        print("-------form here--------------")
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])