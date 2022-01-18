from typing import Optional, Union
from tortoise.exceptions import FieldError
from tortoise.fields import JSONField, TextField


class I18NField(JSONField):
    pass


class CodeField(TextField):
    pass
