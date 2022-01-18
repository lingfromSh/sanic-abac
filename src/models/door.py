from tortoise import fields
from common.fields import CodeField
from common.model import BaseModel


class Door(BaseModel):
    """
    Doors for allowing specified key to open.
    """
    name = fields.CharField(max_length=255)
    desc = fields.TextField()
    py_code = CodeField()

    def is_open(self, value):
        # TODO
        raise NotImplementedError

    @property
    def expected_params(self):
        # TODO
        raise NotImplementedError


class BasicAttributeTypeDoor(BaseModel):
    """
    Allowed basic key type for door.
    """

    basic_attribute_type = fields.ForeignKeyField("BasicAttributeType")
    Door = fields.ForeignKeyField("Door")


class AttributeTypeDoor(BaseModel):
    """
    Allowed key types for door.
    """

    attribute_type = fields.ForeignKeyField("AttributeType")
    door = fields.ForeignKeyField("Door")
    default_params = fields.JSONField()

    def is_open(self, value):
        # TODO
        raise NotImplementedError
