# -*- coding: utf-8 -*-
"""DenseLayers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BL-JAyDE6sAFlAzfXmBnv9D34iZ88Q76
"""

class DenseLayer():
  def __init__(self, Data, units ):
    self.units = units
    self.prev_units = Data.shape[0]

    self.W = np.random.randn(units, self.prev_units) * 0.01
    self.b = np.zeros((units,1))