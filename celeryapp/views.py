
from django.views.generic.edit import FormView
from .forms import ReviewForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.



class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "review.html"

    def form_valid(self, form):
        print("---------form valid---------")
        form.send_email()
        # name = form.cleaned_data['name']
        # email = form.cleaned_data.get('email')
        # review = form.cleaned_data.get('review')

        # send_mail.delay(name,email,review)
        
        messages.success(self.request,"Thank you for your response!!")
        return HttpResponse("Thank you for your Review")

        

    def form_invalid(self, form):
        messages.warning(self.request,"Form Invalid, Try Again")
        return HttpResponse("Thank you for your Review")
