from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.database.sql.session import get_all_session_users
from app.integrations.kapso import send_text_message


async def send_message_to_all_session_users(db_session: AsyncSession, session_id: UUID, message: str) -> None:
    users = await get_all_session_users(db_session, session_id)
    for user_id, phone_number in users:
        send_text_message(phone_number, message)
