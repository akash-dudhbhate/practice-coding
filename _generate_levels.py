"""
Generate all AI/ML levels (02-13) with problems, solutions, and auto-check.
"""

import os

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

LEVELS = {
    "level-02-python-ml": {
        "title": "Python for ML",
        "concepts": [
            "NumPy arrays and operations",
            "Pandas DataFrames",
            "Data loading and inspection",
            "Missing value handling",
            "Feature scaling",
            "Train/test splitting",
        ],
        "easy": [
            ("create-array", "Create a 4x5 NumPy array of random integers (0-100) with a fixed seed. Print its shape, dtype, ndim, size, and column means."),
            ("load-csv", "Load a CSV file into a pandas DataFrame. Print the first 5 rows, shape, and column dtypes."),
            ("fill-missing", "Given a DataFrame with NaN values, fill numeric columns with median and categorical with mode."),
        ],
        "medium": [
            ("preprocess-pipeline", "Build a preprocessing pipeline: impute missing values, scale features, train a logistic regression. Return accuracy."),
            ("detect-outliers", "Detect outliers using IQR method. Cap them and return the cleaned array with outlier count."),
            ("mixed-types", "Handle a DataFrame with numeric, categorical, and datetime columns. Convert, encode, and scale."),
        ],
        "hard": [
            ("data-leakage", "Prevent data leakage: split FIRST, then fit preprocessing on train only. Train a model and return both accuracies."),
            ("column-transformer", "Use ColumnTransformer to apply different preprocessing to numeric vs categorical columns."),
            ("stratified-split", "Create imbalanced data (95/5), split with and without stratify, compare class distributions."),
        ],
        "project": "Clean a real messy dataset — handle missing values, encode categories, scale features, train a model, evaluate.",
    },
    "level-03-visualization": {
        "title": "Data Visualization",
        "concepts": [
            "Matplotlib basics",
            "Seaborn for statistical plots",
            "Line, bar, scatter, histogram",
            "Heatmaps and correlation",
            "Subplots and figure sizing",
            "Saving figures",
        ],
        "easy": [
            ("line-plot", "Plot y = sin(x) and y = cos(x) on the same figure with labels, legend, title, and grid."),
            ("scatter-plot", "Create a scatter plot of height vs weight. Color by gender. Add labels and title."),
            ("histogram", "Plot a histogram of exam scores. Add mean and median lines. Label everything."),
        ],
        "medium": [
            ("correlation-heatmap", "Create a correlation heatmap of a dataset. Use seaborn. Annotate values."),
            ("subplots", "Create a 2x2 subplot figure with: line plot, scatter, histogram, and bar chart."),
            ("box-plot", "Create a box plot comparing distributions across categories. Add swarm plot overlay."),
        ],
        "hard": [
            ("custom-dashboard", "Build a 4-panel dashboard: revenue over time, by product, by region, and correlation matrix."),
            ("animated-plot", "Create an animated plot showing data changing over time (use matplotlib.animation)."),
            ("publication-figure", "Create a publication-quality figure with custom fonts, colors, and export at 300 DPI."),
        ],
        "project": "Build a complete data dashboard for a sales dataset with 6 different visualizations.",
    },
    "level-04-supervised": {
        "title": "Supervised Learning",
        "concepts": [
            "Linear regression from scratch",
            "Logistic regression",
            "Decision trees",
            "Random forests",
            "SVM and KNN",
            "Feature importance",
        ],
        "easy": [
            ("linear-scratch", "Implement linear regression from scratch using numpy. Calculate slope and intercept."),
            ("logistic-scratch", "Implement sigmoid function and logistic regression from scratch."),
            ("decision-tree", "Train a decision tree on Iris dataset. Print accuracy and visualize the tree."),
        ],
        "medium": [
            ("gradient-descent", "Implement gradient descent for linear regression. Track MSE over iterations."),
            ("random-forest", "Train a random forest on a synthetic dataset. Show feature importances."),
            ("svm-knn", "Compare SVM and KNN on a classification dataset. Print accuracy for both."),
        ],
        "hard": [
            ("regularization", "Implement L1 and L2 regularization from scratch. Show effect on coefficients."),
            ("ensemble-compare", "Compare decision tree, random forest, and gradient boosting on same dataset."),
            ("feature-selection", "Implement recursive feature elimination. Show which features matter most."),
        ],
        "project": "Build a house price predictor using linear regression from scratch, compare with sklearn.",
    },
    "level-05-evaluation": {
        "title": "Model Evaluation & Tuning",
        "concepts": [
            "Accuracy, precision, recall, F1",
            "Confusion matrix",
            "ROC and AUC",
            "Cross-validation",
            "Hyperparameter tuning",
            "Learning curves",
        ],
        "easy": [
            ("metrics-scratch", "Implement accuracy, precision, recall, and F1 from scratch. Test with sample data."),
            ("confusion-matrix", "Build a confusion matrix from predictions. Print TP, FP, TN, FN."),
            ("kfold-cv", "Run 5-fold cross-validation on a model. Print mean and std of accuracy."),
        ],
        "medium": [
            ("roc-auc", "Plot ROC curve and calculate AUC for a classifier."),
            ("grid-search", "Use GridSearchCV to tune hyperparameters. Print best params and score."),
            ("learning-curve", "Plot learning curve showing train vs validation error over training size."),
        ],
        "hard": [
            ("precision-recall-tradeoff", "Find the threshold that gives 80% recall. Report precision at that threshold."),
            ("model-comparison", "Compare 5 models with 3 metrics each. Print a comparison table."),
            ("nested-cv", "Implement nested cross-validation for unbiased model evaluation."),
        ],
        "project": "Build a model evaluation dashboard comparing multiple classifiers with all metrics.",
    },
    "level-06-advanced-ml": {
        "title": "Advanced ML",
        "concepts": [
            "Feature engineering",
            "Handling imbalanced data",
            "SMOTE and resampling",
            "Feature selection",
            "Dimensionality reduction",
            "Pipeline building",
        ],
        "easy": [
            ("feature-polynomial", "Create polynomial features from numeric data. Show effect on model."),
            ("label-encode", "Encode categorical features using label encoding and one-hot encoding."),
            ("feature-scale", "Compare standardization vs normalization. Show effect on model."),
        ],
        "medium": [
            ("smote-imbalance", "Handle imbalanced data with SMOTE. Compare before/after metrics."),
            ("feature-importance", "Use feature importance to select top features. Compare model performance."),
            ("pca-reduce", "Apply PCA to reduce dimensions. Show explained variance ratio."),
        ],
        "hard": [
            ("custom-transformer", "Build a custom sklearn transformer for a specific preprocessing step."),
            ("feature-engineering-pipeline", "Build a complete feature engineering pipeline with multiple steps."),
            ("imbalanced-ensemble", "Use ensemble methods designed for imbalanced data (BalancedRandomForest)."),
        ],
        "project": "Build a fraud detection system handling extreme class imbalance.",
    },
    "level-07-unsupervised": {
        "title": "Unsupervised Learning",
        "concepts": [
            "K-Means clustering",
            "Hierarchical clustering",
            "DBSCAN",
            "Dimensionality reduction",
            "Anomaly detection",
            "Association rules",
        ],
        "easy": [
            ("kmeans-basic", "Apply K-Means to a dataset. Print cluster centers and labels."),
            ("elbow-method", "Use the elbow method to find optimal K. Plot inertias."),
            ("pca-basic", "Apply PCA to reduce 4D data to 2D. Plot the result."),
        ],
        "medium": [
            ("silhouette-score", "Use silhouette score to evaluate clustering quality."),
            ("dbscan-vs-kmeans", "Compare K-Means and DBSCAN on non-spherical data."),
            ("hierarchical", "Apply hierarchical clustering. Plot dendrogram."),
        ],
        "hard": [
            ("customer-segmentation", "Build a customer segmentation pipeline with profiling."),
            ("anomaly-detection", "Detect anomalies using isolation forest or LOF."),
            ("topic-modeling", "Apply LDA to discover topics in text data."),
        ],
        "project": "Build a customer segmentation engine with cluster profiling and visualization.",
    },
    "level-08-neural-networks": {
        "title": "Neural Networks & PyTorch",
        "concepts": [
            "Perceptron and activation functions",
            "Forward and backward propagation",
            "Loss functions and optimizers",
            "PyTorch tensors and autograd",
            "Building nn.Module",
            "Training loops",
        ],
        "easy": [
            ("perceptron", "Implement a single perceptron from scratch. Train on OR gate."),
            ("activation-functions", "Implement sigmoid, ReLU, and tanh from scratch. Plot them."),
            ("pytorch-tensor", "Create PyTorch tensors, do basic operations, compute gradients."),
        ],
        "medium": [
            ("mlp-scratch", "Build a 2-layer neural network from scratch. Train on XOR."),
            ("pytorch-nn", "Build a neural network with nn.Module. Train on synthetic data."),
            ("training-loop", "Write a complete PyTorch training loop with loss tracking."),
        ],
        "hard": [
            ("backprop-scratch", "Implement backpropagation from scratch for a 2-layer network."),
            ("custom-loss", "Implement a custom loss function in PyTorch."),
            ("transfer-learning", "Use a pretrained model (ResNet) for a new classification task."),
        ],
        "project": "Build a MNIST digit recognizer with PyTorch from scratch.",
    },
    "level-09-deep-learning": {
        "title": "Deep Learning",
        "concepts": [
            "CNN architecture",
            "Convolution and pooling",
            "Batch normalization",
            "Dropout and regularization",
            "Transfer learning",
            "Data augmentation",
        ],
        "easy": [
            ("conv-basic", "Implement a simple convolution operation from scratch."),
            ("cnn-basic", "Build a basic CNN for MNIST using PyTorch or Keras."),
            ("pooling", "Implement max pooling and average pooling from scratch."),
        ],
        "medium": [
            ("cifar10", "Build a CNN for CIFAR-10. Train and evaluate."),
            ("batchnorm", "Add batch normalization to a network. Compare training."),
            ("dropout", "Add dropout to prevent overfitting. Compare with/without."),
        ],
        "hard": [
            ("resnet", "Use a pretrained ResNet for transfer learning on a custom dataset."),
            ("data-augmentation", "Implement data augmentation pipeline (rotation, flip, crop)."),
            ("custom-cnn", "Design and train a custom CNN architecture for a specific task."),
        ],
        "project": "Build an image classifier for a custom dataset using CNN.",
    },
    "level-10-deployment": {
        "title": "Model Deployment",
        "concepts": [
            "Saving and loading models",
            "FastAPI/Flask APIs",
            "Model versioning",
            "Docker basics",
            "Monitoring and logging",
            "A/B testing",
        ],
        "easy": [
            ("save-model", "Train a model, save it with joblib/pickle, load and predict."),
            ("simple-api", "Create a Flask API that takes features and returns prediction."),
            ("model-info", "Create an API endpoint that returns model metadata."),
        ],
        "medium": [
            ("fastapi-predict", "Build a FastAPI endpoint with input validation and prediction."),
            ("batch-predict", "Create a batch prediction endpoint that processes multiple inputs."),
            ("model-versioning", "Implement model versioning — load different versions."),
        ],
        "hard": [
            ("docker-ml", "Create a Dockerfile for an ML API."),
            ("monitoring", "Add logging and monitoring to an ML API."),
            ("a-b-testing", "Implement A/B testing logic for model comparison."),
        ],
        "project": "Build a complete ML API with FastAPI, Docker, and monitoring.",
    },
    "level-11-llm-prompt": {
        "title": "LLM & Prompt Engineering",
        "concepts": [
            "What are LLMs",
            "Prompt design patterns",
            "Few-shot learning",
            "Chain-of-thought",
            "Temperature and sampling",
            "Evaluation of LLM outputs",
        ],
        "easy": [
            ("basic-prompts", "Write 3 prompts for the same task. Compare outputs."),
            ("few-shot", "Create a few-shot prompt for classification. Test with examples."),
            ("temperature", "Compare outputs at different temperature settings."),
        ],
        "medium": [
            ("chain-of-thought", "Write a chain-of-thought prompt for math problems."),
            ("prompt-templates", "Create reusable prompt templates with variables."),
            ("output-parsing", "Parse structured output from LLM responses."),
        ],
        "hard": [
            ("prompt-optimization", "Optimize a prompt for a specific task through iteration."),
            ("llm-evaluation", "Build a framework to evaluate LLM outputs systematically."),
            ("system-prompts", "Design system prompts for different personas/tasks."),
        ],
        "project": "Build a prompt engineering playground with testing framework.",
    },
    "level-12-rag": {
        "title": "RAG Systems",
        "concepts": [
            "What is RAG",
            "Embeddings and vector databases",
            "Retrieval strategies",
            "Chunking documents",
            "Reranking",
            "Evaluation of RAG",
        ],
        "easy": [
            ("embeddings-basic", "Generate embeddings for text. Compute similarity."),
            ("simple-rag", "Build a simple RAG: embed documents, retrieve, generate."),
            ("chunking", "Implement document chunking strategies."),
        ],
        "medium": [
            ("vector-db", "Store and query embeddings in a vector database."),
            ("reranking", "Implement reranking of retrieved documents."),
            ("hybrid-search", "Combine keyword and semantic search."),
        ],
        "hard": [
            ("rag-pipeline", "Build a complete RAG pipeline with retrieval and generation."),
            ("rag-evaluation", "Evaluate RAG quality with metrics."),
            ("advanced-rag", "Implement advanced RAG with query rewriting and multi-hop."),
        ],
        "project": "Build a document Q&A system using RAG.",
    },
    "level-13-agentic-ai": {
        "title": "Agentic AI",
        "concepts": [
            "What are AI agents",
            "Tool use and function calling",
            "Agent loops and planning",
            "Multi-agent systems",
            "Memory and context",
            "Agent evaluation",
        ],
        "easy": [
            ("simple-agent", "Build a simple agent that can use a calculator tool."),
            ("tool-use", "Implement function calling for an LLM."),
            ("agent-loop", "Create a basic agent loop: think, act, observe."),
        ],
        "medium": [
            ("multi-tool", "Build an agent that can use multiple tools."),
            ("planning-agent", "Implement a planning agent that breaks down tasks."),
            ("memory-agent", "Add memory to an agent so it remembers context."),
        ],
        "hard": [
            ("multi-agent", "Build a multi-agent system where agents collaborate."),
            ("agent-evaluation", "Build a framework to evaluate agent performance."),
            ("autonomous-agent", "Build an autonomous agent that completes a multi-step task."),
        ],
        "project": "Build an AI agent that can research a topic and write a report.",
    },
}


