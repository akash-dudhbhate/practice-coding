"""Level 00 — Setup & Math — Easy P01 Solution"""

def check_env():
    import numpy
    import pandas
    import sklearn
    return {
        "numpy": numpy.__version__,
        "pandas": pandas.__version__,
        "sklearn": sklearn.__version__,
    }

if __name__ == "__main__":
    print(check_env())
