"""Database configuration and session management."""

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


# Naming convention for database constraints
# This ensures consistent naming across all database objects
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",  # Index
    "uq": "uq_%(table_name)s_%(column_0_name)s",  # Unique constraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # Check constraint
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # Foreign key
    "pk": "pk_%(table_name)s",  # Primary key
}


class Base(DeclarativeBase):
    """Base class for all database models.

    All models should inherit from this class to be properly
    registered with SQLAlchemy and Alembic migrations.
    """

    metadata = MetaData(naming_convention=NAMING_CONVENTION)


class DatabaseManager:
    """Database connection and session management.

    Manages the lifecycle of database connections and provides
    session factories for dependency injection.

    Attributes:
        engine: SQLAlchemy async engine
        sessionmaker: Factory for creating database sessions
    """

    def __init__(self) -> None:
        """Initialize database manager."""
        self.engine: AsyncEngine | None = None
        self._sessionmaker: async_sessionmaker[AsyncSession] | None = None

    async def connect(self) -> None:
        """Create database engine and session factory.

        Should be called during application startup.
        """
        self.engine = create_async_engine(
            settings.database_url_async,
            echo=settings.DB_ECHO,
            pool_pre_ping=True,
        )
        self._sessionmaker = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def disconnect(self) -> None:
        """Dispose database engine and close all connections.

        Should be called during application shutdown.
        """
        if self.engine:
            await self.engine.dispose()

    def sessionmaker(self) -> async_sessionmaker[AsyncSession]:
        """Get the session factory.

        Returns:
            async_sessionmaker: Factory for creating database sessions

        Raises:
            RuntimeError: If database is not connected
        """
        if self._sessionmaker is None:
            raise RuntimeError("Database is not connected. Call connect() first.")
        return self._sessionmaker


# Global database manager instance
db_manager = DatabaseManager()
