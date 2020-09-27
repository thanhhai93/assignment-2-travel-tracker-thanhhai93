"""
Name: NGUYEN THANH HAI
Date: 27/09/2020
Brief Project Description: An application for user
GitHub URL:https://github.com/JCUS-CP1404/assignment-2-travel-tracker-thanhhai93
"""
# Create your main program in this file, using the TravelTrackerApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.uix.button import Button
from place import Place
from placecollection import PlaceCollection

OPTIONS = {'Unvisited' : 4, 'Visited' : 3, 'Priority' : 2, 'Country' : 1, 'City' : 0}
VISITED_COLOR = (1.1, 1.5, 1.5, 1)
UNVISITED_COLOR = (2, 1, 1, 1.5)


class TravelTracker (App, Place) :
    """ The main class for the GUI of the place app"""
    current_sort = StringProperty ( )
    sort_options = ListProperty ( )
    category = StringProperty ( )

    def build(self) :
        """ Build app with the help of app.kv file"""
        self.title = "Travel Tracker"
        # load app.kv
        self.root = Builder.load_file ('app.kv')
        self.sort_options = sorted (OPTIONS.keys ( ), reverse=True)
        self.current_sort = self.sort_options [ 0 ]
        self.root.ids.status.text = "Welcome to Travel Tracker 2.0"

        return self.root




    def sorted(self, sort_choice) :
        """sorting based on users choice"""
        self.root.ids.entries_box.clear_widgets ( )
        Place.sort (self, OPTIONS [ sort_choice ])
        self.show_place ( )
        self.root.ids.visit.text = "Place to visist: " + str (Place.visit_place (self))

    def on_stop(self):
        """ Save changes to the csv file after closing the program"""
        Place.save(self)


    def show_place(self) :
        """displaying the place from the data list"""
        id_count = 0
        for a in self.sorted_data:
            id_count = id_count + 1
            if a [ 3 ] == "n" :
                entries_box = Button (
                    id=str (id_count),
                    text="{0} in {1}, priority {2}".format (a [ 0 ], a [ 1 ], a [ 2 ]),
                    background_color=UNVISITED_COLOR,
                    on_press=lambda x : Place.mark_place (self, x.id))
                self.root.ids.entries_box.add_widget (entries_box)
            else :
                entries_box = Button (
                    id=str (id_count),
                    text="{0} in {1}, priority {2} (visited)".format (a [ 0 ], a [ 1 ], a [ 2 ]),
                    background_color=VISITED_COLOR,
                    on_press=lambda x : Place.mark_place (self, x.id))
                self.root.ids.entries_box.add_widget (entries_box)





    def clear_text(self) :
        """Clear the input when 'clear' button"""
        self.root.ids.city_name.text = ""
        self.root.ids.country_name.text = ""
        self.root.ids.priority_num.text = ""
        self.root.ids.status.text = ""


    def add_places(self) :
        """adding new places"""
        temp_list = [ ]
        name = self.root.ids.city_name.text
        country = self.root.ids.country_name.text
        try :
            priority = int (self.root.ids.priority_num.text)
            if name == "" or country == "" or priority == "" :
                self.root.ids.status.text = "All fields must be filled in."
            elif priority <= 0 :
                self.root.ids.status.text = "INVALLD number input."
            else :
                temp_list.append (name)
                temp_list.append (country)
                temp_list.append (priority)
                self.root.ids.status_text = "{} has been added.".format (name)

        except ValueError :
            self.root.ids.status_text = "Invalid input. Fill in all fields and a number is chosen for 'Priority'."
        self.root.ids.city_name.text = ""
        self.root.ids.country_name.text = ""
        self.root.ids.priority_num.text = ""


if __name__ == "__main__" :
    TravelTracker ( ).run ( )


