"""Create models"""
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class User(Base):
    """user

    Args:
        Base (model): base_model
    """
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    number_phone: Mapped[int] = mapped_column(Integer, unique=True)
    order_id: Mapped["Order"] = relationship(
        "Order",
        back_populates="user",
        # Ключевой параметр для связи один-к-одному
        lazy="joined"  # Автоматически подгружает profile при запросе user
    )


class Order(Base):
    __tablename__ = 'orders'

    products: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders"
    )
