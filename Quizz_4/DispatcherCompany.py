from Package import Package

class DistpatcherCompany():
    def __init__(self, id, name, packages):
        self.id = id
        self.name = name
        self.packages = packages

    def show_attr(self):
        print(f" Id: {self.id}")
        print(f" Name: {self.name}")
        print(f" Packages: ")
        for package in self.packages:
            print(f"\t {package.id} - {package.address} ({package.delivered})")
