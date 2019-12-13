from django import forms


class BenefitCheckForm(forms.Form):
    # General info
    full_name = forms.CharField(label='Your full name', max_length=100)
    dob = forms.DateField(label='Date of birth')
    street_address = forms.CharField(label='Street address', max_length=100)
    city = forms.CharField(label='City', max_length=30)
    state = forms.CharField(label='State', max_length=2)
    zipcode = forms.IntegerField(label="ZIP Code",)
    income = forms.IntegerField(label='Annual gross income')
    monthly_net = forms.IntegerField(label='Monthly net income')


    disability_status = forms.BooleanField(label='Do you have a disability?', required=False)
    household_size = forms.IntegerField(min_value=1, help_text='Include yourself')
    household_has_senior = forms.BooleanField(label='Does anyone 60+ years old (excluding yourself) live in your household?', required=False)
    household_has_disabled = forms.BooleanField(label='Does anybody in your household (excluding yourself) have a disability?', required=False)

    # Employment
    unemployed = forms.BooleanField(label='Are you currently unemployed or have your hours been involuntarily reduced?', required=False)
    work_in_state = forms.BooleanField(label='Have you worked in Washington in the past 18 months?', required=False)
    hours_check = forms.BooleanField(label='Have you worked at least 680 hours in the past 12 months?', required=False)
    hours_in_state = forms.BooleanField(label='If yes, were some of those wages earned in Washington?', required=False)
    on_leave_or_working = forms.BooleanField(label='Are you currently on a leave of absence or have lost one day or less per week of full-time work?', required=False)

    # Food Assistance
    unable_own_meals = forms.BooleanField(label='Are you 60+ years of age and unable to cook your own meals?', required=False)
    ### Get col C question (other elderly/disabled) from above

    # Housing Assistance (HEN)
    unable_work = forms.BooleanField(label='Are you unable to work for at least 90 days due to mental or physical incapacity?', required=False)

    ### These questions make someone ineligible
    pwa_tanf_eligible = forms.BooleanField(label='Are you eligible for Pregnant Women Assistance (PWA) or Temporary Assistance to Needy Families (TANF)?', required=False)
    federal_aid_pursuit = forms.BooleanField(label='Have you pursued federal aid assistance (such as Medicaid) unless there is good cause to not?', required=False)
    subs_abuse_treatment = forms.BooleanField(label='If required, have you participated in substance use disorder treatment, unless there is good cause to not?', required=False)
    ssi_eligibility = forms.BooleanField(label='Are you eligible for SSI benefits or are you an ineligible spouse of an SSI recipient?', required=False)
    ssa_termination = forms.BooleanField(label='Has the Social Security Administration denied or terminated benefits to you due to a failure to follow program rules?', required=False)

