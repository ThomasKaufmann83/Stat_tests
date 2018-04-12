from scipy import stats
import numpy as np

survivors = np.array([[1781,135], [1443, 47]])
stats.chi2_contingency(survivors)

