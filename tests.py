from data_capture import DataCapture


def test_add_data_capture():
    capture = DataCapture()
    expected_value_adding_one = 1
    expected_value_adding_two_twice = 2
    capture.add(1)
    capture.add(2)
    capture.add(2)
    assert capture.data[1] == expected_value_adding_one
    assert capture.data[2] == expected_value_adding_two_twice


def test_build_stats():
    expected_list_after_build_stats = [0, 1, 3]
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(2)
    stats = capture.build_stats()
    assert stats.numbers[0] == expected_list_after_build_stats[0]
    assert stats.numbers[1] == expected_list_after_build_stats[1]
    assert stats.numbers[2] == expected_list_after_build_stats[2]


def test_Statistic():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.less(4) == 2
    assert stats.between(3, 6) == 5
    assert stats.greater(4) == 3
