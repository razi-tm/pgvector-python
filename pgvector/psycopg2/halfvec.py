from psycopg2.extensions import adapt, new_type, register_adapter, register_type
from ..utils import HalfVec


class HalfvecAdapter(object):
    def __init__(self, halfvec):
        self._halfvec = halfvec

    def getquoted(self):
        return adapt(HalfVec.to_db(self._halfvec)).getquoted()


def cast_halfvec(value, cur):
    return HalfVec.from_db(value)


def register_halfvec_info(oid):
    halfvec = new_type((oid,), 'HALFVEC', cast_halfvec)
    register_type(halfvec)
    register_adapter(HalfVec, HalfvecAdapter)
