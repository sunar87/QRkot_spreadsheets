from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDReservation(CRUDBase):

    @staticmethod
    async def get_by_user(
            session: AsyncSession,
            user: User,
    ) -> List[Donation]:
        donations = await session.execute(
            select(Donation).where(Donation.user_id == user.id)
        )
        return donations.scalars().all()


donation_crud = CRUDReservation(Donation)
