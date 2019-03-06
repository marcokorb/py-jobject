"""
Error definitions.
"""

class UndefinedTypeError(Exception):
    """
    Exception thrown when a type is not defined.
    """

    def __init__(self, type_):
        msg = "Type '%s' is not defined." % type_.__name__
        super().__init__(msg)
