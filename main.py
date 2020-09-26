"""
Name: NGUYEN THANH HAI
Date: 27/09/2020
Brief Project Description:
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-thanhhai93
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App


class TravelTrackerApp(App):
    """..."""
    pass


if __name__ == '__main__':
    TravelTrackerApp().run()

    from place import Place

    """This for importing place class"""
    from kivy.app import App

    """This for importing kivy for building the app"""
    from kivy.lang import Builder

    """This for importing kivy for building the app"""
    from kivy.uix.button import Button

    """This for importing kivy for give button"""
    from kivy.properties import StringProperty

    """This for importing kivy for spinner showing string property"""
    from kivy.properties import ListProperty

    """This for importing kivy for spinner that will display spinner like dropdown menu"""

    OPTIONS = {'Unvisited': 4, 'Visited': 3, 'Priority': 2, 'Country': 1, 'City': 0}
    """This dictionary is used for choice and sorting from user preferences"""
    VISITED_COLOR = (0.1, 0.5, 0.6, 0.1)
    """Constant value for visited color"""
    UNVISITED_COLOR = (2.0, 0.0, 0.0, 0.5)
    """Constant value for unvisited color"""


    class TravelTracker(App, Place):
        current_sort = StringProperty()
        """This variable is used for defining first that it will give string property"""
        sort_options = ListProperty()
        """This variable is used for defining first that it will resulting list property"""
        program_message = StringProperty()
        """This variable is used for displaying the welcone message"""

        def on_stop(self):
            """This method is used when users quit the app or the app stopped it will run the functions below which is saving the data"""
            Place.save(self)
            """Calling method from place class to save the data list to the data"""

        def show_place(self):
            """This method is used for displaying the place from the data list"""
            id_count = 0
            """This variable is used for defining each button ids"""
            for a in self.sorted_data:
                """loop for making  sure that all the data list is read and is already sorted"""
                id_count = id_count + 1
                """The variable will be add each loop for giving each place different ids"""
                if a[3] == "n":
                    """Conditions to check if its unvisited or visited to give different color"""
                    entries_box = Button(
                        id=str(id_count),
                        text="{0} in {1}, priority {2}".format(a[0], a[1], a[2]),
                        background_color=UNVISITED_COLOR,
                        on_press=lambda x: Place.mark_place(self, x.id))
                    self.root.ids.entries_box.add_widget(entries_box)
                else:
                    """Conditions to check if its unvisited or visited to give different color"""
                    entries_box = Button(
                        id=str(id_count),
                        text="{0} in {1}, priority {2} (visited)".format(a[0], a[1], a[2]),
                        background_color=VISITED_COLOR,
                        on_press=lambda x: Place.mark_place(self, x.id))
                    self.root.ids.entries_box.add_widget(entries_box)

        def sorted(self, sort_choice):
            """This method is used for sorting based on users choice"""
            self.root.ids.entries_box.clear_widgets()
            """To make sure the same button is created the widget will be cleared"""
            Place.sort(self, OPTIONS[sort_choice])
            """It will call Place method for sorting based on the choice in the dictionary"""
            self.show_place()
            """This method is used for showing the place based on the data in button widget form after its being cleared"""
            self.root.ids.visit.text = "Place to visist: " + str(Place.visit_place(self))
            """After it will be sorted it will show the place needed to visit"""

        def build(self):
            """This method is used for building the kivy apps"""
            self.title = "Travel Tracker"
            """This is used for showing the title of the app based which is Travel Tracker"""
            self.root = Builder.load_file('App.kv')
            """This is used for loading the template of the kivy app"""
            self.sort_options = sorted(OPTIONS.keys(), reverse=True)
            """This is used to display the dictionary of choice in reverse"""
            self.current_sort = self.sort_options[0]
            """This is used for automatically sort the default by first options sort"""
            self.root.ids.status.text = "Welcome to Travel Tracker 2.0"
            """This is used to display the welcome messge to the user"""
            return self.root
            """It will return the application in kivy template that made before"""

        def clear_text(self):
            """This method is used for clearing the text input and status bar that will be used after add place and press clear button"""
            self.root.ids.city_name.text = ""
            """Change city name text editor value or clear it"""
            self.root.ids.country_name.text = ""
            """Change country name text editor value or clear it"""
            self.root.ids.priority_num.text = ""
            """Change priority text editor value or clear it"""
            self.root.ids.status.text = ""
            """Change status name text editor value or clear it"""

        def add_places(self):
            """this method is used for adding new places and pass value from the app to place collections"""
            temp_list = []
            name = self.root.ids.city_name.text
            country = self.root.ids.country_name.text
            try:
                priority = int(self.root.ids.priority_num.text)
                if name == "" or country == "" or priority == "":
                    self.root.ids.status.text = "All fields must be filled in."
                elif priority <= 0:
                    self.root.ids.status.text = "INVALLD number input."
                else:
                    temp_list.append(name)
                    temp_list.append(country)
                    temp_list.append(priority)
                    self.root.ids.status_text = "{} has been added.".format(name)
                    """tells user they have managed to add their new location to visit"""
            except ValueError:
                """will be displayed if user enters incorrect input"""
                self.root.ids.status_text = "Invalid input. Fill in all fields and a number is chosen for 'Priority'."
            self.root.ids.city_name.text = ""
            self.root.ids.country_name.text = ""
            self.root.ids.priority_num.text = ""


    if __name__ == "__main__":
        TravelTracker().run()
        """To make sure it will run the applications by calling the class and . run() and make sure kivy is already imported"""
