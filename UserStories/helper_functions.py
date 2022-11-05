from datetime import datetime
from dateutil.relativedelta import relativedelta

def difference_in_dates(start_date: datetime.date, end_date: datetime.date, unit: str) -> int:
    
    if unit == 'days':
        no_of_days = (end_date - start_date).days
        return no_of_days
    
    elif unit == 'months' or unit == 'years':
        difference_in_dates = relativedelta(end_date, start_date)
    
        if unit == "months":
            no_of_months = (difference_in_dates.years * 12) + difference_in_dates.months
            return no_of_months
        
        elif unit == "years":
            no_of_years = difference_in_dates.years
            return no_of_years
        
    else:
        print(f"Error in function date_subtract: No unit type {unit}")