"""
Generate real working solutions for remaining AI/ML levels (05-13).
Each solution is a complete, runnable implementation.
"""

import os

AIML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ai-ml")

# Level 05: Model Evaluation & Tuning
LEVEL_05 = {
    "easy": [
        """def solve():
    y_true = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    accuracy = (tp + tn) / len(y_true)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    print(f"TP={tp}, FP={fp}, TN={tn}, FN={fn}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1: {f1:.2f}")
    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}

if __name__ == "__main__":
    solve()""",
        """def solve():
    y_true = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    print(f"Confusion Matrix:")
    print(f"  TP={tp}  FN={fn}")
    print(f"  FP={fp}  TN={tn}")
    return {"TP": tp, "FP": fp, "TN": tn, "FN": fn}

if __name__ == "__main__":
    solve()""",
        """from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

def solve():
    iris = load_iris()
    X, y = iris.data, iris.target
    rf = RandomForestClassifier(random_state=42)
    scores = cross_val_score(rf, X, y, cv=5)
    print(f"Fold scores: {scores}")
    print(f"Mean accuracy: {scores.mean():.4f}")
    print(f"Std accuracy: {scores.std():.4f}")
    return scores

if __name__ == "__main__":
    solve()""",
    ],
    "medium": [
        """from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def solve():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend()
    plt.savefig('roc_curve.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"AUC: {roc_auc:.4f}")
    return roc_auc

if __name__ == "__main__":
    solve()""",
        """from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV

def solve():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [3, 5, 10],
        'min_samples_split': [2, 5]
    }
    rf = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(rf, param_grid, cv=3, scoring='accuracy')
    grid.fit(X_train, y_train)
    print(f"Best params: {grid.best_params_}")
    print(f"Best score: {grid.best_score_:.4f}")
    print(f"Test score: {grid.score(X_test, y_test):.4f}")
    return grid.best_params_, grid.best_score_

if __name__ == "__main__":
    solve()""",
        """import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve

def solve():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    train_sizes, train_scores, val_scores = learning_curve(
        LogisticRegression(random_state=42), X, y, cv=5,
        train_sizes=np.linspace(0.1, 1.0, 10)
    )
    train_mean = np.mean(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    plt.figure(figsize=(10, 6))
    plt.plot(train_sizes, train_mean, 'o-', label='Training score')
    plt.plot(train_sizes, val_mean, 'o-', label='Validation score')
    plt.xlabel('Training Size')
    plt.ylabel('Score')
    plt.title('Learning Curve')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('learning_curve.png', dpi=150, bbox_inches='tight')
    plt.show()
    return train_sizes, train_mean, val_mean

if __name__ == "__main__":
    solve()""",
    ],
    "hard": [
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve

def solve():
    X, y = make_classification(n_samples=1000, n_features=10, weights=[0.9, 0.1], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)
    idx = np.argmin(np.abs(recalls - 0.8))
    threshold = thresholds[idx]
    precision = precisions[idx]
    print(f"Threshold for 80% recall: {threshold:.4f}")
    print(f"Precision at that threshold: {precision:.4f}")
    return threshold, precision

if __name__ == "__main__":
    solve()""",
        """from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
import numpy as np

def solve():
    X, y = make_classification(n_samples=500, n_features=10, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Random Forest': RandomForestClassifier(random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'SVM': SVC(probability=True, random_state=42),
        'KNN': KNeighborsClassifier(),
    }
    print(f"{'Model':<22} {'Accuracy':<10} {'F1':<10} {'AUC':<10}")
    print("-" * 52)
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else y_pred
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)
        results[name] = {"accuracy": acc, "f1": f1, "auc": auc}
        print(f"{name:<22} {acc:<10.4f} {f1:<10.4f} {auc:<10.4f}")
    return results

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

def solve():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    # Inner CV for hyperparameter tuning
    param_grid = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
    rf = RandomForestClassifier(random_state=42)
    inner_cv = GridSearchCV(rf, param_grid, cv=3)
    # Outer CV for unbiased evaluation
    outer_scores = cross_val_score(inner_cv, X, y, cv=5)
    print(f"Nested CV scores: {outer_scores}")
    print(f"Mean: {outer_scores.mean():.4f} (+/- {outer_scores.std():.4f})")
    return outer_scores

if __name__ == "__main__":
    solve()""",
    ],
}

# Level 06: Advanced ML
LEVEL_06 = {
    "easy": [
        """import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def solve():
    np.random.seed(42)
    X = np.random.rand(50, 1) * 10
    y = 3 * X.flatten()**2 + 2 * X.flatten() + np.random.randn(50) * 10
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Without polynomial
    lr = LinearRegression().fit(X_train, y_train)
    score_linear = lr.score(X_test, y_test)
    # With polynomial
    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    lr_poly = LinearRegression().fit(X_train_poly, y_train)
    score_poly = lr_poly.score(X_test_poly, y_test)
    print(f"Linear R²: {score_linear:.4f}")
    print(f"Polynomial R²: {score_poly:.4f}")
    return score_linear, score_poly

if __name__ == "__main__":
    solve()""",
        """import pandas as pd
from sklearn.preprocessing import LabelEncoder

def solve():
    df = pd.DataFrame({
        'color': ['red', 'blue', 'green', 'red', 'blue'],
        'size': ['S', 'M', 'L', 'M', 'S']
    })
    # Label encoding
    le = LabelEncoder()
    df['color_encoded'] = le.fit_transform(df['color'])
    # One-hot encoding
    df_onehot = pd.get_dummies(df, columns=['size'])
    print("Label encoded:")
    print(df[['color', 'color_encoded']])
    print("\nOne-hot encoded:")
    print(df_onehot)
    return df, df_onehot

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # No scaling
    model = LogisticRegression(random_state=42).fit(X_train, y_train)
    score_none = model.score(X_test, y_test)
    # Standardization
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)
    model = LogisticRegression(random_state=42).fit(X_train_std, y_train)
    score_std = model.score(X_test_std, y_test)
    # Normalization
    scaler = MinMaxScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm = scaler.transform(X_test)
    model = LogisticRegression(random_state=42).fit(X_train_norm, y_train)
    score_norm = model.score(X_test_norm, y_test)
    print(f"No scaling: {score_none:.4f}")
    print(f"Standardization: {score_std:.4f}")
    print(f"Normalization: {score_norm:.4f}")
    return score_none, score_std, score_norm

