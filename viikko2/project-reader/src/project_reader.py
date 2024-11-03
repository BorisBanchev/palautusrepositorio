from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        parsed_toml = toml.loads(content)
        information = parsed_toml["tool"]["poetry"]
        name = information["name"]
        description = information["description"]
        license = information["license"]
        authors = information["authors"]
        dependencies = list(information["dependencies"])
        devdependencies = list(information["group"]["dev"]["dependencies"])
                               
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        
        return Project(name, description, license, authors, dependencies, devdependencies)
