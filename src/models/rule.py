from tortoise import fields
from common.model import BaseModel


class Rule(BaseModel):
    """
    Rule detail.
    """

    name = fields.CharField(max_length=255)
    desc = fields.TextField()
    tags = fields.JSONField()
    on_attributes = fields.ManyToManyField("models.Attribute")


class RuleDoorForAttribute(BaseModel):
    """
    Choose door for attributes.
    """

    rule = fields.ForeignKeyField("models.Rule")
    attribute = fields.ForeignKeyField("models.Attribute")
    door = fields.ForeignKeyField("models.Door")
    parent = fields.ForeignKeyField("models.RuleDoorForAttribute", null=True)
    params = fields.JSONField()


class RuleFilterForAttribute(BaseModel):
    """
    Choose filter for attributes.
    """

    rule = fields.ForeignKeyField("models.Rule")
    attribute = fields.ForeignKeyField("models.Attribute")
    filter = fields.ForeignKeyField("models.Filter")
    parent = fields.ForeignKeyField("models.RuleFilterForAttribute")
    params = fields.JSONField()
