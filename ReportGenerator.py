
def border(func):
    def show(self):
        print("*" * 40)
        func(self)
        print("*" * 40)
    return show


class Report:
    title = "Simple Report"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.template = "{title}\nName: {name}\nMarks: {marks}"

   
    @classmethod
    def set_title(cls, new_title):
        cls.title = new_title

    def set_template(self, text):
        self.template = text

    def __str__(self):
        return self.template.format(
            title=Report.title,
            name=self.name,
            marks=self.marks
        )

    
    @border
    def print_report(self):
        print(self)



r1 = Report("Rahul", 85)

print("Default Report:")
r1.print_report()


Report.set_title("Student Result Report")

new_template = """
{title}
----------------
Student : {name}
Score   : {marks}
Status  : Pass
"""

r1.set_template(new_template)

print("\nUpdated Report:")
r1.print_report()