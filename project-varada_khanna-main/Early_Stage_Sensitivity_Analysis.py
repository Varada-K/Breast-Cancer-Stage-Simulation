import numpy as np
import matplotlib.pyplot as plt

# Define functions to generate random samples within confidence intervals using normal distribution
def generate_samples_normal(mean, ci, num_samples):
    mu = mean
    sigma = (ci[1] - ci[0]) / 3.92  # 95% CI width is approximately 2 * standard deviation
    return np.random.normal(mu, sigma, num_samples)

# Define parameters for MONO therapy
mono_mean_survival_time = 6.37
mono_survival_time_ci = (6.31, 6.43)
mono_discounted_cost = 17915
mono_cost_ci = (17608, 18221)
mono_discounted_utility = 4.48
mono_utility_ci = (4.43, 4.52)

# Define parameters for COMBO therapy
combo_mean_survival_time = 9.20
combo_survival_time_ci = (9.05, 9.35)
combo_discounted_cost = 193050
combo_cost_ci = (190894, 195206)
combo_discounted_utility = 9.83
combo_utility_ci = (9.76, 9.91)

# Number of samples for uncertainty analysis
num_samples = 1000

# Generate samples for MONO therapy parameters
mono_survival_time_samples = generate_samples_normal(mono_mean_survival_time, mono_survival_time_ci, num_samples)
mono_cost_samples = generate_samples_normal(mono_discounted_cost, mono_cost_ci, num_samples)
mono_utility_samples = generate_samples_normal(mono_discounted_utility, mono_utility_ci, num_samples)

# Generate samples for COMBO therapy parameters
combo_survival_time_samples = generate_samples_normal(combo_mean_survival_time, combo_survival_time_ci, num_samples)
combo_cost_samples = generate_samples_normal(combo_discounted_cost, combo_cost_ci, num_samples)
combo_utility_samples = generate_samples_normal(combo_discounted_utility, combo_utility_ci, num_samples)

# Plot histograms for MONO therapy parameters
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(mono_survival_time_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('MONO Mean Survival Time Distribution')
plt.xlabel('Mean Survival Time (years)')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(mono_cost_samples, bins=30, color='salmon', edgecolor='black')
plt.title('MONO Discounted Cost Distribution')
plt.xlabel('Discounted Cost ($)')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(mono_utility_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('MONO Discounted Utility Distribution')
plt.xlabel('Discounted Utility')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Plot histograms for COMBO therapy parameters
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(combo_survival_time_samples, bins=30, color='skyblue', edgecolor='black')
plt.title('COMBO Mean Survival Time Distribution')
plt.xlabel('Mean Survival Time (years)')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(combo_cost_samples, bins=30, color='salmon', edgecolor='black')
plt.title('COMBO Discounted Cost Distribution')
plt.xlabel('Discounted Cost ($)')
plt.ylabel('Frequency')

plt.subplot(1, 3, 3)
plt.hist(combo_utility_samples, bins=30, color='lightgreen', edgecolor='black')
plt.title('COMBO Discounted Utility Distribution')
plt.xlabel('Discounted Utility')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
