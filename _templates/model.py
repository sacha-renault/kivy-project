from kivy.event import EventDispatcher
from kivy.properties import (
    StringProperty, NumericProperty, BooleanProperty,
    ListProperty, DictProperty, ObjectProperty,
    OptionProperty
)

class TemplateModel(EventDispatcher): 
    string_property = StringProperty("Default String")
    # chose which property to use
    # string_property = StringProperty("Default String")
    # numeric_property = NumericProperty(0)
    # boolean_property = BooleanProperty(False)
    # list_property = ListProperty([1, 2, 3])
    # dict_property = DictProperty({'key': 'value'})
    # object_property = ObjectProperty(None)
    # float_property = FloatProperty(0.0)
    # int_property = IntProperty(0)
    # option_property = OptionProperty('auto', options=['auto', 'manual'])
