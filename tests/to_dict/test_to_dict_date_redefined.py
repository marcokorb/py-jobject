"""
Assert that type redefinition works.
"""

from datetime import datetime
from dateutil.tz import tzutc
from pytest import fixture
from py_jobject import to_dict, get_type_definition, set_type_definition

from ..definitions import BrazilianDatetimeDefinition
from ..objects import SeveralDataTypes

@fixture(scope='function', autouse=True)
def datetime_redefinition():
    """
    Redefines type `datetime`.
    """

    original_def = get_type_definition(datetime)
    set_type_definition(datetime, BrazilianDatetimeDefinition)

    yield

    set_type_definition(datetime, original_def)

def test_to_dict_date_redefined():
    """
    Execute the test.
    """

    obj = SeveralDataTypes()
    obj.datetime = datetime(2019, 3, 6, 18, 36, 21, tzinfo=tzutc())

    result = to_dict(obj)

    assert result == {
        'datetime': '2019-03-06 15:36:21'
    }
