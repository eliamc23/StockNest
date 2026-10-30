from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.mixins import TimestampMixin


#The Organization class represents an organization (tenant) in the database.
class Organization(Base, TimestampMixin):
    __tablename__ = "organizations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(90), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    