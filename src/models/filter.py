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

    basic_attribute_type = fields.ForeignKeyField("models.BasicAttributeType")
    filter = fields.ForeignKeyField("models.Filter")
    default_params = fields.JSONField()

    def filter_value(self, value):
        # TODO
        raise NotImplementedError


class AttributeTypeFilter(BaseModel):
    """
    Attribute type's bound filters.
    """

    attribute_type = fields.ForeignKeyField("models.AttributeType")
    filter = fields.ForeignKeyField("models.Filter")
    default_params = fields.JSONField()

    def filter_value(self, value):
        # TODO
        raise NotImplementedError
