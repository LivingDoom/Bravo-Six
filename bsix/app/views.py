from django.shortcuts import render
from django.utils.timezone import now
from app.forms import BenefitCheckForm
from app.eligibility_checkers import FoodAssistanceChecker, UnemploymentChecker
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def faq(request):
    return render(request, 'app/faq.html')

def welfare(request):
    return render(request, 'app/welfare.html')

def application(request):

    if request.method == 'POST':
        form = BenefitCheckForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            (eligible, testresults) = FoodAssistanceChecker.check(data)
            (ui_eligible, ui_testresults) = UnemploymentChecker.check(data)
            # if eligible:
            #     return HttpResponseRedirect('/bsix/results/')
            # else:
            #     return HttpResponseRedirect('/bsix/')

            return render(request, 'app/results.html', {
                    'eligible': eligible, 'tests': testresults,
                    'ui_eligible': ui_eligible, 'ui_tests': ui_testresults
                })
        else:
            print(form.errors)
    else:
        form = BenefitCheckForm()
    
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
            print(form.errors)
    else:
        form = BenefitCheckForm()
    
    return render(request, 'app/apply.html', {'form': form})
    
def unemploymentConfirmation(request):
    return render(request, 'app/unemploymentConfirmation.html')

def gettingStarted(request):
    return render(request, 'app/gettingStarted.html')

def createAccount(request):
    return render(request, 'app/createAccount.html')