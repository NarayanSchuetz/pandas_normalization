"""
 Created by Narayan Schuetz at 15.11.20 
 University of Bern
 
 This file is subject to the terms and conditions defined in
 file 'LICENSE.txt', which is part of this source code package.
"""


import pandas as pd
import importlib


class PandasNormalization:

    def standardize(self):
        return (self - self.mean()) / self.std()

    def scale(self):
        return (self - self.min()) / (self.max() - self.min())


class ScalingPatchedSeries(pd.core.series.Series, PandasNormalization):

    @property
    def _constructor(self):
        return ScalingPatchedSeries


class ScalingPatchedDataFrame(pd.core.frame.DataFrame, PandasNormalization):

    @property
    def _series(self):
        return {
            item: ScalingPatchedSeries(
                self._mgr.iget(idx), index=self.index, name=item, fastpath=True
            )
            for idx, item in enumerate(self.columns)
        }


pd.Series = pd.core.series.Series = ScalingPatchedSeries
importlib.reload(pd.core.frame)
pd.DataFrame = pd.core.frame.DataFrame = ScalingPatchedDataFrame