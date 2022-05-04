import new1
import mock

print("Lab 2 testing")

def test_get_user_input():
    result = []
    test_arr = [5,6,39,8]

    with mock.patch('builtins.input', return_value="5,6,39,8"):
        assert new1.get_user_input()==test_arr

def test_calc_average():
    result = []
    input_arr = [1,1,1,1]
    test = 1
    result = new1.calc_average(input_arr)
    assert(result==test)