if __name__ == "__main__":
    solve()""",
    ],
    "medium": [
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

def solve():
    X, y = make_classification(n_samples=1000, n_features=10, weights=[0.95, 0.05], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Without SMOTE
    model = LogisticRegression(random_state=42).fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Without SMOTE:")
    print(classification_report(y_test, y_pred))
    # With SMOTE
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    model = LogisticRegression(random_state=42).fit(X_train_res, y_train_res)
    y_pred = model.predict(X_test)
    print("With SMOTE:")
    print(classification_report(y_test, y_pred))
    return y_pred

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    importances = rf.feature_importances_
    # Select top 5 features
    top_idx = np.argsort(importances)[-5:]
    X_train_top = X_train[:, top_idx]
    X_test_top = X_test[:, top_idx]
    rf_top = RandomForestClassifier(random_state=42).fit(X_train_top, y_train)
    acc_all = rf.score(X_test, y_test)
    acc_top = rf_top.score(X_test_top, y_test)
    print(f"All features accuracy: {acc_all:.4f}")
    print(f"Top 5 features accuracy: {acc_top:.4f}")
    print(f"Top features: {list(top_idx)}")
    return top_idx, acc_all, acc_top

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X = iris.data
    pca = PCA()
    X_pca = pca.fit_transform(X)
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Cumulative: {np.cumsum(pca.explained_variance_ratio_)}")
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('PCA Explained Variance')
    plt.savefig('pca_variance.png', dpi=150, bbox_inches='tight')
    plt.show()
    return pca.explained_variance_ratio_

if __name__ == "__main__":
    solve()""",
    ],
    "hard": [
        """import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

class LogTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return np.log1p(X)

def solve():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('log', LogTransformer()),
        ('scaler', StandardScaler()),
        ('model', LogisticRegression())
    ])
    pipeline.fit(X_train, y_train)
    accuracy = pipeline.score(X_test, y_test)
    print(f"Accuracy with custom transformer: {accuracy:.4f}")
    return accuracy

if __name__ == "__main__":
    solve()""",
        """import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

def solve():
    X, y = make_classification(n_samples=300, n_features=5, n_informative=3, random_state=42)
    df = pd.DataFrame(X, columns=[f'num_{i}' for i in range(5)])
    df['cat'] = np.random.choice(['A', 'B', 'C'], 300)
    df['cat2'] = np.random.choice(['X', 'Y'], 300)
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2, random_state=42)
    preprocessor = ColumnTransformer([
        ('num', Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler())]), [f'num_{i}' for i in range(5)]),
        ('cat', Pipeline([('imputer', SimpleImputer(strategy='most_frequent')), ('onehot', OneHotEncoder())]), ['cat', 'cat2'])
    ])
    model = Pipeline([('preprocessor', preprocessor), ('classifier', RandomForestClassifier(random_state=42))])
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Pipeline accuracy: {accuracy:.4f}")
    return accuracy

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.ensemble import BalancedRandomForestClassifier

def solve():
    X, y = make_classification(n_samples=2000, n_features=10, weights=[0.98, 0.02], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Regular RF
    rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print("Regular RandomForest:")
    print(classification_report(y_test, y_pred))
    # Balanced RF
    brf = BalancedRandomForestClassifier(random_state=42).fit(X_train, y_train)
    y_pred = brf.predict(X_test)
    print("Balanced RandomForest:")
    print(classification_report(y_test, y_pred))
    return y_pred

if __name__ == "__main__":
    solve()""",
    ],
}

