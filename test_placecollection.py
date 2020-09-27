from placecollection import PlaceCollection
from place import Place
import csv

def run_tests():
    """Test Collection class."""

    # Test empty Collection (defaults)
    print("Test empty Collection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.place  # an empty list is considered False

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.place_list  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new lace with values
    print("Test adding new place :")
    place_collection.add_place(Place ("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("Test sorting - Priority:")
    sorted_list = place_collection.sort_place("priority ")
    print(place_collection.format_data(sorted_list))

    # Test sorting country
    print("Test sorting - country:")
    sorted_list_2 = place_collection.sort_place("country", descending=True)
    print(place_collection.format_data(sorted_list_2))
    # test sorting name
    print("Test sorting - name:")
    sorted_list_3 = place_collection.sort_place("name", descending=False)
    print(place_collection.format_data(sorted_list_3))
 #  Test saving places (check CSV file manually to see results)
    print("Test saving places:")
    place_collection.save_changes("places.csv")

    # Add more tests, as appropriate, for each method
    print("Test count learned places:")
    print(place_collection.count_learned())
    # Test count unlearned places
    print("Test count unlearned places:")
    print(place_collection.count_unlearned())


run_tests()
