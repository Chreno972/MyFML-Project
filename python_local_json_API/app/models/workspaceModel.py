class Workspace:
    """
    La classe workspace, représente les informations définissant un workspace
    """

    def __init__(self, category, technologies, path, ws, pathname=None, state=None):
        self.category = category
        self.technologies = technologies
        self.path = path
        self.ws = ws
        self.pathname = pathname
        self.state = state

    def record_workspace_path(self, database_table):
        database_table.insert(
            {
                "Projet": self.pathname,
                "Categorie": self.category,
                "Technologies": self.technologies,
                "Chemin": self.path.replace("\\", "/"),
                "Workspace_name": self.ws,
                "Etat": self.state,
            }
        )
