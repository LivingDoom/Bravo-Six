

class FoodAssistanceChecker():
    
    @staticmethod
    def check(data):

        # #members, Max Monthly Gross Income, Max Monthly Net Income, 165% Poverty Level
        table = [
            [1,1316,1012,1670],
            [2,1784,1352,2264],
            [3,2252,1732,2858],
            [4,2720,2092,3452],
            [5,3188,2452,4046],
            [6,3656,2812,4640],
            [7,4124,3172,5234],
            [8,4592,3532,5828],
            [9,5060,3892,6422],
            [10,5528,4252,7016],
            [11,5996,4612,7610],
        ]

        tests = []

        pwa_tanf_eligible = data.get('pwa_tanf_eligible')
        if pwa_tanf_eligible:
            tests.append((False, "You're eligible for Pregnant Women Assistance (PWA) or Temporary Assistance for Needy Families (TANF)"))
            return (False, tests)
        else:
            tests.append((True, "You're not eligible for Pregnant Women Assistance (PWA) or Temporary Assistance for Needy Families (TANF)"))
       
        hh_size = data.get('household_size')

        if data.get('disability_status'): # best chance to fall in income range
            # Just column D
            d = table[hh_size - 1][3] if (hh_size <= 11) else 7610 + (594 * (hh_size - 11))
            self_dis_income_threshold = data.get('income') / 12 <= d
            
            if self_dis_income_threshold:
                tests.append((True, "You meet the income threshold for a disabled individual"))
                return (True, tests)
            else:
                tests.append((False, "You exceed the income threshold for a disabled individual"))
                return (True, tests)

        elif data.get('household_has_senior') or data.get('household_has_disabled'):
            # Just column C
            c = table[hh_size - 1][2] if (hh_size <= 11) else 4612 + (360 * (hh_size - 11))
            house_sr_or_dis = data.get('monthly_net') <= c

            if house_sr_or_dis:
                tests.append((True, "You meet the income threshold for a household with a senior or disabled individual"))
                return (True, tests)
            else:
                tests.append((False, "You exceed the income threshold for a household with a senior or disabled individual"))
                return (False, tests)
        else:
            # Columns B and C
            b_max = table[hh_size - 1][1] if (hh_size <= 11) else 5996 + (468 * (hh_size - 11))
            c_max = table[hh_size - 1][2] if (hh_size <= 11) else 4612 + (360 * (hh_size - 11))

            b_met = (data.get('income') / 12) < b_max
            c_met = data.get('monthly_net') < c_max

            if b_met:
                tests.append((True, "You meet the monthly gross income threshold for a household with a no senior or disabled individuals"))
            else:
                tests.append((False, "You exceed the monthly gross income threshold for a household with a no senior or disabled individuals"))

            if c_met:
                tests.append((True, "You meet the monthly net income threshold for a household with a no senior or disabled individuals"))
            else:
                tests.append((False, "You exceed the monthly gross income threshold for a household with a no senior or disabled individuals"))

            return (b_met and c_met, tests)


class UnemploymentChecker():

    @staticmethod
    def check(data):

        tests = []

        unemployed = data.get('unemployed')
        worked_in_wa = data.get('work_in_state')
        hours = data.get('hours_check')
        hours_in_state = data.get('hours_in_state')
        loa_or_working = data.get('on_leave_or_working')

        if unemployed:
            tests.append((True, "You are currently unemployed or have had your hours reduced"))
        else:
            tests.append((False, "You are not currently unemployed and have not had your hours reduced"))

        if worked_in_wa:
            tests.append((True, "You have worked in Washington in the past 18 months"))
        else:
            tests.append((False, "You have not worked in Washington in the past 18 months"))
        
        if hours:
            tests.append((True, "You have worked at least 680 hours in your base year"))
        else:
            tests.append((False, "You have not worked at least 680 hours in your base year"))
        
        if hours_in_state:
            tests.append((True, "You earned some of those wages in Washington"))
        else:
            tests.append((False, "You did not earn any of those wages in Washington"))
        
        if loa_or_working:
            tests.append((False, "You are on a leave of absence or have lost one day or less per week of work"))
        else:
            tests.append((True, "You are not on a leave of absence and have lost more than one day per week of work"))

        return (unemployed and worked_in_wa and hours and hours_in_state and not loa_or_working, tests)