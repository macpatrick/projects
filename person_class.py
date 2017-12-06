from PIL import Image, ImageTk
import datetime
import tkinter as tk

window = tk.Tk()
window.geometry("400x600")
window.title("Age Calculator App")

customer_label = tk.Label(text="YourName")
customer_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=3)

Day_label = tk.Label(text="Day")
Day_label.grid(column=0, row=4)


customer_entry = tk.Entry()
customer_entry.grid(column=1, row=1)

year_entry = tk.Entry()
year_entry.grid(column=1, row=2)

month_entry = tk.Entry()
month_entry.grid(column=1, row=3)

day_entry = tk.Entry()
day_entry.grid(column=1, row=4)


def calculate_age():
	print(year_entry.get())
	print(month_entry.get())
	print(day_entry.get())
	person = Person('You', datetime.date(int(year_entry.get()), 
										      int(month_entry.get()), 
										      int(day_entry.get())))
	
	print(person.age())	
	text_answer = tk.Text(master=window, height=5, width=20)
	text_answer.grid(column=1, row=7)
	answer_text = "{name} are {age} years old".format(name=person.name, age=person.age())
	text_answer.insert(tk.END, answer_text)


calculate_button = tk.Button(text="Calcutate Now", command=calculate_age)
calculate_button.grid(column=1, row=5)


class Person:

	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate

	def age(self):
		today = datetime.date.today()
		age = today.year - self.birthdate.year
		return age	

image = Image.open('ales-krivec-2859.jpg')
image.thumbnail((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1, row=0)




#person = person('Patrick', datetime.date(1958, 3, 15))

#print(Patrick.name)
#print(Patrick.birthdate)
#print(Patrick.age())

window.mainloop()