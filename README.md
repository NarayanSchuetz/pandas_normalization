# Pandas Normalization
Monkey patches pandas to directly allow data normalization by means of min-max scaling and zero-mean unit-variance standardization  unit variance  
This is only for convenience as I found myself too often having to write this by hand or use sklearn, which both leads
to less concise code.


## PIP Install
To pip install this monkey patch you may use the following command:

    pip install git+https://github.com/NarayanSchuetz/pandas_normalization.git


## Usage
First you need to import pandas and load the monkey patch

    import pandas as pd
    from pandas_normalization import pandas_normalization_monkeypatch
    
Now you can use the `standardize` and `scale` methods on DataFrames and Series objects.

To standardize a Pandas Series or DataFrame to zero mean and unit variance:

    a = pd.Series([1,5,2,10,100,-2])
    a.standardize().hist()
    
    b = pd.DataFrame({
                        "a": [1, 5, 2, 10, 100, -2],
                        "b":  [5, 200, 31, -10, 2, 78] 
                     })

    b.standardize()
    
To min-max scale a Pandas Series or DataFrame to a 0-1 interval:

    a = pd.Series([1,5,2,10,100,-2])
    a.scale().hist()
    
    b = pd.DataFrame({
                        "a": [1, 5, 2, 10, 100, -2],
                        "b":  [5, 200, 31, -10, 2, 78] 
                     })

    b.scale()
    

As an alternative to `pip` one can also simply copy the code in `pandas_normalization_monkeypatch` module after the
Pandas import.  


## Note:
Has been tested with Pandas version `1.1.3` and Python `3.8`. 