# Level 07: Unsupervised Learning
LEVEL_07 = {
    "easy": [
        """import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)
    print(f"Cluster centers:\\n{kmeans.cluster_centers_}")
    print(f"Labels (first 10): {labels[:10]}")
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                c='red', marker='X', s=200, label='Centers')
    plt.legend()
    plt.savefig('kmeans.png', dpi=150, bbox_inches='tight')
    plt.show()
    return labels, kmeans.cluster_centers_

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    inertias = []
    K_range = range(1, 11)
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
    plt.plot(K_range, inertias, 'bo-')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')
    plt.savefig('elbow.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Inertias: {inertias}")
    return inertias

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X = iris.data
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap='viridis')
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA of Iris Dataset')
    plt.colorbar(scatter)
    plt.savefig('pca.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Explained variance: {pca.explained_variance_ratio_}")
    return X_pca

if __name__ == "__main__":
    solve()""",
    ],
    "medium": [
        """import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

def solve():
    X, _ = make_blobs(n_samples=200, centers=3, random_state=42)
    best_k = 2
    best_score = -1
    for k in range(2, 8):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        score = silhouette_score(X, labels)
        print(f"K={k}: silhouette={score:.4f}")
        if score > best_score:
            best_score = score
            best_k = k
    print(f"Best K: {best_k} (silhouette={best_score:.4f})")
    return best_k, best_score

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

def solve():
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # K-Means
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    labels_km = kmeans.fit_predict(X)
    axes[0].scatter(X[:, 0], X[:, 1], c=labels_km, cmap='viridis')
    axes[0].set_title('K-Means')
    # DBSCAN
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels_db = dbscan.fit_predict(X)
    axes[1].scatter(X[:, 0], X[:, 1], c=labels_db, cmap='viridis')
    axes[1].set_title('DBSCAN')
    plt.savefig('kmeans_vs_dbscan.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("K-Means fails on non-spherical data, DBSCAN succeeds")
    return labels_km, labels_db

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

def solve():
    X, _ = make_blobs(n_samples=50, centers=3, random_state=42)
    # Dendrogram
    linked = linkage(X, method='ward')
    plt.figure(figsize=(10, 6))
    dendrogram(linked)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Sample Index')
    plt.ylabel('Distance')
    plt.savefig('dendrogram.png', dpi=150, bbox_inches='tight')
    plt.show()
    # Clustering
    hc = AgglomerativeClustering(n_clusters=3)
    labels = hc.fit_predict(X)
    print(f"Cluster labels: {labels}")
    return labels

if __name__ == "__main__":
    solve()""",
    ],
    "hard": [
        """import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'age': np.random.randint(18, 70, 300),
        'income': np.random.randn(300) * 20000 + 60000,
        'spending': np.random.uniform(1, 100, 300)
    })
    X = StandardScaler().fit_transform(data)
    # Find optimal K
    sil_scores = []
    for k in range(2, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X)
        from sklearn.metrics import silhouette_score
        sil_scores.append(silhouette_score(X, labels))
    best_k = np.argmax(sil_scores) + 2
    km = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    data['cluster'] = labels
    # Profile clusters
    print(data.groupby('cluster').mean())
    # Visualize
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
    plt.title('Customer Segments')
    plt.savefig('segments.png', dpi=150, bbox_inches='tight')
    plt.show()
    return data

if __name__ == "__main__":
    solve()""",
        """import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    normal = np.random.randn(100, 2)
    anomalies = np.random.uniform(-4, 4, (10, 2))
    X = np.vstack([normal, anomalies])
    iso = IsolationForest(contamination=0.1, random_state=42)
    labels = iso.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title('Anomaly Detection (Isolation Forest)')
    plt.savefig('anomalies.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Anomalies detected: {sum(labels == -1)}")
    return labels

if __name__ == "__main__":
    solve()""",
        """from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def solve():
    docs = [
        "machine learning is great for prediction",
        "deep learning uses neural networks",
        "data science involves statistics",
        "python is a programming language",
        "machine learning models need data",
        "neural networks are powerful",
        "statistics helps understand data",
        "python is popular for ml",
    ]
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)
    lda = LatentDirichletAllocation(n_components=2, random_state=42)
    lda.fit(X)
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [feature_names[i] for i in topic.argsort()[-5:]]
        print(f"Topic {topic_idx}: {', '.join(top_words)}")
    return lda

if __name__ == "__main__":
    solve()""",
    ],
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
    all_solutions = {
        "level-05-evaluation": LEVEL_05,
        "level-06-advanced-ml": LEVEL_06,
        "level-07-unsupervised": LEVEL_07,
    }
    for level_name, solutions in all_solutions.items():
        write_solutions(level_name, solutions)
    print(f"\nDone writing solutions for {len(all_solutions)} levels")


if __name__ == "__main__":
    main()
