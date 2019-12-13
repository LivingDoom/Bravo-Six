

class FoodAssistanceChecker():

    def check(self, data, userProfile):

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
       
        hh_size = data.get('household_size')

        if data.get('disability_status'):
            # Just column D
            if hh_size <= 11:
                if data.get('income') / 12 <= table[hh_size - 1][3]:
                    return True
            else:
                d = 7610 + (594 * (hh_size - 11))
                if data.get('income') / 12 <= d:
                    return True
                else:
                    return False
        elif data.get('household_has_senior') or data.get('household_has_disabled'):
            # Just column C
            if hh_size <= 11:
                if data.get('income') * 0.769 / 12 <= table[hh_size - 1][2]:
                    # Note: .769 appears to be a magic-ish number that's used in the
                    # government numbers, so we're using it here
                    return True
                else:
                    return False
            else:
                if data.get('income') * 0.769 / 12 <= table[hh_size - 1][2]:
                    return True
                else:
                    return False
        else:
            # Columns B and C
            # TODO: Implement
            return False


