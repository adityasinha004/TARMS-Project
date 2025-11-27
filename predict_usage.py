import matplotlib.pyplot as plt
import random
import os

def generate_prediction_graph():
    # Mock data for prediction
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Simulate "Predicted" usage (0-100%)
    usage = [random.randint(40, 90) for _ in days]
    
    # Make Friday/Saturday busier to look realistic
    usage[4] = random.randint(80, 100) # Fri
    usage[5] = random.randint(70, 90)  # Sat

    plt.figure(figsize=(10, 6))
    bars = plt.bar(days, usage, color='#4F81BD')
    
    plt.title('Predicted Auditorium Usage for Next Week', fontsize=16)
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
