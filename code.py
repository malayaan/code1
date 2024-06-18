import pandas as pd
import calendar

# Sample DataFrame
data = {
    'Date': [
        pd.Timestamp('2024-06-05'), pd.Timestamp('2024-06-15'), pd.Timestamp('2024-06-25'),
        pd.Timestamp('2024-07-10'), pd.Timestamp('2024-07-20'),
        pd.Timestamp('2024-08-05'), pd.Timestamp('2024-08-15')
    ],
    'Type': ['A', 'B', 'A', 'C', 'A', 'B', 'C']
}
df = pd.DataFrame(data)

# Dictionary mapping types to ANSI color codes
type_to_color = {
    'A': "\033[91m",  # Red
    'B': "\033[94m",  # Blue
    'C': "\033[92m"   # Green
}
end_color = "\033[0m"  # Reset color

# Define a function to print the calendar with highlighted dates based on type
def print_highlighted_calendar_with_types(year, start_month, end_month, df, type_to_color):
    for month in range(start_month, end_month + 1):
        # Create a calendar
        cal = calendar.TextCalendar(calendar.SUNDAY)
        
        # Generate the calendar for the month
        cal_str = cal.formatmonth(year, month).split('\n')
        
        # Create a dictionary to map dates to types
        date_to_type = {row['Date'].day: row['Type'] for _, row in df.iterrows() if row['Date'].month == month and row['Date'].year == year}
        
        # Modify the calendar string to highlight specific dates based on type
        for i in range(len(cal_str)):
            if i > 1:  # Data starts from line 2 in the formatted calendar string
                line = cal_str[i].split()
                new_line = []
                for day in line:
                    if day.isdigit():
                        day_int = int(day)
                        if day_int in date_to_type:
                            type_color = type_to_color.get(date_to_type[day_int], "")
                            day = f"{type_color}{day}{end_color}"
                    new_line.append(day)
                cal_str[i] = " ".join(new_line)
        
        # Print the modified calendar
        print(f"\nCalendar for {calendar.month_name[month]} {year} with highlighted dates based on type:")
        for line in cal_str:
            print(line)

# Year to display
year = 2024

# Start and end month to display
start_month = 6  # June
end_month = 8    # August

# Print the calendar for multiple months
print_highlighted_calendar_with_types(year, start_month, end_month, df, type_to_color)
