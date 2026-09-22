"""Level 03 — Data Visualization — Easy P03 Solution"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_histogram():
    np.random.seed(42)
    scores = np.random.normal(75, 15, 200)
    scores = np.clip(scores, 0, 100)
    plt.figure(figsize=(10, 6))
    plt.hist(scores, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
    plt.axvline(np.mean(scores), color='red', linestyle='--', linewidth=2,
                label=f'Mean: {np.mean(scores):.1f}')
    plt.axvline(np.median(scores), color='green', linestyle='--', linewidth=2,
                label=f'Median: {np.median(scores):.1f}')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Distribution of Exam Scores')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('histogram.png', dpi=150, bbox_inches='tight')
    plt.close()
    return scores

if __name__ == "__main__":
    s = plot_histogram()
    print(len(s))
    print(f"{s.mean():.1f}")
