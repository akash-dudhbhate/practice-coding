"""
Generate real working solutions for all AI/ML levels.
Each solution is a complete, runnable implementation.
"""

import os
import glob

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

# All solutions organized by level
SOLUTIONS = {
    "level-03-visualization": {
        "easy": [
            """import numpy as np
import matplotlib.pyplot as plt

def solve():
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), label='sin(x)', linewidth=2)
    plt.plot(x, np.cos(x), label='cos(x)', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine and Cosine Waves')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('trig_plot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to trig_plot.png")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    height = np.random.normal(170, 10, 100)
    weight = height * 0.6 + np.random.normal(0, 5, 100)
    gender = np.random.choice(['M', 'F'], 100)
    colors = {'M': 'blue', 'F': 'red'}
    plt.figure(figsize=(10, 6))
    for g in ['M', 'F']:
        mask = gender == g
        plt.scatter(height[mask], weight[mask], c=colors[g], label=g, alpha=0.6)
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.title('Height vs Weight by Gender')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter_plot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to scatter_plot.png")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    scores = np.random.normal(75, 15, 200)
    scores = np.clip(scores, 0, 100)
    plt.figure(figsize=(10, 6))
    plt.hist(scores, bins=20, edgecolor='black', alpha=0.7, color='skyblue')
    plt.axvline(np.mean(scores), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(scores):.1f}')
    plt.axvline(np.median(scores), color='green', linestyle='--', linewidth=2, label=f'Median: {np.median(scores):.1f}')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Distribution of Exam Scores')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('histogram.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to histogram.png")

if __name__ == "__main__":
    solve()""",
        ],
        "medium": [
            """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'feature_a': np.random.randn(100),
        'feature_b': np.random.randn(100),
        'feature_c': np.random.randn(100),
        'feature_d': np.random.randn(100),
        'target': np.random.randn(100)
    })
    corr = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f',
                square=True, linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to correlation_heatmap.png")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Data Dashboard', fontsize=16)
    # Line plot
    x = np.linspace(0, 10, 100)
    axes[0, 0].plot(x, np.sin(x), 'r-')
    axes[0, 0].set_title('Line Plot')
    axes[0, 0].grid(True, alpha=0.3)
    # Scatter plot
    axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
    axes[0, 1].set_title('Scatter Plot')
    axes[0, 1].grid(True, alpha=0.3)
    # Histogram
    axes[1, 0].hist(np.random.randn(200), bins=20, edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('Histogram')
    axes[1, 0].grid(True, alpha=0.3)
    # Bar chart
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 56, 78]
    axes[1, 1].bar(categories, values, color=['red', 'blue', 'green', 'orange'])
    axes[1, 1].set_title('Bar Chart')
    axes[1, 1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to dashboard.png")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'category': np.repeat(['A', 'B', 'C', 'D'], 50),
        'value': np.concatenate([
            np.random.normal(50, 10, 50),
            np.random.normal(60, 15, 50),
            np.random.normal(55, 12, 50),
            np.random.normal(70, 8, 50)
        ])
    })
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='category', y='value', data=data, palette='Set2')
    sns.swarmplot(x='category', y='value', data=data, color='black', alpha=0.5, size=3)
    plt.title('Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.3)
    plt.savefig('boxplot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to boxplot.png")

if __name__ == "__main__":
    solve()""",
        ],
        "hard": [
            """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=90)
    data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.normal(10000, 2000, 90),
        'product': np.random.choice(['A', 'B', 'C'], 90),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 90)
    })
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sales Dashboard', fontsize=16)
    # Revenue over time
    data.groupby('date')['revenue'].sum().plot(ax=axes[0, 0], title='Revenue Over Time')
    # Revenue by product
    data.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0, 1], title='Revenue by Product')
    # Revenue by region
    data.groupby('region')['revenue'].sum().plot(kind='pie', ax=axes[1, 0], title='Revenue by Region', autopct='%1.1f%%')
    # Correlation
    numeric_data = data.groupby(['product', 'region'])['revenue'].sum().unstack()
    sns.heatmap(numeric_data, annot=True, ax=axes[1, 1], cmap='YlOrRd')
    axes[1, 1].set_title('Product × Region Revenue')
    plt.tight_layout()
    plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to sales_dashboard.png")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def solve():
    np.random.seed(42)
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 2 * np.pi, 100)
    line, = ax.plot(x, np.sin(x))
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Animated Sine Wave')
    ax.grid(True, alpha=0.3)
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,
    anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.show()
    print("Animation displayed")

if __name__ == "__main__":
    solve()""",
            """import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def solve():
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['font.size'] = 12
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
    ax.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
    ax.fill_between(x, np.sin(x), np.cos(x), alpha=0.2, color='purple')
    ax.set_xlabel('X Axis Label', fontsize=14)
    ax.set_ylabel('Y Axis Label', fontsize=14)
    ax.set_title('Publication Quality Figure', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('publication_figure.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Plot saved to publication_figure.png at 300 DPI")

if __name__ == "__main__":
    solve()""",
        ],
    },
    "level-04-supervised": {
        "easy": [
            """import numpy as np

def solve():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 5, 4, 5])
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    m = numerator / denominator
    b = y_mean - m * x_mean
    y_pred = m * x + b
    r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y_mean) ** 2)
    print(f"Slope: {m:.4f}")
    print(f"Intercept: {b:.4f}")
    print(f"R²: {r2:.4f}")
    return m, b

if __name__ == "__main__":
    solve()""",
            """import numpy as np

def solve():
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([0, 0, 0, 1, 1])
    weights = np.zeros(X.shape[1])
    bias = 0
    lr = 0.1
    for _ in range(1000):
        z = np.dot(X, weights) + bias
        y_pred = sigmoid(z)
        dw = np.dot(X.T, (y_pred - y)) / len(y)
        db = np.sum(y_pred - y) / len(y)
        weights -= lr * dw
        bias -= lr * db
    predictions = sigmoid(np.dot(X, weights) + bias)
    accuracy = np.mean((predictions > 0.5) == y)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weights: {weights}")
    print(f"Bias: {bias:.4f}")
    return weights, bias

if __name__ == "__main__":
    solve()""",
            """from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    accuracy = tree.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")
    plt.figure(figsize=(14, 8))
    plot_tree(tree, feature_names=iris.feature_names,
              class_names=iris.target_names, filled=True, rounded=True)
    plt.savefig('decision_tree.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Tree saved to decision_tree.png")
    return accuracy

if __name__ == "__main__":
    solve()""",
        ],
        "medium": [
            """import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    X = np.random.randn(100, 1)
    y = 3 * X.flatten() + 2 + np.random.randn(100) * 0.5
    m, b = 0.0, 0.0
    lr = 0.01
    losses = []
    for i in range(1000):
        y_pred = m * X.flatten() + b
        mse = np.mean((y - y_pred) ** 2)
        losses.append(mse)
        dm = -2 * np.mean(X.flatten() * (y - y_pred))
        db = -2 * np.mean(y - y_pred)
        m -= lr * dm
        b -= lr * db
    print(f"Final m: {m:.4f}, b: {b:.4f}")
    print(f"Final MSE: {losses[-1]:.4f}")
    plt.plot(losses)
    plt.xlabel('Iteration')
    plt.ylabel('MSE')
    plt.title('Gradient Descent Loss')
    plt.savefig('gradient_descent.png', dpi=150, bbox_inches='tight')
    plt.show()
    return m, b

if __name__ == "__main__":
    solve()""",
            """from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def solve():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    accuracy = rf.score(X_test, y_test)
    importances = rf.feature_importances_
    print(f"Accuracy: {accuracy:.4f}")
    print("Feature importances:")
    for i, imp in enumerate(importances):
        print(f"  Feature {i}: {imp:.4f}")
    return accuracy, importances

if __name__ == "__main__":
    solve()""",
            """from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def solve():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svm = SVC(random_state=42)
    svm.fit(X_train, y_train)
    svm_acc = svm.score(X_test, y_test)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_acc = knn.score(X_test, y_test)
    print(f"SVM Accuracy: {svm_acc:.4f}")
    print(f"KNN Accuracy: {knn_acc:.4f}")
    return svm_acc, knn_acc

if __name__ == "__main__":
    solve()""",
        ],
        "hard": [
            """import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.datasets import make_regression

def solve():
    X, y = make_regression(n_samples=100, n_features=10, noise=10, random_state=42)
    lr = LinearRegression().fit(X, y)
    lasso = Lasso(alpha=1.0).fit(X, y)
    ridge = Ridge(alpha=1.0).fit(X, y)
    print("Coefficients comparison:")
    print(f"{'Feature':<10} {'Linear':<12} {'Lasso':<12} {'Ridge':<12}")
    for i in range(X.shape[1]):
        print(f"{i:<10} {lr.coef_[i]:<12.4f} {lasso.coef_[i]:<12.4f} {ridge.coef_[i]:<12.4f}")
    return lr.coef_, lasso.coef_, ridge.coef_

if __name__ == "__main__":
    solve()""",
            """from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    }
    print(f"{'Model':<20} {'Train Acc':<12} {'Test Acc':<12}")
    print("-" * 44)
    for name, model in models.items():
        model.fit(X_train, y_train)
        train_acc = model.score(X_train, y_train)
        test_acc = model.score(X_test, y_test)
        print(f"{name:<20} {train_acc:<12.4f} {test_acc:<12.4f}")
    return models

if __name__ == "__main__":
    solve()""",
            """from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(random_state=42)
    rfe = RFE(estimator=rf, n_features_to_select=5)
    rfe.fit(X_train, y_train)
    selected = rfe.support_
    X_train_selected = X_train[:, selected]
    X_test_selected = X_test[:, selected]
    rf.fit(X_train_selected, y_train)
    accuracy = rf.score(X_test_selected, y_test)
    print(f"Selected features: {list(np.where(selected)[0])}")
    print(f"Accuracy with selected features: {accuracy:.4f}")
    return selected, accuracy

if __name__ == "__main__":
    solve()""",
        ],
    },
}


def write_solutions(level_name, solutions):
    """Write solution files for a level."""
    level_path = os.path.join(AIML_DIR, level_name)
    for difficulty, sols in solutions.items():
        for i, solution_code in enumerate(sols, 1):
            filepath = os.path.join(level_path, difficulty, "solutions", f"p{i:02d}-solution.py")
            title = level_name.replace('-', ' ').title()
            with open(filepath, "w") as f:
                f.write(f'"""{title} — {difficulty.capitalize()} P{i:02d} Solution"""\n\n')
                f.write(solution_code)
            print(f"Wrote {filepath}")


def main():
    for level_name, solutions in SOLUTIONS.items():
        write_solutions(level_name, solutions)
    print(f"\nDone writing solutions for {len(SOLUTIONS)} levels")


if __name__ == "__main__":
    main()
