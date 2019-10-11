import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r_1():
    data_1 = {'color': ['red', 'purple'], 'animal': ['cat', 'dog']}
    df_1 = pd.DataFrame(data=data_1)
    return Relation(df_1)

@pytest.fixture
def r_2():
    data_2 = {'color': ['green', 'blue'], 'food': ['apple', 'banana']}
    df_2 = pd.DataFrame(data=data_2)
    return Relation(df_2)


def test_semi_join_left(r_1, r_2):
    
    data_expected = {'color': ['red', 'purple']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    r = r_1.semi_join(r_2)
    
    assert r.equals(r_expected)

def test_semi_join_right(r_1, r_2):
        
    data_expected = {'color': ['green', 'blue']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)
    r = r_2.semi_join(r_1)
    
    assert r.equals(r_expected)