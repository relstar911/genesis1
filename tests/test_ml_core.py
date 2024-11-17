import pytest
import numpy as np
from genesis.src.core.ml_core import MLCore

def test_ml_core_initialization():
    ml_core = MLCore()
    assert ml_core.model is None
    assert isinstance(ml_core.config, dict)

def test_data_processing():
    ml_core = MLCore()
    test_data = np.array([[1, 2, 3], [4, 5, 6]])
    processed_data = ml_core.process_data(test_data)
    assert isinstance(processed_data, np.ndarray) 