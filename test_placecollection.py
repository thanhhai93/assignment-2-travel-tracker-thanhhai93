"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("Test adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)
    # TODO: Add more sorting tests

    # TODO: Test saving places (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method

    # TODO: Add more sorting tests
    """Sorting tests"""
    print("Test sorting-Alphabetically:")
    place_collection.sort_Alphabetically(place_collection.places)
    print(place_collection)

    print("Test sorting by vivsited status")
    place_collection.sort_visited(place_collection.places)
    print(place_collection)

    print("Test sorting by name")
    place_collection.sort_name(place_collection.places)
    print(place_collection)

    print("Test sorting by country")
    place_collection.sort_country(place_collection.places)
    print(place_collection)

    print("Test sorting by unvisited status")
    place_collection.sort_unvisited(place_collection.places)
    print(place_collection)
    # TODO: Test saving places (check CSV file manually to see results)
    """Save file from places list that is stored in the csv file"""
    print("test saving")
    place_collection.save_file('places.csv')
    """New edited file is now saved and the csv is updated!"""
    assert place_collection.places
    # TODO: Add more tests, as appropriate, for each method
    print(place_collection.get_number_unvisited_places())


run_tests()
