

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_URBANFIXEDREGISTERED(Base):
    __tablename__ = "MAC_URBANFIXEDREGISTERED"

    SGNMONTH = Column(String(14, u'utf8_bin'), primary_key=True, nullable=False)
    REGISTEREDID = Column(String(20, u'utf8_bin'), primary_key=True, nullable=False)
    FIXEDASSETSINVEST = Column(Numeric(18, 4))
    FIXEDASSETSINVESTYOY = Column(Numeric(10, 4))