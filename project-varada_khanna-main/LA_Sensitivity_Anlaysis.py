import numpy as np
import matplotlib.pyplot as plt

# Define functions to generate random samples within confidence intervals using normal distribution
def generate_samples_normal(mean, ci, num_samples):
    mu = mean
    sigma = (ci[1] - ci[0]) / 3.92  # 95% CI width is approximately 2 * standard deviation
    return np.random.normal(mu, sigma, num_samples)

# Parameters for increase in mean survival time
increase_mean_survival_time = 1.74
increase_survival_time_ci = (1.55, 1.93)

# Parameters for increase in mean discounted cost
increase_mean_discounted_cost = 198147.95
increase_cost_ci = (188097.21, 208198.69)

# Parameters for increase in mean discounted utility
increase_mean_discounted_utility = 1.59
increase_utility_ci = (1.45, 1.73)

# Number of samples for uncertainty analysis
num_samples = 1000

# Generate samples for increase in mean survival time
survival_time_increases = generate_samples_normal(increase_mean_survival_time, increase_survival_time_ci, num_samples)

# Generate samples for increase in mean discounted cost
cost_increases = generate_samples_normal(increase_mean_discounted_cost, increase_cost_ci, num_samples)

# Generate samples for increase in mean discounted utility
utility_increases = generate_samples_normal(increase_mean_discounted_utility, increase_utility_ci, num_samples)

# Plot histograms for increase in mean survival time
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.hist(survival_time_increases, bins=30, color='skyblue', edgecolor='black')
plt.title('Increase in Mean Survival Time Distribution')
plt.xlabel('Increase in Mean Survival Time (years)')
plt.ylabel('Frequency')

# Plot histograms for increase in mean discounted cost
plt.subplot(1, 3, 2)
plt.hist(cost_increases, bins=30, color='salmon', edgecolor='black')
plt.title('Increase in Mean Discounted Cost Distribution')
plt.xlabel('Increase in Mean Discounted Cost ($)')
plt.ylabel('Frequency')

# Plot histograms for increase in mean discounted utility
plt.subplot(1, 3, 3)
plt.hist(utility_increases, bins=30, color='lightgreen', edgecolor='black')
plt.title('Increase in Mean Discounted Utility Distribution')
plt.xlabel('Increase in Mean Discounted Utility')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
#####