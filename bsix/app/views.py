from django.shortcuts import render
from app.forms import BenefitCheckForm
from app.eligibility_checkers import FoodAssistanceChecker
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def faq(request):
    return render(request, 'app/faq.html')

def welfare(request):
    return render(request, 'app/welfare.html')

def application(request):
    return render(request, 'app/application.html')

def apply(request):

    if request.method == 'POST':
        form = BenefitCheckForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = FoodAssistanceChecker().check(data, None)

            if result:
                return HttpResponseRedirect('/bsix/results/')
            else:
                return HttpResponseRedirect('/bsix/')
    else:
        form = BenefitCheckForm()
    
    return render(request, 'app/apply.html', {'form': form})
    
def unemploymentConfirmation(request):
    return render(request, 'app/unemploymentConfirmation.html')
