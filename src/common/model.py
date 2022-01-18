from tortoise import fields
from tortoise.models import Model


class TimestampMixin:
    """
    Store created_at, modified_at datetime.
    """

    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class BaseModel(TimestampMixin, Model):
    """
    Use uuid as primary key.
    Store created_at, modified_at.
    """
    id = fields.UUIDField(pk=True)

