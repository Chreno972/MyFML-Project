class View(object):
    """
    classdocs
    """

    def __init__(self, controller):
        """
        constructor
        """
        self.controller = controller

    def make_choice(self):
        print()
        print("MENU PRINCIPAL")
        print("Que souhaitez-vous faire ?\n")

        print("0. Accéder à un workspace")
        print("1. Créer et enregistrer un workspace")
        print("2. Enregistrer un workspace existant dans la BDD")
        print("3. Mettre à jour un workspace")
        print("4. Effacer un workspace")
        print("5. Exporter la base de données en CSV")
        print("6. Sortir de l'application")

        choice = input("Faites votre choix :\n")
        return choice

    def access_your_workspace(self):
        """Accéder au un workspace présent dans la database

        Returns:
            [string]: [un nombre format str converti en int à la récupération]
        """
        self.controller.display_informations()
        choix_workspace = input("\nQuel est l'id de votre workspace :\n")
        return choix_workspace

    def record_existant_workspace(self):
        """[Enregistrer un nouveau workspace dans la database]

        Returns:
            [list]: [liste des informations du nouveau workspace pour la database]
        """
        category = input("Catégorie : Projet Perso, Projet Pro ou Apprentissage ?\n")
        technologies = input("Quelles technologies sont utilisées ?\n")
        path = input("Quel est le chemin du workspace ?\n")
        ws = input("Quel est le nom du workspace ?\n")
        pathname = input("Quel est le nom du projet ?\n")
        state = input("Quel est l'état d'avancement du projet ?\n")
        return [
            category,
            technologies,
            path,
            ws,
            pathname,
            state,
        ]

    def create_record_workspace(self):
        category = input("Catégorie : Projet Perso, Projet Pro ou Apprentissage ?\n")
        technologies = input("Quelles technologies sont utilisées ?\n")
        path = input("tapez 'apprentissage' ou 'projet'\n")
        ws = input("Quel est le nom du workspace ?\n")
        pathname = input("Quel est le nom du projet ?\n")
        state = input("Quel est l'état d'avancement du projet ?\n")
        return [
            category,
            technologies,
            path,
            ws,
            pathname,
            state,
        ]

    def update_workspace(self):
        self.controller.display_informations()
        id_workspace = input("Quel est l'id du workspace à mettre à jour ?\n")
        index_actuel = input("Projet, Technologies, Etat, Chemin, Workspace_name ?\n")
        nouvel_index = input("Quelle sera la nouvelle valeur de l'index ?\n")
        return [int(id_workspace), index_actuel, nouvel_index]

    def delete_workspace(self):
        """[Effacer un workspace]

        Returns:
            [string]: [L'id du workspace converti en int à la récupération]
        """
        self.controller.display_informations()
        ws_id = input("Quelle est l'id du workspace ?\n")
        return ws_id
