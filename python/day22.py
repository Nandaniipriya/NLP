'''
Question1: Create a visualization that shows the performance comparison of two machine learning models 
over different training epochs. Create a line plot showing accuracy over time with proper labels, 
legend, and styling. Use this sample data:
model1_accuracy = [0.65, 0.70, 0.75, 0.78, 0.82, 0.85, 0.87, 0.88, 0.89, 0.90]
model2_accuracy = [0.60, 0.68, 0.72, 0.75, 0.78, 0.80, 0.81, 0.82, 0.82, 0.83]
'''
import matplotlib.pyplot as plt
import numpy as np

# Sample data
epochs = np.arange(1, 11)  # 1 to 10 epochs
model1_accuracy = [0.65, 0.70, 0.75, 0.78, 0.82, 0.85, 0.87, 0.88, 0.89, 0.90]
model2_accuracy = [0.60, 0.68, 0.72, 0.75, 0.78, 0.80, 0.81, 0.82, 0.82, 0.83]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(epochs, model1_accuracy, 'b-o', label='Model 1', linewidth=2)
plt.plot(epochs, model2_accuracy, 'r-o', label='Model 2', linewidth=2)

# Customize the plot
plt.title('Model Performance Comparison', fontsize=14, pad=15)
plt.xlabel('Epochs', fontsize=12)
plt.ylabel('Accuracy', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)

# Set y-axis limits to start from 0.5 for better visualization
plt.ylim(0.5, 1.0)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Customize ticks
plt.xticks(epochs)
plt.yticks(np.arange(0.5, 1.05, 0.05))

# Add a light background grid
plt.grid(True, linestyle='--', alpha=0.3)

# Save the plot (optional)
# plt.savefig('model_comparison.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.tight_layout()
plt.show()