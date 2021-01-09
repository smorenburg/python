class Vehicle:
    """
    Vehicle is a type that describes a machine that helps us travel.
    """

    def __init__(self, distance_traveled=0, unit='kilometers', **kwargs):
        self.distance_traveled = distance_traveled
        self.unit = unit

    # @classmethod
    # def bicycle(cls, tires=None):
    #     """
    #     """
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    def description(self):
        return(
            f'A {str(self.__class__.__name__).lower()} that has traveled '
            f'{self.distance_traveled} {self.unit}'
        )
