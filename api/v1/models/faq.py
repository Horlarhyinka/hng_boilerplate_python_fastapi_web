#!/usr/bin/env python3
""" The Job Model Class
"""
from sqlalchemy import (
        Column,
        Integer,
        String,
        Text,
        Date,
        ForeignKey,
        Numeric,
        DateTime,
        func,
        )
from sqlalchemy.orm import relationship
from datetime import datetime
from api.v1.models.base import Base
from api.v1.models.base_model import BaseModel
from uuid_extensions import uuid7
from sqlalchemy.dialects.postgresql import UUID


class Job(BaseModel, Base):
    __tablename__ = 'faqs'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    question = Column(String(1024), nullable=False)
    answer = Column(String(1024), nullable=False)
    category = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

