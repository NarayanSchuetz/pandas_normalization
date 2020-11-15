"""
 Created by Narayan Schuetz at 15.11.20 
 University of Bern
 
 This file is subject to the terms and conditions defined in
 file 'LICENSE.txt', which is part of this source code package.
"""


import unittest
import pandas as pd
import numpy as np

from pandas_normalization import pandas_normalization_monkeypatch


class TestScalingPatchedSeries(unittest.TestCase):

    def setUp(self) -> None:
        self.test_series = pd.Series(np.random.normal(102, 2, 1000))
        self.test_series_empty = pd.Series(dtype=float)
        self.test_series_nan = self.test_series.copy()
        self.test_series_nan.iloc[:10] = np.nan

    def test_standardize_normal(self):
        standardized = self.test_series.standardize()

        mean = standardized.mean()
        var = standardized.var()

        self.assertAlmostEqual(mean, 0)
        self.assertAlmostEqual(var, 1)

    def test_standardize_nan(self):
        standardized_nan = self.test_series_nan.standardize()

        mean = standardized_nan.mean()
        var = standardized_nan.var()

        self.assertAlmostEqual(mean, 0)
        self.assertAlmostEqual(var, 1)

    def test_standardize_empty(self):
        standardized_empty = self.test_series_empty.standardize()
        self.assertTrue(standardized_empty.empty)

    def test_scale_normal(self):
        scaled = self.test_series.scale()

        min = scaled.min()
        max = scaled.max()

        self.assertTrue(min >= 0)
        self.assertTrue(max <= 1)

    def test_scale_nan(self):
        scaled_nan = self.test_series_nan.scale()

        min = scaled_nan.min()
        max = scaled_nan.max()

        self.assertTrue(min >= 0)
        self.assertTrue(max <= 1)

    def test_scale_empty(self):
        scaled_empty = self.test_series_empty.scale()
        self.assertTrue(scaled_empty.empty)


class TestScalingPatchedDataFrame(unittest.TestCase):

    def setUp(self) -> None:
        self.test_df = pd.DataFrame({"a": np.random.normal(102, 2, 1000),
                                     "b": np.random.normal(-202, 5, 1000)})

        self.test_df_empty = pd.DataFrame(dtype=float)
        self.test_df_nan = self.test_df.copy()
        self.test_df_nan.iloc[:10] = np.nan

    def test_standardize_normal(self):
        standardized = self.test_df.standardize()

        mean = standardized.mean()
        var = standardized.var()

        self.assertAlmostEqual(mean.a, 0)
        self.assertAlmostEqual(mean.b, 0)
        self.assertAlmostEqual(var.a, 1)
        self.assertAlmostEqual(var.b, 1)

    def test_standardize_nan(self):
        standardized_nan = self.test_df_nan.standardize()

        mean = standardized_nan.mean()
        var = standardized_nan.var()

        self.assertAlmostEqual(mean.a, 0)
        self.assertAlmostEqual(mean.b, 0)
        self.assertAlmostEqual(var.a, 1)
        self.assertAlmostEqual(var.b, 1)

    def test_standardize_empty(self):
        standardized_empty = self.test_df_empty.standardize()
        self.assertTrue(standardized_empty.empty)

    def test_scale_normal(self):
        scaled = self.test_df.scale()

        min = scaled.min()
        max = scaled.max()

        self.assertTrue(min.a >= 0)
        self.assertTrue(min.b >= 0)
        self.assertTrue(max.a <= 1)
        self.assertTrue(max.b <= 1)

    def test_scale_nan(self):
        scaled_nan = self.test_df_nan.scale()

        min = scaled_nan.min()
        max = scaled_nan.max()

        self.assertTrue(min.a >= 0)
        self.assertTrue(min.b >= 0)
        self.assertTrue(max.a <= 1)
        self.assertTrue(max.b <= 1)

    def test_scale_empty(self):
        scaled_empty = self.test_df_empty.scale()
        self.assertTrue(scaled_empty.empty)
