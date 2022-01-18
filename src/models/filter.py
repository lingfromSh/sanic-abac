from tortoise import fields
from common.fields import CodeField
from common.model import BaseModel


class Filter(BaseModel):
    """
    Filters for filtering attributes.
    """
    name = fields.CharField(max_length=255)
    desc = fields.TextField()
    py_code = CodeField()

    def filter_value(self, value):
        # TODO
        raise NotImplementedError

    @property
    def expected_params(self):
        # TODO
        raise NotImplementedError


class BasicAttributeTypeFilter(BaseModel):
    """
    Allowed filters for basic attribute type.
    """

    basic_attribute_type = fields.ForeignKeyField("BasicAttributeType")
    filter = fields.ForeignKeyField("Filter")
    default_params = fields.JSONField()

    def filter_value(self, value):
        # TODO
        raise NotImplementedError


class AttributeTypeFilter(BaseModel):
    """
    Attribute type's bound filters.
    """

    attribute_type = fields.ForeignKeyField("AttributeType")
    filter = fields.ForeignKeyField("Filter")
    default_params = fields.JSONField()

    def filter_value(self, value):
        # TODO
        raise NotImplementedError
