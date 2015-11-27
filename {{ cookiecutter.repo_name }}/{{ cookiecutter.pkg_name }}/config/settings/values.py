from configurations import values
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class AdminsValue(values.SingleNestedTupleValue):
    """A ``SingleNestedTupleValue`` subclass to be used for the ADMINS and MANAGERS settings.

    Two validators are executed for each tuple:

        1. The exact length of each tuple must be two.
        2. The second element of each tuple must be a valid email address.
    """

    def __init__(self, *args, **kwargs):
        """Configure the value object and validate the default if present."""
        super(AdminsValue, self).__init__(*args, **kwargs)
        if self.default:
            self.validate(self.default)

    def validate_length(self, value):
        """Validate that each tuple contains only two values."""
        if len(value) != 2:
            raise ValueError('Each ADMINS tuple must have exact two values')

    def validate_email(self, value):
        """Validate the email address."""
        try:
            validate_email(value)
        except ValidationError:
            raise ValueError('Cannot interpret email value {0!r}'.format(value))

    def validate(self, value):
        """Validate all tuples."""
        for item in value:
            self.validate_length(item)
            self.validate_email(item[1])

    def to_python(self, value):
        """Convert environment variable string and validate the python objects."""
        value = super(AdminsValue, self).to_python(value)
        self.validate(value)
        return value
