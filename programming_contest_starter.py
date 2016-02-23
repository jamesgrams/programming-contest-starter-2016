""" 
The following is helper code for making a text-based game.

The game is essentially made up of events. Each event contains a title,
a short description, and a dictionary named events_from_here. The events_from_here
dictionary has letters on the keyboard for keys and other event objects for values.

When an event is displayed, the event's title and description is displayed.
Additonally, each event that is possible to go to from that event (i.e. the
events in the options events_from_here)'s title and keyboard character is displayed
(Thus, suprizes should be in the description rather than the title!).
The user will press a key on the keyboard corresponding to one of the events in the
dictionary and then press ENTER, and that event will then be displayed.

Feel free to edit this class to make your game more advanced! (e.g. Having an inventory system)

Original author: James Grams, 2016
"""

import os

# Class for an Event
class Event:
	# Constructor
	# @param	title		The title text for the event
	# @param	description	The description of the event
	def __init__(self, title, description):
		self.title = title;
		self.description = description
		self.events_from_here = {};

	# Add an event that can be reached from this event
	# @param	key		The key the user entered to go to an event (will be converted to capital)
	# @param	event	The event the user will go to upon entering the key
	def add_sub_event(self, key, event):
		self.events_from_here[key.upper()] = event

	# Switch to the event the user selects
	# This function will print "Invalid option" and call display
	# if an invalid input is entered.
	# @param	key		The key the user has selected
	def go_to_event(self, key):
		if not key in self.events_from_here:
			print "Invalid option."
			print
			self.display();
		else:
			print
			self.events_from_here[key].display()

	# Display the event, the other events that can be accessed from this event
	# and get the user input about what they would like to do next
	def display(self):
		if os.name == "posix":
			os.system("clear")
		else:		
			os.system("cls")
		print self.title
		print self.description
		print
		print "Options"
		for key in self.events_from_here:
			print key + ": " + self.events_from_here[key].title
		print "Q: Quit"
		print
		key = raw_input("What do you want to do? ")
		if key.upper() == "Q":
			return
		self.go_to_event(key.upper());

# The following is an example of how one might use the event class above to
# create a text-based game
root = Event("Play Dungeon Explorer", "Welcome to Dungeon Explorer! You must find the treasure!")
root_option_a = Event("Walk down the hallway", "You walk down the hallway and encounter a dragon!")
root_a_option_a = Event("Fight the dragon", "The dragon overpowers you! You lose.")
root_a_option_b = Event("Befriend the dragon", "The friendly dragon leads you to the treasure! You win!")
root_option_b = Event("Go home", "You have chickened out! You lose.")

root.add_sub_event("A", root_option_a)
root_option_a.add_sub_event("A", root_a_option_a)
root_a_option_a.add_sub_event("A", root)
root_option_a.add_sub_event("B", root_a_option_b)
root_a_option_b.add_sub_event("A", root)
root.add_sub_event("B", root_option_b)
root_option_b.add_sub_event("A", root)

print
root.display()

		
