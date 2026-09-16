"""
Add example input/output and expected output to all solve.py files.

This script adds an EXAMPLE section showing what the function should look like
and what output format is expected.
"""

import os
import glob
import re

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

def get_problem_info(content):
    """Extract problem description from the file."""
    match = re.search(r'PROBLEM:\n(.+?)\n\nWrite a function', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def generate_example(desc, level, num):
    """Generate a generic example based on the problem description."""
    # Try to infer the function signature from the description
    desc_lower = desc.lower()

    # Common function patterns
    if "fill" in desc_lower and "missing" in desc_lower:
        func_name = "fill_missing_values"
        example_in = "df = pd.DataFrame({'age': [25, None, 30], 'city': ['Mumbai', 'Delhi', None]})"
        example_out = "DataFrame with NaN filled (age→median, city→most_frequent)"
    elif "one-hot" in desc_lower or "encode" in desc_lower:
        func_name = "encode_categories"
        example_in = "df = pd.DataFrame({'color': ['red', 'blue', 'red']})"
        example_out = "DataFrame with one-hot encoded columns"
    elif "standardize" in desc_lower or "scale" in desc_lower:
        func_name = "scale_features"
        example_in = "X = np.array([[1, 100], [2, 200], [3, 300]])"
        example_out = "Scaled array with mean≈0, std≈1"
    elif "linear regression" in desc_lower:
        func_name = "linear_regression"
        example_in = "x=[1,2,3,4,5], y=[2,4,5,4,5]"
        example_out = "slope=0.6, intercept=2.2"
    elif "mse" in desc_lower or "mean squared" in desc_lower:
        func_name = "mse"
        example_in = "y_true=[1,2,3], y_pred=[1,2,4]"
        example_out = "MSE = 0.333"
    elif "cross-validation" in desc_lower or "cross_val" in desc_lower:
        func_name = "cross_validate"
        example_in = "X, y = load_iris(return_X_y=True)"
        example_out = "mean_accuracy=0.95, std=0.03"
    elif "gridsearch" in desc_lower or "grid search" in desc_lower:
        func_name = "grid_search"
        example_in = "param_grid={'max_depth': [1,3,5,10,20]}"
        example_out = "best_depth=5, best_score=0.93"
    elif "sigmoid" in desc_lower:
        func_name = "sigmoid"
        example_in = "z = 0"
        example_out = "0.5"
    elif "decision tree" in desc_lower:
        func_name = "train_tree"
        example_in = "X, y = load_iris(return_X_y=True)"
        example_out = "accuracy=0.95, tree plotted"
    elif "random forest" in desc_lower:
        func_name = "train_forest"
        example_in = "X, y = make_classification(n_samples=100)"
        example_out = "accuracy=0.92, feature_importances printed"
    elif "accuracy" in desc_lower and "precision" in desc_lower:
        func_name = "compute_metrics"
        example_in = "y_true=[0,0,1,1,1], y_pred=[0,1,1,1,0]"
        example_out = "accuracy=0.6, precision=0.67, recall=0.67, f1=0.67"
    elif "confusion" in desc_lower:
        func_name = "confusion_matrix"
        example_in = "y_true=[0,0,1,1,1], y_pred=[0,1,1,1,0]"
        example_out = "TP=2, FP=1, TN=1, FN=1"
    elif "kmeans" in desc_lower or "cluster" in desc_lower:
        func_name = "cluster"
        example_in = "X = np.random.rand(100, 3)"
        example_out = "cluster_labels=[0,1,2,...], centers=[[...], [...]]"
    elif "svm" in desc_lower or "support vector" in desc_lower:
        func_name = "train_svm"
        example_in = "X, y = make_classification(n_samples=100)"
        example_out = "accuracy=0.95"
    elif "knn" in desc_lower or "k-nearest" in desc_lower:
        func_name = "train_knn"
        example_in = "X, y = load_iris(return_X_y=True)"
        example_out = "accuracy=0.96"
    elif "neural network" in desc_lower or "nn" in desc_lower:
        func_name = "train_nn"
        example_in = "X, y = make_classification(n_samples=100)"
        example_out = "loss decreases over epochs"
    elif "gradient boosting" in desc_lower or "xgboost" in desc_lower:
        func_name = "train_gb"
        example_in = "X, y = make_regression(n_samples=100)"
        example_out = "rmse=0.5"
    elif "feature importance" in desc_lower:
        func_name = "feature_importance"
        example_in = "X, y = make_classification(n_samples=100)"
        example_out = "top features printed"
    elif "pipeline" in desc_lower:
        func_name = "build_pipeline"
        example_in = "X, y = make_classification(n_samples=100)"
        example_out = "accuracy=0.95"
    elif "imbalanced" in desc_lower or "smote" in desc_lower:
        func_name = "handle_imbalance"
        example_in = "X, y = make_classification(n_samples=1000, weights=[0.95])"
        example_out = "recall improves after balancing"
    elif "deploy" in desc_lower or "api" in desc_lower or "flask" in desc_lower or "fastapi" in desc_lower:
        func_name = "create_api"
        example_in = "model trained and saved"
        example_out = "POST /predict returns prediction"
    elif "prompt" in desc_lower or "llm" in desc_lower:
        func_name = "test_prompt"
        example_in = "prompt = 'Summarize this text'"
        example_out = "response compared across strategies"
    else:
        # Generic example
        func_name = "solve"
        example_in = "# input data"
        example_out = "# expected output"

    return func_name, example_in, example_out

def update_solve_file(filepath, level, num):
    """Add example and expected output to a solve.py file."""
    with open(filepath) as f:
        content = f.read()

    # Skip if already has EXAMPLE section
    if "EXAMPLE:" in content:
        return False

    desc = get_problem_info(content)
    if not desc:
        return False

    func_name, example_in, example_out = generate_example(desc, level, num)

    example_section = f'''
EXAMPLE:
  {example_in}
  → {example_out}
'''

    # Insert after PROBLEM section — replace the existing "Write a function" line
    new_content = content.replace(
        f'PROBLEM:\n  {desc}\n\nWrite a function `solve()` that implements the solution.',
        f'PROBLEM:\n  {desc}\n{example_section}\nWrite a function `{func_name}()` that implements the solution.'
    )

    with open(filepath, "w") as f:
        f.write(new_content)
    return True

def main():
    lessons = sorted(glob.glob(os.path.join(AIML_DIR, "lesson-*")))
    updated = 0
    skipped = 0

    for lesson_path in lessons:
        lesson_name = os.path.basename(lesson_path)
        print(f"\n{lesson_name}")
        for level in ["easy", "medium", "hard"]:
            for i in range(1, 4):
                filepath = os.path.join(lesson_path, level, f"p{i:02d}-solve.py")
                if os.path.exists(filepath):
                    if update_solve_file(filepath, level, i):
                        updated += 1
                        print(f"  {level}/p{i:02d}-solve.py")
                    else:
                        skipped += 1

    print(f"\nUpdated {updated} files, skipped {skipped}")

if __name__ == "__main__":
    main()
