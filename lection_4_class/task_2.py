class Markets:
    def __init__(self, name, area, categories):
        self.name = name
        self.area = area
        self.categories = categories
    def __str__(self):
        return f"Supermarket {self.name} has an area of {self.area} meters \
squared and has the following categories: {', '.join(self.categories)}"
