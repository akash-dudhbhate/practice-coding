"""
Auto-Check System — Level 03 (Data Visualization)
===================================================
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import os
import sys
import glob
import importlib.util

# Force headless plotting during checks
import matplotlib
matplotlib.use('Agg')


def load_module(filepath):
    spec = importlib.util.spec_from_file_location("solution", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _find_file(level_dir, level, num):
    num_clean = num.lstrip("p")
    filepath = os.path.join(level_dir, level, f"p{num_clean}-solve.py")
    if not os.path.exists(filepath):
        pattern = os.path.join(level_dir, level, f"p{num_clean}-*.py")
        matches = [f for f in glob.glob(pattern) if "solutions" not in f]
        if matches:
            filepath = matches[0]
    return filepath


def check_easy_p01(module):
    import numpy as np
    if not hasattr(module, 'plot_trig'):
        return False, "Function 'plot_trig' not found"
    x = module.plot_trig()
    if not isinstance(x, np.ndarray):
        return False, f"Expected np.ndarray, got {type(x)}"
    if len(x) != 100:
        return False, f"Expected 100 points, got {len(x)}"
    if not (np.isclose(x[0], 0) and np.isclose(x[-1], 10)):
        return False, f"x should go 0→10, got {x[0]}→{x[-1]}"
    if not os.path.exists('trig_plot.png'):
        return False, "trig_plot.png was not saved"
    return True, "All tests passed!"


def check_easy_p02(module):
    import numpy as np
    if not hasattr(module, 'plot_scatter'):
        return False, "Function 'plot_scatter' not found"
    result = module.plot_scatter()
    if not isinstance(result, tuple) or len(result) != 3:
        return False, "Should return (height, weight, gender)"
    h, w, g = result
    if len(h) != 100:
        return False, f"Expected 100 heights, got {len(h)}"
    if not (160 < h.mean() < 180):
        return False, f"Mean height should be ~170, got {h.mean():.1f}"
    if set(g) != {'M', 'F'}:
        return False, "gender should contain 'M' and 'F'"
    if not os.path.exists('scatter_plot.png'):
        return False, "scatter_plot.png was not saved"
    return True, "All tests passed!"


def check_easy_p03(module):
    import numpy as np
    if not hasattr(module, 'plot_histogram'):
        return False, "Function 'plot_histogram' not found"
    scores = module.plot_histogram()
    if len(scores) != 200:
        return False, f"Expected 200 scores, got {len(scores)}"
    if scores.min() < 0 or scores.max() > 100:
        return False, "Scores should be clipped to 0-100"
    if not (70 < scores.mean() < 80):
        return False, f"Mean should be ~75, got {scores.mean():.1f}"
    if not os.path.exists('histogram.png'):
        return False, "histogram.png was not saved"
    return True, "All tests passed!"


def check_medium_p01(module):
    import pandas as pd
    if not hasattr(module, 'plot_corr'):
        return False, "Function 'plot_corr' not found"
    corr = module.plot_corr()
    if not isinstance(corr, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(corr)}"
    if corr.shape != (5, 5):
        return False, f"Expected (5,5) matrix, got {corr.shape}"
    if not abs(corr.loc['feature_a', 'feature_a'] - 1.0) < 0.001:
        return False, "Diagonal should be 1.0 (self-correlation)"
    if not os.path.exists('correlation_heatmap.png'):
        return False, "correlation_heatmap.png was not saved"
    return True, "All tests passed!"


def check_medium_p02(module):
    if not hasattr(module, 'plot_dashboard'):
        return False, "Function 'plot_dashboard' not found"
    fig = module.plot_dashboard()
    if len(fig.axes) != 4:
        return False, f"Expected 4 subplots, got {len(fig.axes)}"
    if not os.path.exists('dashboard.png'):
        return False, "dashboard.png was not saved"
    return True, "All tests passed!"


def check_medium_p03(module):
    import pandas as pd
    if not hasattr(module, 'plot_box'):
        return False, "Function 'plot_box' not found"
    df = module.plot_box()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if df.shape != (200, 2):
        return False, f"Expected (200,2), got {df.shape}"
    means = df.groupby('category')['value'].mean()
    if not (45 < means['A'] < 55 and 55 < means['B'] < 65):
        return False, f"Group means wrong: {dict(means)}"
    if not os.path.exists('boxplot.png'):
        return False, "boxplot.png was not saved"
    return True, "All tests passed!"


def check_hard_p01(module):
    import pandas as pd
    if not hasattr(module, 'plot_sales'):
        return False, "Function 'plot_sales' not found"
    df = module.plot_sales()
    if not isinstance(df, pd.DataFrame):
        return False, f"Expected DataFrame, got {type(df)}"
    if df.shape != (90, 4):
        return False, f"Expected (90,4), got {df.shape}"
    if not (9000 < df['revenue'].mean() < 11000):
        return False, f"Mean revenue should be ~10000, got {df['revenue'].mean():.0f}"
    if not os.path.exists('sales_dashboard.png'):
        return False, "sales_dashboard.png was not saved"
    return True, "All tests passed!"


def check_hard_p02(module):
    import numpy as np
    if not hasattr(module, 'animate'):
        return False, "Function 'animate' not found"
    x = module.animate()
    if len(x) != 100:
        return False, f"Expected 100 points, got {len(x)}"
    if not np.isclose(x[-1], 2 * np.pi):
        return False, f"x[-1] should be 2π (6.2832), got {x[-1]}"
    return True, "All tests passed!"


def check_hard_p03(module):
    if not hasattr(module, 'plot_publication'):
        return False, "Function 'plot_publication' not found"
    x = module.plot_publication()
    if not os.path.exists('publication_figure.png'):
        return False, "publication_figure.png was not saved"
    if len(x) != 100:
        return False, f"Expected 100 points, got {len(x)}"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,
    "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01,
    "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,
    "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <level>/<problem>")
        sys.exit(1)

    target = sys.argv[1]
    level_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(level_dir)  # plots save relative to level dir

    if target == "all":
        print("=" * 60)
        print("  LEVEL 03 — AUTO-CHECK ALL")
        print("=" * 60)
        for check_id, check_func in CHECKS.items():
            level, num = check_id.split("/")
            filepath = _find_file(level_dir, level, num)
            if not os.path.exists(filepath):
                print(f"  {check_id}: FILE NOT FOUND")
                continue
            try:
                module = load_module(filepath)
                passed, msg = check_func(module)
                status = "PASS" if passed else "FAIL"
                print(f"  {check_id}: {status} — {msg}")
            except Exception as e:
                print(f"  {check_id}: ERROR — {e}")
        print("=" * 60)
        return

    level, num = target.split("/")
    check_id = f"{level}/{num}"
    if check_id not in CHECKS:
        print(f"Error: unknown problem '{check_id}'")
        sys.exit(1)

    filepath = _find_file(level_dir, level, num)
    if not os.path.exists(filepath):
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        module = load_module(filepath)
        passed, msg = CHECKS[check_id](module)
        if passed:
            print(f"PASS — {msg}")
            print(f"  Add '# DONE' to the first line of {filepath}")
        else:
            print(f"FAIL — {msg}")
    except Exception as e:
        print(f"ERROR — {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
