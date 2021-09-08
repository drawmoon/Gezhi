from date_parser import str_to_digit, parse, merge
from typing import List, Tuple
import pytest

merge_testdata = [
    ([("2017年", "DATE", 0, 1), ("2021年", "DATE", 3, 4)], [("2017年", "DATE", 0, 1), ("2021年", "DATE", 3, 4)]),
    ([("第四", "ORDINAL", 0, 1), ("季度", "DATE", 1, 2)], [("第四季度", "DATE", 0, 2)]),
    ([("2021年7月28日", "DATE", 4, 7), ("当天", "DATE", 7, 8)], [("2021年7月28日当天", "DATE", 4, 8)]),
    ([("4", "CARDINAL", 0, 1), ("季度", "DATE", 1, 2)], [("4季度", "DATE", 0, 2)])
]


@pytest.mark.parametrize("ner,expected_ner", merge_testdata)
def test_merge(ner: List[Tuple[str, str, int, int]], expected_ner: List[Tuple[str, str, int, int]]):
    rst = merge(ner)
    assert len(rst) == len(expected_ner)
    for i, t in enumerate(expected_ner):
        assert rst[i] == t


to_digit_testdata = [
    ("17", "year", 2017),
    ("2017", "year", 2017),
    ("一七", "year", 2017),
    ("二零一七", "year", 2017),
    ("07", "year", 2007),
    ("12", "month", 12),
    ("十二", "month", 12),
    ("1", "month", 1),
    ("一", "month", 1),
    ("31", "day", 31),
    ("三十一", "day", 31),
    ("1", "day", 1),
    ("一", "day", 1),
]


@pytest.mark.parametrize("input_str,typ,expected", to_digit_testdata, ids=[i[0] for i in to_digit_testdata])
def test_str_to_digit(input_str: str, typ: str, expected: int):
    rst = str_to_digit(input_str, typ)
    assert rst == expected


