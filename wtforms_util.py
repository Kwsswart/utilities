class OptionalIf(Optional):
    """ Custom Validator, making a field optional if another field has a desired value """

    def __init__(self, other_field_name, *args, **kwargs):
        self.other_field_name = other_field_name
        super(OptionalIf, self).__init__(*args, **kwargs)

    def __call__(self, form, field):
        """ Check if other field has data allow """
        
        other_field = form._fields.get(self.other_field_name)
        if other_field is None:
            raise Exception('no field named "%s" in form' % self.other_field_name)
        if other_field.data == 'No':
            super(OptionalIf, self).__call__(form, field)
