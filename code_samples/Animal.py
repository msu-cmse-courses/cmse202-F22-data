import datetime


class Animal(object):
    """
        This is an Animal class, used to store information about animals in the Zoo. Or for characters in the Madagascar movies.
    """

    def __init__(self, kind, name, to_zoo='', area=100, staff=1):
        """ Initialize the Animal object.
        Inputs are
        kind : the type of animal (string)
        name : the nickname for the animal (string)
        to_zoo : the date the animal came to the zoo (in 'yyyy-mm-dd' format)
        """
        self.kind = kind
        self.name = name
        self.brought_to_zoo = to_zoo
        self.required_area = area  # required area [m2]
        # required number of staff members per animal; can be fraction, e.g. 0.2 means one zookeeper can take care of
        # 5 animals
        self.required_staff = staff

    def set_name(self, name):
        """ Set animal's name. """
        self.name = name

    def set_kind(self, kind):
        """ Set animal's kind. """
        self.kind = kind

    def set_arrive_to_zoo(self, to_zoo):
        """ Set animal's date delivered to the Zoo. """
        self.brought_to_zoo = to_zoo

    def set_required_area(self, area):
        """ Set average required area by single a animal. """
        self.required_area = area

    def set_number_keepers(self, num):
        """ Set the number of Zoo keepers required by a single animal. """
        self.required_staff = num

    def get_name(self):
        """ Return animal's nick name. """
        return self.name

    def get_kind(self):
        """ Return animal's kind. """
        return self.kind

    def get_arrive_to_zoo(self):
        """ Return animal's date delivered to the Zoo. """
        return self.brought_to_zoo

    def get_required_area(self):
        """ Return average required area by single animal. """
        return self.required_area

    def get_number_keepers(self):
        """ Return the number of Zoo keepers required by a single animal. """
        return self.required_staff

    def days_in_zoo(self):
        """
            Return the number of days the animal is in the Zoo.
        """
        today = datetime.date.today()
        # convert string 'YYYY-MM-DD' into three strings, that are used do create a date object when animal arrived
        # to the zoo
        y, m, d = self.brought_to_zoo.split("-")
        brought_in = datetime.date(int(y), int(m), int(d))

        days_in_zoo = today - brought_in
        return days_in_zoo.days
