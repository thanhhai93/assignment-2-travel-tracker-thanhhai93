"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    print ("marking visited place")
    new_place = Place ("Malage", "Spain", 1, "n")
    print (new_place)

    # TODO: Add more tests, as appropriate, for each method
    print(new_place)
    print (new_place.check_visited())
    "check already visited this place or not "
    print(new_place.is_important())
    "add important place"


run_tests()