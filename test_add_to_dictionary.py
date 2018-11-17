from api import add_to_dictionary

goodgoods = {'Burger': 8.7,
             'Ramen': 5.8
             }


def test_add_to_dictionary():
    """
    This test checks if the given key-value pair has been added to a dictionary.
    """
    dictionary = add_to_dictionary(goodgoods, 'Sushi', 9.0)
    assert goodgoods['Sushi'] == 9.0
