from tortoise import fields
from common.model import BaseModel


class Rule(BaseModel):
    """
    Rule detail.
    """

    name = fields.CharField(max_length=255)
    desc = fields.TextField()
    tags = fields.JSONField()
    on_attributes = fields.ManyToManyField("Attribute")


class RuleDoorForAttribute(BaseModel):
    """
    Choose door for attributes.
    """

    rule = fields.ForeignKeyField("Rule")
    attribute = fields.ForeignKeyField("Attribute")
    door = fields.ForeignKeyField("Door")
    parent = fields.ForeignKeyField("RuleDoorForAttribute")
    params = fields.JSONField()


class RuleFilterForAttribute(BaseModel):
    """
    Choose filter for attributes.
    """

    rule = fields.ForeignKeyField("Rule")
    attribute = fields.ForeignKeyField("Attribute")
    filter = fields.ForeignKeyField("Filter")
    parent = fields.ForeignKeyField("RuleFilterForAttribute")
    params = fields.JSONField()
