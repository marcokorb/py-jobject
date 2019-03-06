"""
Assert that type redefinition works.
"""

from datetime import datetime
from dateutil.tz import tzutc
from pytest import fixture
from py_jobject import from_dict, get_type_definition, set_type_definition

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

def test_from_dict_date_redefined():
    """
    Execute the test.
    """

    source = {
        'datetime': '2019-03-06 15:36:21'
    }

    result = from_dict(source, SeveralDataTypes)

    assert isinstance(result, SeveralDataTypes)
    assert result.datetime == datetime(2019, 3, 6, 18, 36, 21, tzinfo=tzutc())
