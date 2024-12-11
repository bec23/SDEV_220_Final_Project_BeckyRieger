# Becky Rieger
#Program for Livingston County humane society. Enter animal, adopter, adoption record, and have function to approve adopter

#add classes: Animal, Adopter, Adoption_Record, Adoption_Center
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class Adopter:
    def __init__(self, name, contact_info, approved=False):
        self.name = name
        self.contact_info = contact_info
        self.approved = approved

class Adoption_Record:
    def __init__(self, animal, adopter, date):
        self.animal = animal
        self.adopter = adopter
        self.date = date

class Adoption_Center:
    def __init__(self):
        self.animals = []
        self.adopters = []
        self.adoption_records = []

#add animals, adopters, adoption records, and approve adopters
    def add_animal(self, animal):
        self.animals.append(animal)

    def add_adopter(self, adopter):
        self.adopters.append(adopter)

    def approve_adopter(self, adopter_name):
        adopter = next((a for a in self.adopters if a.name == adopter_name), None)
        if adopter:
            adopter.approved = True
            return f"{adopter.name} has been approved."
        return "Adopter not found."

#record of the adoption
    def record_adoption(self, animal_name, adopter_name, date):
        animal = next((a for a in self.animals if a.name == animal_name), None)
        adopter = next((a for a in self.adopters if a.name == adopter_name), None)
        if animal and adopter and adopter.approved:
            self.animals.remove(animal)
            record = Adoption_Record(animal, adopter, date)
            self.adoption_records.append(record)
            return f"{adopter.name} has adopted {animal.name} on {date}."
        return "Adoption failed. Animal or adopter not found, or adopter not approved."

#GUI
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#creating the sections of app
class Humane_Society_App:
    def __init__(self, root):
        self.root = root
        self.root.title("Livingston County Humane Society")
        self.center = Adoption_Center()

        self.create_widgets()

    def create_widgets(self):
        # animal section
        tk.Label(self.root, text="Animal Name:").grid(row=0, column=0)
        self.animal_name_entry = tk.Entry(self.root)
        self.animal_name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Species:").grid(row=1, column=0)
        self.species_entry = tk.Entry(self.root)
        self.species_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Age:").grid(row=2, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1)

        tk.Button(self.root, text="Add Animal", command=self.add_animal).grid(row=3, column=0, columnspan=2)

        # adopter section
        tk.Label(self.root, text="Adopter Name:").grid(row=4, column=0)
        self.adopter_name_entry = tk.Entry(self.root)
        self.adopter_name_entry.grid(row=4, column=1)

        tk.Label(self.root, text="Contact Info:").grid(row=5, column=0)
        self.contact_info_entry = tk.Entry(self.root)
        self.contact_info_entry.grid(row=5, column=1)

        tk.Button(self.root, text="Add Adopter", command=self.add_adopter).grid(row=6, column=0, columnspan=2)

        tk.Label(self.root, text="Enter the adopter full name to approve adopter:").grid(row=7, column=0)
        self.approve_adopter_entry = tk.Entry(self.root)
        self.approve_adopter_entry.grid(row=7, column=1)

        tk.Button(self.root, text="Approve", command=self.approve_adopter).grid(row=8, column=0, columnspan=2)

        # adoption section
        tk.Label(self.root, text="Animal to Adopt:").grid(row=9, column=0)
        self.adopt_animal_entry = tk.Entry(self.root)
        self.adopt_animal_entry.grid(row=9, column=1)

        tk.Label(self.root, text="Adopter Name:").grid(row=10, column=0)
        self.adopt_adopter_entry = tk.Entry(self.root)
        self.adopt_adopter_entry.grid(row=10, column=1)

        tk.Label(self.root, text="Adoption Date (YYYY-MM-DD):").grid(row=11, column=0)
        self.adoption_date_entry = tk.Entry(self.root)
        self.adoption_date_entry.grid(row=11, column=1)

        tk.Button(self.root, text="Adopt Animal", command=self.adopt_animal).grid(row=12, column=0, columnspan=2)
        
        #view buttons
        tk.Button(self.root, text="View Animals", command=self.view_animals).grid(row=13, column=0, columnspan=2) 
        tk.Button(self.root, text="View Adopters", command=self.view_adopters).grid(row=14, column=0, columnspan=2) 
        tk.Button(self.root, text="View Adoptions", command=self.view_adoptions).grid(row=15, column=0, columnspan=2)

    def add_animal(self):
        name = self.animal_name_entry.get()
        species = self.species_entry.get()
        age = self.age_entry.get()
        animal = Animal(name, species, age)
        self.center.add_animal(animal)
        messagebox.showinfo("Success", f"Added {name} the {species}.")

    def add_adopter(self):
        name = self.adopter_name_entry.get()
        contact_info = self.contact_info_entry.get()
        adopter = Adopter(name, contact_info)
        self.center.add_adopter(adopter)
        messagebox.showinfo("Success", f"Added adopter {name}.")

    def approve_adopter(self):
        adopter_name = self.approve_adopter_entry.get()
        result = self.center.approve_adopter(adopter_name)
        messagebox.showinfo("Approval Result", result)

    def adopt_animal(self):
        animal_name = self.adopt_animal_entry.get()
        adopter_name = self.adopt_adopter_entry.get()
        adoption_date = self.adoption_date_entry.get()
        try:
            datetime.strptime(adoption_date, "%Y-%m-%d")
            result = self.center.record_adoption(animal_name, adopter_name, adoption_date)
            messagebox.showinfo("Adoption Result", result)
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")

    #views
    def view_animals(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Animals")
        for i, animal in enumerate(self.center.animals):
            tk.Label(view_window, text=f"{animal.name}, {animal.species}, {animal.age} years old").grid(row=i, column=0)
            
    def view_adopters(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Adopters")
        for i, adopter in enumerate(self.center.adopters):
            status = "Approved" if adopter.approved else "Not Approved"
            tk.Label(view_window, text=f"{adopter.name}, {adopter.contact_info}, {status}").grid(row=i, colum=0)
    
    def view_adoptions(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Adoptions")
        for i, record in enumerate(self.center.adoption_records):
            tk.Label(view_window, text=f"{record.adopter.name} adopted {record.animal.name} on {record.date}").grid(row=i, column=0)
                    
if __name__ == "__main__":
    root = tk.Tk()
    app = Humane_Society_App(root)
    root.mainloop()
