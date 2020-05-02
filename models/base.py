from sqlalchemy import Column, Integer, DateTime, func, Boolean


class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now(), server_default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(),
                        nullable=False, server_default=func.now())
    deleted_at = Column(DateTime, nullable=True)
    deleted = Column(Boolean, default=False)
