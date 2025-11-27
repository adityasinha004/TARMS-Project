import matplotlib.pyplot as plt
import random
import os
from datetime import datetime, timedelta

def generate_prediction_graph():
    # Use current date as seed to keep predictions static for the day
    # This ensures the same predictions are shown throughout the day
    # but will change when the date changes
    today = datetime.now().date()
    seed_value = int(today.strftime('%Y%m%d'))  # e.g., 20251128
    random.seed(seed_value)
    
    # Generate next 7 days starting from today
    days = []
    day_labels = []
    for i in range(7):
        future_date = today + timedelta(days=i)
        day_name = future_date.strftime('%a')  # Mon, Tue, etc.
        day_num = future_date.strftime('%d')   # 28, 29, etc.
        days.append(future_date)
        day_labels.append(f'{day_name}\n{day_num}')  # "Mon\n28"
    
    # Simulate "Predicted" usage (0-100%)
    usage = []
    for day in days:
        weekday = day.weekday()  # 0=Monday, 6=Sunday
        # Make Friday (4) and Saturday (5) busier
        if weekday == 4:  # Friday
            usage.append(random.randint(80, 100))
        elif weekday == 5:  # Saturday
            usage.append(random.randint(70, 90))
        else:
            usage.append(random.randint(40, 90))

    plt.figure(figsize=(10, 6))
    bars = plt.bar(day_labels, usage, color='#4F81BD')
    
    # Create a dynamic title with date range
    start_date = days[0].strftime('%b %d')
    end_date = days[-1].strftime('%b %d, %Y')
    plt.title(f'Predicted Auditorium Usage ({start_date} - {end_date})', fontsize=16)
    plt.xlabel('Day of Week', fontsize=12)
    plt.ylabel('Predicted Occupancy (%)', fontsize=12)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}%',
                ha='center', va='bottom')

    # Ensure directory exists
    output_dir = 'public/images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_path = os.path.join(output_dir, 'prediction.png')
    plt.savefig(output_path)
    print(f"Prediction graph saved to {output_path}")

if __name__ == "__main__":
    generate_prediction_graph()
