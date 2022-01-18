from tortoise import fields
from common.model import BaseModel


class BasicAttributeType(BaseModel):
    """
    Basic type of attribute type
    """
    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255, unique=True)
    desc = fields.TextField(null=True)


class AttributeType(BaseModel):
    """
    Type of attribute
    """

    name = fields.CharField(max_length=255)
    belong_to = fields.ForeignKeyField("AttributeType", related_name="sub_attr_types", null=True)
    type = fields.ForeignKeyField("BasicAttributeType", related_name="bound_attr_types", null=True)
    desc = fields.TextField(null=True)

    is_multiple = fields.BooleanField(default=False)

    def to_key(self, value):
        pass


class Attribute(BaseModel):
    """
    Use attribute to represent any kinds of resources.

    Example:
        attr_role = Attribute(name="role", desc="role", tags=["service-a", "rbac"])
    """

    name = fields.CharField(max_length=255)
    code = fields.CharField(max_length=255)
    parent = fields.ForeignKeyField("Attribute")
    type = fields.ForeignKeyField("AttributeType", related_name="used_in_attributes")
    desc = fields.TextField()
    tags = fields.JSONField()

    class Meta:
        unique_together = ("code", "parent")
