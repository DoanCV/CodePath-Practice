class Solution:
    def reformatDate(self, date: str) -> str:
        month_dict = {'Jan':'01',
                      'Feb':'02',
                      'Mar':'03',
                      'Apr':'04',
                      'May':'05',
                      'Jun':'06',
                      'Jul':'07',
                      'Aug':'08',
                      'Sep':'09',
                      'Oct':'10',
                      'Nov':'11',
                      'Dec':'12'
                     }
        
        date_list = date.split()
        date_string = ""
        
        # add the year
        date_string = date_string + date_list[2] + "-"
        
        # add the month
        date_string = date_string + month_dict[date_list[1]] + "-"
        
        # add the day
            # we have single digit case where we need to add a 9 right before just like the month
        day_digit = [i for i in date_list[0] if not i.isalpha()]
        day_digit = "".join(day_digit)
        
        if len(day_digit) == 1:
            date_string = date_string + "0" + day_digit
        else:
            date_string = date_string + day_digit
        
        return date_string
