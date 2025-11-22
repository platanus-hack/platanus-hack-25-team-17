"""Session model definition."""

from sqlalchemy import String, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.database.database import Base

# Association table for many-to-many relationship between Session and User
session_users = Table(
    "session_users",
    Base.metadata,
    Column("session_id", ForeignKey("sessions.id"), primary_key=True),
    Column("user_id", ForeignKey("users.id"), primary_key=True),
)


class Session(Base):
    """Session model.

    Represents a session with multiple users participating.

    Attributes:
        id: Primary key
        description: Description of the session
        users: Users participating in this session (many-to-many)
    """

    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

    # Relationships
    users: Mapped[list["User"]] = relationship(secondary=session_users, back_populates="sessions")
