from functools import reduce
from operator import and_

from sanic.response import json
from models import Rule, BasicAttributeType, AttributeType, Attribute, Door, RuleDoorForAttribute
from tortoise.transactions import atomic


@atomic()
async def make_test_data():
    string_type = await BasicAttributeType.create(name="string", code="string", desc="Represent string type.")
    int_type = await BasicAttributeType.create(name="int", code="int", desc="Represent int type.")
    float_type = await BasicAttributeType.create(name="float", code="float", desc="Represent float type.")
    dict_type = await BasicAttributeType.create(name="dict", code="dict", desc="Represent dict type.")
    list_type = await BasicAttributeType.create(name="list", code="list", desc="Represent list type.")
    tuple_type = await BasicAttributeType.create(name="tuple", code="tuple", desc="Represent tuple type.")

    user_id_attr_type = await AttributeType.create(name="user_id", type=int_type, desc="User Id")
    user_id_attr = await Attribute.create(name="user_id", code="user_id", type=user_id_attr_type, desc="User Id",
                                          tags=[])
    media_id_attr_type = await AttributeType.create(name="media_id", type=int_type, desc="Media Id")
    media_id_attr = await Attribute.create(name="media_id", code="media_id", type=media_id_attr_type,
                                           desc="Media Id",
                                           tags=[])

    rule = await Rule.create(name="media-download-rule",
                             desc="Only allow <user: 1> to download his picture.",
                             tags=["media-microservice"])
    await rule.on_attributes.add(user_id_attr, media_id_attr)

    equal_door = await Door.create(name="Exact",
                                   desc="Return True if a equal b otherwise False.",
                                   py_code="lambda a, b: a == b")
    check = await RuleDoorForAttribute.create(rule=rule, attribute=user_id_attr, door=equal_door,
                                              params={"b": 1})
    await RuleDoorForAttribute.create(rule=rule, attribute=media_id_attr, door=equal_door, parent=check,
                                      params={"b": 2})


async def authenticate(request):
    """
    Return the request whether is allowed to execute or not.

    request.resource -> rules -> constraints -> Allowed/Denied.

    :param request: Request
    :return:
    """
    # await make_test_data()

    data = request.json
    tags = data['tags']
    # resource_type = data['resource_type']
    resource = data['resource']
    rules = Rule.filter(tags=tags, on_attributes__name__in=list(resource.keys())).distinct()

    if not rules:
        ret = True
    else:
        ret = False
        async for rule in rules:
            rule_doors = await RuleDoorForAttribute.filter(rule=rule)
            ret = reduce(and_,
                         [(await rule_door.door).should_open(resource[(await rule_door.attribute).code],
                                                             **rule_door.params)
                          for rule_door in rule_doors])
            if ret is False:
                break

    return json({"ret": ret})


async def ws_authenticate(request, ws):
    """
    Return the request whether is allowed to be executed or not.

    :param request:
    :param ws:
    :return:
    """
    print(ws)
    pass
