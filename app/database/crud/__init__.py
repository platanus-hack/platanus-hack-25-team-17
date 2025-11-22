"""CRUD operations package.

This package contains CRUD (Create, Read, Update, Delete) operations
for database models.

Example:
    ```python
    from app.database.crud import user_crud

    # In a route
    @router.get("/users/{user_id}")
    async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
        return await user_crud.get(db, id=user_id)
    ```
"""

# Import all CRUD modules here
# Example:
# from app.database.crud.user import user_crud

__all__ = [
    # Add your CRUD modules here
    # "user_crud",
]
