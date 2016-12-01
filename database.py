# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///./test.db', convert_unicode=True) # �������ݿ�����( ��ǰĿ¼�±������ݿ��ļ�) 
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # �����ﵼ�����еĿ����붨��ģ���йص�ģ�飬�������ǲŻ���ʵ�
    # �� metadata ��ע�ᡣ�����������ò��ڵ�һ��ִ�� init_db() ʱ
    # �ȵ������ǡ�
    import models
    Base.metadata.create_all(bind=engine)