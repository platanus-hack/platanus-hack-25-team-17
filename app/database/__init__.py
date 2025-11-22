"""Database package exports.

This module exports all database-related components for easy importing
throughout the application.

Example:
    ```python
    from app.database import Base, db_manager

    # Create a new model
    class User(Base):
        __tablename__ = "users"
        ...

    # Use in a route
    from app.routers.deps import get_db

    @router.get("/items")
    async def get_items(db: AsyncSession = Depends(get_db)):
        ...
    ```
"""

from app.database.database import Base, db_manager

__all__ = [
    "Base",
    "db_manager",
]
