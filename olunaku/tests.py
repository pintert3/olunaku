import pytest
from datetime import datetime as dt
from olunaku import lg_ctime, lgtr_ctime

TEST_DATE = dt(2020,9,26,12,5)

def test_lg_ctime():
    assert(lg_ctime(TEST_DATE) == 'Lw6 Og9 26 12:05:00 2020')

def test_lgtr_ctime():
    assert(lgtr_ctime(TEST_DATE) == 'Lw6 Mut 26 12:05:00 2020')