def create_level(level_name, config):
    """Create a complete level directory with all files."""
    level_path = os.path.join(AIML_DIR, level_name)
    os.makedirs(level_path, exist_ok=True)

    title = config["title"]
    concepts = config["concepts"]

    # Create README.md
    readme = f"""# {level_name.replace('-', ' ').title()} — {title}

## What You'll Learn
{chr(10).join(f'- {c}' for c in concepts)}

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
{chr(10).join(f'{i+1}. `easy/p{i+1:02d}-{name}.py` — {desc[:60]}...' for i, (name, desc) in enumerate(config["easy"]))}

### Medium
{chr(10).join(f'{i+4}. `medium/p{i+1:02d}-{name}.py` — {desc[:60]}...' for i, (name, desc) in enumerate(config["medium"]))}

### Hard
{chr(10).join(f'{i+7}. `hard/p{i+1:02d}-{name}.py` — {desc[:60]}...' for i, (name, desc) in enumerate(config["hard"]))}

### Project
`project/` — {config["project"]}

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-{config["easy"][0][0]}.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
"""
    with open(os.path.join(level_path, "README.md"), "w") as f:
        f.write(readme)

    # Create concepts.md
    concepts_md = f"""# {level_name.replace('-', ' ').title()} — Concepts Reference

## Key Concepts

{chr(10).join(f'### {c}{chr(10)}- Brief explanation of {c.lower()}.{chr(10)}' for c in concepts)}
"""
    with open(os.path.join(level_path, "concepts.md"), "w") as f:
        f.write(concepts_md)

    # Create check.py template
    check_template = f'''"""
Auto-Check System — {title}
=============================
Run this to verify your solutions automatically.

Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# TODO: Add check functions for each problem
# def check_p01(module):
#     if not hasattr(module, 'solve'):
#         return False, "Function 'solve' not found"
#     result = module.solve(...)
#     if result != expected:
#         return False, f"Expected X, got Y"
#     return True, "All tests passed!"


CHECKS = {{
    # Add checks here
}}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))

    if target == "all":
        print("=" * 60)
        print(f"  {title.upper()} — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            num_clean = num.lstrip("p")
            filepath = os.path.join(level_dir, level, f"p{{num_clean}}-solve.py")
            if not os.path.exists(filepath):
                pattern = os.path.join(level_dir, level, f"p{{num_clean}}-*.py")
                matches = [f for f in glob.glob(pattern) if "solutions" not in f]
                if matches:
                    filepath = matches[0]
            if not os.path.exists(filepath):
                print(f"  {{check_id}}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {{check_id}}: {{status}} — {{msg}}")
            except Exception as e:
                print(f"  {{check_id}}: ERROR — {{e}}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{{level}}/{{num}}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{{check_id}}'")
        sys.exit(1)

    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{{num_clean}}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{{num_clean}}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    if not os.path.exists(filepath):
        print(f"Error: file not found: {{filepath}}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"✓ PASS — {{msg}}")
            print(f"  Add '# DONE' to the first line of {{filepath}}")
        else:
            print(f"✗ FAIL — {{msg}}")
    except Exception as e:
        print(f"✗ ERROR — {{e}}")


if __name__ == "__main__":
    main()
'''
    with open(os.path.join(level_path, "check.py"), "w") as f:
        f.write(check_template)

    # Create problem files
    for difficulty in ["easy", "medium", "hard"]:
        diff_dir = os.path.join(level_path, difficulty)
        os.makedirs(diff_dir, exist_ok=True)
        os.makedirs(os.path.join(diff_dir, "solutions"), exist_ok=True)

        problems = config[difficulty]
        for i, (name, desc) in enumerate(problems, 1):
            # Problem file
            problem_content = f'''"""
{level_name.replace('-', ' ').upper()}
{difficulty.upper()} P{i:02d} — {name.replace('-', ' ').title()}
{'=' * 50}

CONCEPT:
  See concepts.md in this level folder for detailed explanations.

PROBLEM:
  {desc}

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  # Your test data here
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 {difficulty}/solutions/p{i:02d}-solution.py

  Then compare your output format with theirs.

Write a function `solve()` that implements the solution.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test your solution:
# result = solve(...)
# print(result)
'''
            with open(os.path.join(diff_dir, f"p{i:02d}-{name}.py"), "w") as f:
                f.write(problem_content)

            # Solution file
            solution_content = f'''"""
{level_name.replace('-', ' ').upper()}
{difficulty.upper()} P{i:02d} — {name.replace('-', ' ').title()} (Solution)
{'=' * 50}
"""

def solve():
    """Solution for: {desc[:60]}..."""
    # TODO: Implement solution
    pass


if __name__ == "__main__":
    result = solve()
    print(result)
'''
            with open(os.path.join(diff_dir, "solutions", f"p{i:02d}-solution.py"), "w") as f:
                f.write(solution_content)

    # Create project file
    project_dir = os.path.join(level_path, "project")
    os.makedirs(project_dir, exist_ok=True)
    project_content = f'''"""
{level_name.replace('-', ' ').upper()} PROJECT — {title}
{'=' * 50}

{config["project"]}

This is a design + implementation exercise. Apply everything
you learned in this level to build a real system.

INSTRUCTIONS:
  1. Read the project description above
  2. Plan your approach (write comments first)
  3. Implement step by step
  4. Test each component
  5. Document your design decisions

EXPECTED OUTPUT:
  A working system that demonstrates the concepts from this level.
  Write code, comments, and documentation.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Build the project step by step.
'''
    with open(os.path.join(project_dir, f"{config['project'].split()[0].lower()}-project.py"), "w") as f:
        f.write(project_content)

    print(f"Created {level_name}")


def main():
    for level_name, config in LEVELS.items():
        create_level(level_name, config)
    print(f"\nCreated {len(LEVELS)} levels")


if __name__ == "__main__":
    main()
