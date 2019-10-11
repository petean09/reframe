import pandas as pd
import pytest
from reframe import Relation


def test_rename_1():
    data_expected = {'color': ['green', 'blue']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    data_real = {'hello': ['green', 'blue']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.rename("hello", "color")

    assert r.equals(r_expected)

def test_rename_2():
    data_expected = {'color': ['green', 'blue'], 'food': ['banana', 'cookie']}
    df_expected = pd.DataFrame(data=data_expected)
    r_expected = Relation(df_expected)

    data_real = {'color': ['green', 'blue'], 'hello': ['banana', 'cookie']}
    df = pd.DataFrame(data=data_real)
    r = Relation(df)
    r = r.rename("hello", "food")

    assert r.equals(r_expected)