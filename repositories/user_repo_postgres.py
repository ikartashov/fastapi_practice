from database.db_models import UserBase
from database.db_postgres import get_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


def add_user(name: str):
    with get_session() as session:
        try:
            new_user = UserBase(name=name)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            return new_user
        except IntegrityError:
            session.rollback()
            return None


def get_users():
    with get_session() as session:
        all_users = session.scalars(select(UserBase)).all()
        return all_users


def get_user_by_id(user_id: int):
    with get_session() as session:
        user_by_id = session.get(UserBase, user_id)
        if not user_by_id:
            return None
        return user_by_id


def get_user_by_name(name: str):
    with get_session() as session:
        user_by_name = session.scalars(
            select(UserBase).where(UserBase.name == name)).first()
        if not user_by_name:
            return None
        return user_by_name


def update_user(user_id: int, new_name: str):
    with get_session() as session:
        user_to_change = session.get(UserBase, user_id)
        if not user_to_change:
            return None
        else:
            user_to_change.name = new_name
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                raise
            session.refresh(user_to_change)
            return user_to_change


def delete_user(user_id: int):
    with get_session() as session:
        user_to_delete = session.get(UserBase, user_id)
        if not user_to_delete:
            return None
        else:
            session.delete(user_to_delete)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                return None
            return user_to_delete
