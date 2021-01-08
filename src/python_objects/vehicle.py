class Vehicle:
    """
    Vehicle is a type that describes a machine that helps us travel.
    """

    default_tire = 'tire'

    def __init__(self, engine, tires):
        """
        Customizes the initialization of the object.
        """
        self.engine = engine
        self.tires = tires

    @classmethod
    def bicycle(cls, tires=None):
        """
        """
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        """
        Prints out the description of the vehicle.
        """
        print(
            f'A vehicle with an {self.engine} engine, '
            f'and {self.tires} tires'
        )
