"""Database models package.

Import all models here to ensure they are registered with SQLAlchemy
and included in Alembic migrations.

Example:
    ```python
    from app.database.models import User, Invoice

    # Models are automatically available
    ```
"""

# Import all models here so they are registered with Base
from app.database.models.user import User
from app.database.models.session import Session, session_users
from app.database.models.invoice import Invoice
from app.database.models.item import Item
from app.database.models.payment import Payment

__all__ = [
    "User",
    "Session",
    "session_users",
    "Invoice",
    "Item",
    "Payment",
]