parse_testdata = [
    ("2017年", ("2017-01-01 00:00:00", "2018-01-01 00:00:00")),
    ("二零一七年", ("2017-01-01 00:00:00", "2018-01-01 00:00:00")),
    ("17年", ("2017-01-01 00:00:00", "2018-01-01 00:00:00")),
    ("一七年", ("2017-01-01 00:00:00", "2018-01-01 00:00:00")),
    ("2017年7月", ("2017-07-01 00:00:00", "2017-08-01 00:00:00")),
    ("二零一七年七月", ("2017-07-01 00:00:00", "2017-08-01 00:00:00")),
    ("7月", ("2021-07-01 00:00:00", "2021-08-01 00:00:00")),
    ("七月", ("2021-07-01 00:00:00", "2021-08-01 00:00:00")),
    ("2017/7/23", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("2017-7-23", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("2017年7月23日", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("二零一七年七月二十三", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("二零一七年七月二十三日", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("二零一七年七月二十三日当天", ("2017-07-23 00:00:00", "2017-07-24 00:00:00")),
    ("07/11", ("2021-07-11 00:00:00", "2021-07-12 00:00:00")),
    ("07-11", ("2021-07-11 00:00:00", "2021-07-12 00:00:00")),
    ("07月11", ("2021-07-11 00:00:00", "2021-07-12 00:00:00")),
    ("07月11日", ("2021-07-11 00:00:00", "2021-07-12 00:00:00")),
    ("11日当天", ("2021-09-11 00:00:00", "2021-09-12 00:00:00")),
    ("十一日当天", ("2021-09-11 00:00:00", "2021-09-12 00:00:00")),
    ("今年", ("2021-01-01 00:00:00", "2022-01-01 00:00:00")),
    ("明年", ("2022-01-01 00:00:00", "2023-01-01 00:00:00")),
    ("去年", ("2020-01-01 00:00:00", "2021-01-01 00:00:00")),
    ("前年", ("2019-01-01 00:00:00", "2020-01-01 00:00:00")),
    ("本月", ("2021-09-01 00:00:00", "2021-10-01 00:00:00")),
    ("上月", ("2021-08-01 00:00:00", "2021-09-01 00:00:00")),
    ("下月", ("2021-10-01 00:00:00", "2021-11-01 00:00:00")),
    ("今天", ("2021-09-01 00:00:00", "2021-09-02 00:00:00")),
    ("明天", ("2021-09-02 00:00:00", "2021-09-03 00:00:00")),
    ("后天", ("2021-09-03 00:00:00", "2021-09-04 00:00:00")),
    ("昨天", ("2021-08-31 00:00:00", "2021-09-01 00:00:00")),
    ("前天", ("2021-08-30 00:00:00", "2021-08-31 00:00:00")),
    ("上午", ("2021-09-01 00:00:00", "2021-09-01 12:00:00")),
    ("下午", ("2021-09-01 12:00:00", "2021-09-01 19:00:00")),
    ("本周", ("2021-08-30 00:00:00", "2021-09-06 00:00:00")),
    ("上周", ("2021-08-23 00:00:00", "2021-08-30 00:00:00")),
    ("下周", ("2021-09-06 00:00:00", "2021-09-13 00:00:00")),
    ("上半年", ("2021-01-01 00:00:00", "2021-07-01 00:00:00")),
    ("下半年", ("2021-07-01 00:00:00", "2022-01-01 00:00:00")),
    ("第一季度", ("2021-01-01 00:00:00", "2021-04-01 00:00:00")),
    ("第1季度", ("2021-01-01 00:00:00", "2021-04-01 00:00:00")),
    ("一季度", ("2021-01-01 00:00:00", "2021-04-01 00:00:00")),
    ("1季度", ("2021-01-01 00:00:00", "2021-04-01 00:00:00")),
    ("第二季度", ("2021-04-01 00:00:00", "2021-07-01 00:00:00")),
    ("第2季度", ("2021-04-01 00:00:00", "2021-07-01 00:00:00")),
    ("2季度", ("2021-04-01 00:00:00", "2021-07-01 00:00:00")),
    ("二季度", ("2021-04-01 00:00:00", "2021-07-01 00:00:00")),
    ("第三季度", ("2021-07-01 00:00:00", "2021-10-01 00:00:00")),
    ("第3季度", ("2021-07-01 00:00:00", "2021-10-01 00:00:00")),
    ("三季度", ("2021-07-01 00:00:00", "2021-10-01 00:00:00")),
    ("3季度", ("2021-07-01 00:00:00", "2021-10-01 00:00:00")),
    ("第四季度", ("2021-10-01 00:00:00", "2022-01-01 00:00:00")),
    ("第4季度", ("2021-10-01 00:00:00", "2022-01-01 00:00:00")),
    ("四季度", ("2021-10-01 00:00:00", "2022-01-01 00:00:00")),
    ("4季度", ("2021-10-01 00:00:00", "2022-01-01 00:00:00")),
    ("2017年上半年", ("2017-01-01 00:00:00", "2017-07-01 00:00:00")),
    ("17年上半年", ("2017-01-01 00:00:00", "2017-07-01 00:00:00")),
    ("二零一七年上半年", ("2017-01-01 00:00:00", "2017-07-01 00:00:00")),
    ("一七年上半年", ("2017-01-01 00:00:00", "2017-07-01 00:00:00")),
    ("2017年下半年", ("2017-07-01 00:00:00", "2018-01-01 00:00:00")),
    ("17年下半年", ("2017-07-01 00:00:00", "2018-01-01 00:00:00")),
    ("二零一七年下半年", ("2017-07-01 00:00:00", "2018-01-01 00:00:00")),
    ("一七年下半年", ("2017-07-01 00:00:00", "2018-01-01 00:00:00")),
    ("2019年第一季度", ("2019-01-01 00:00:00", "2019-04-01 00:00:00")),
    ("19年第一季度", ("2019-01-01 00:00:00", "2019-04-01 00:00:00")),
    ("二零一九年第一季度", ("2019-01-01 00:00:00", "2019-04-01 00:00:00")),
    ("一九年第一季度", ("2019-01-01 00:00:00", "2019-04-01 00:00:00")),
    ("2019年第二季度", ("2019-04-01 00:00:00", "2019-07-01 00:00:00")),
    ("19年第二季度", ("2019-04-01 00:00:00", "2019-07-01 00:00:00")),
    ("二零一九年第二季度", ("2019-04-01 00:00:00", "2019-07-01 00:00:00")),
    ("一九年第二季度", ("2019-04-01 00:00:00", "2019-07-01 00:00:00")),
    ("2019年第三季度", ("2019-07-01 00:00:00", "2019-10-01 00:00:00")),
    ("19年第三季度", ("2019-07-01 00:00:00", "2019-10-01 00:00:00")),
    ("二零一九年第三季度", ("2019-07-01 00:00:00", "2019-10-01 00:00:00")),
    ("一九年第三季度", ("2019-07-01 00:00:00", "2019-10-01 00:00:00")),
    ("2019年第四季度", ("2019-10-01 00:00:00", "2020-01-01 00:00:00")),
    ("19年第四季度", ("2019-10-01 00:00:00", "2020-01-01 00:00:00")),
    ("二零一九年第四季度", ("2019-10-01 00:00:00", "2020-01-01 00:00:00")),
    ("一九年第四季度", ("2019-10-01 00:00:00", "2020-01-01 00:00:00"))
]


@pytest.mark.parametrize("input_str,expected", parse_testdata, ids=[i[0] for i in parse_testdata])
def test_parse(input_str: str, expected: Tuple[str, str]):
    rst = parse(input_str)
    assert len(rst) == len(expected)
    for i, s in enumerate(expected):
        assert rst[i] == s
