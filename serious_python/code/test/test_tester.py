from src.tester import *

def test_true():
    assert True

def test_false():
    assert False

def test_run():
    result = tester.run()
    assert result is None