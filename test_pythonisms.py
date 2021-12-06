from pythonisms import *

def test_print_list_items():
    expected = "[ {apple}, {orange}, {banana}, {cherry},  ]"
    fruits = ["apple","orange","banana","cherry"]
    actual = print_list_items(fruits)
    assert actual == expected

def test_make_fruit_plural():
    fruits = ["apple","orange","banana","cherry"]
    expected = ["apple's", "orange's", "banana's", "cherry's"]
    actual = make_fruit_plural(fruits)
    assert actual == expected

def test_convert_list_to_dic():
    fruits = ["apple","orange","banana","cherry"]
    expected = ('apple', 'orange', 'banana', 'cherry')
    actual = convert_list_to_dic(fruits)
    assert actual == expected

def test_add_meals():
    restaurant = Restaurant(["Mansaf","Kofta"])
    expected = ["Mansaf","Kofta"]
    actual = restaurant.meals
    assert actual == expected

def test_meal_exist():
    restaurant = Restaurant(["Mansaf","Kofta"])
    expected = True
    actual = restaurant.__bool__("Kofta")
    assert actual == expected

def test_meal_not_exist():
    restaurant = Restaurant(["Mansaf","Kofta"])
    expected = False
    actual = restaurant.__bool__("Maqloba")
    assert actual == expected
