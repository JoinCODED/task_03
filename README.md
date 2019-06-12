1. Setup a virtual environment.
2. Fork the repository for [Django Task 03](https://github.com/JoinCODED/task_03) in JoinCODED’s Github.
3. Clone the repository you just forked.
4. Install the packages from the requirements file.
5. In your views.py file, you'll find the following:
6. A `list view` has been partially created for you, complete it:
    * In your context dictionary, add an empty **list** with a key called "my_list".
    * Add dictionaries/objects in your empty list that contain "restaurant_name" and "food_type" as keys and give them values. Add three restaurants to your list.
    * Render the list of objects in the template provided to the view.
7. A `detail view` has been partially created for you, complete it:
    * In your `context` dictionary, add an empty **dictionary/object** with a key called "my_object"
    * The object must have a `restaurant_name` and `food_type`. Add your favorite restaurant.
    * Render the object in the template provided to the view.
8. The URLs for these views have already been provided for you. You do not need to create them.
9. Pass the tests (python manage.py test).
10. Push your code.
