""" Imports de bibliothèques natives Python """
from time import sleep as sl
from os import mkdir as mkd
from os import rename as rnm
from os import rmdir as rmd
from os import system as sys
from os import chdir as chd
import webbrowser
import csv

""" Imports de modules crées """
from python_local_json_API.app.models.workspaceModel import Workspace
from python_local_json_API.app.views.mainView import View

""" Import de bibliothèques installées """
from tinydb import TinyDB, Query
import numpy as np
import pandas as pd


db = TinyDB(
    "python_local_json_API/app/data/workspaces.json",
    sort_keys=False,
    indent=4,
    separators=(",", ": "),
)
workspaces_table = db.table("workspaces")
User = Query()


class Controller(Workspace):
    """
    docstring
    """

    """ les chemins principaux dans lesquels on crée les workspaces """

    LEARNING_PATH = "../Apprentissages/learning_projects"
    PROJECTS_PATH = "../Projets/Projets"

    def __init__(self):
        self.view = View(self)

    """ MAIN METHOD """

    def main_choice(self):
        result = self.view.make_choice()
        if result == "0":
            self.access_a_workspace()
        elif result == "1":
            self.create_record_a_workspace()
        elif result == "2":
            self.record_workspaces()
        elif result == "3":
            self.update_workspace()
        elif result == "4":
            self.remove_workspace()
        elif result == "5":
            self.export_json_to_csv()
        elif result == "6":
            sys("exit()")
        else:
            print()
            print("Recommencez et entrez uniquement un nombre entier répertorié")
            print()
            sl(2)
            sys("cls")
            Controller().main_choice()

    """ METHODS TO INCORPORATE """

    def display_informations(self):
        """
        Affichage d'informations des workspaces
        [data.append...]: récupère et place les mêmes informations de chaque workspace d'une façon précise
        dans la liste data
        [indexes]: va recevoir l'index de chaque ligne du tableau pandas
        """
        data = []
        d = []
        indexes = []
        for i in range(len(workspaces_table)):
            i = "WORKSPACE"
            indexes.append(i)
        for item in workspaces_table:
            data.append(
                [
                    item.doc_id,
                    item["Etat"],
                    item["Projet"],
                    item["Categorie"],
                    item["Technologies"],
                ]
            )
        """
        [data_numpy]: crée un tableau numpy
        [players_list]: transforme le tableau numpy en un Dataframe avec Pandas
        [indexes]: définit le nom ou l'id par défaut du chaque ligne du tableau
        [columns]: définit l'entête de chaque colonne d'informations
        [by=["ETAT"]]: range les lignes par ordre alphabétique ou numérique 
        selon les infos que contient la colonne ETAT
        [ascending=True]: range du plus petit au plus grand
        """
        data_numpy = np.array(data, dtype=object)
        players_list = pd.DataFrame(
            data_numpy,
            index=indexes,
            columns=[
                "ID",
                "ETAT",
                "PROJET",
                "CATEGORIE",
                "TECHNOLOGIES",
            ],
        )
        print()
        print(players_list.sort_values(by=["ETAT"], ascending=True))
        print()

    def access_a_workspace(self):
        """
        Accéder à un workspace et commencer à travailler
        choosen_workspace_title[str]: reçoit le titre du workspace depuis une fonction de la classe View
        item.doc_id[int]: correspond à l'id d'un workspace par rapport à la boucle for qui parcours
        la base de donnée des workspaces
        chd[exec]: se place dans le dossier d'un path
        sys[exec]: ouvre le workspace dans vscode
        """
        choosen_workspace_title = self.view.access_your_workspace()
        for item in workspaces_table:
            if choosen_workspace_title == str(item.doc_id):
                chd("{}".format(item["Chemin"]))
                sys("code {}".format(item["Workspace_name"]))
        self.main_choice()

    def create_record_a_workspace(self):
        result = self.view.create_record_workspace()
        if result[2] == "apprentissage":
            result[2] = self.LEARNING_PATH
            self.lets_record(result)
        elif result[2] == "projet":
            result[2] = self.PROJECTS_PATH
            self.lets_record(result)
        else:
            result[2] = result[2].replace("\\", "/")
            self.lets_record(result)

    def lets_record(self, rec):
        the_record = Workspace(rec[0], rec[1], rec[2], rec[3], rec[4], rec[5])
        the_record.record_workspace_path(workspaces_table)
        print("BDD à jour patientez pendant la création des dossiers")
        sl(3)
        chd(rec[2])
        mkd(rec[3])

    # ! permet d'enregistrer un workspace dans la base de données (fonction première)
    def record_workspaces(self):
        """[summary]"""
        result = self.view.record_existant_workspace()
        the_record = Workspace(
            result[0], result[1], result[2], result[3], result[4], result[5]
        )
        the_record.record_workspace_path(workspaces_table)
        print("Parfait votre workspace à été enregistrée")
        sl(2)
        Controller().main_choice()

    # ! Permet de mettre à jour le chemin vers le workspace (fonction secondaire)
    def update_workspace(self):
        """[summary]"""
        first_step = self.view.update_workspace()
        for truc in workspaces_table:
            if truc.doc_id == first_step[0]:
                if first_step[1] == "Workspace_name":
                    chd(truc["Chemin"])
                    rnm(truc["Workspace_name"], first_step[2])
        sl(2)
        workspaces_table.update({first_step[1]: first_step[2]}, doc_ids=[first_step[0]])
        print("Parait, le workspace à été mis à jour")
        sl(2)
        Controller().main_choice()

    # ! Permet de supprimer un workspace depuis son nom (fonction secondaire)
    def remove_workspace(self):
        """[summary]"""
        the_id = self.view.delete_workspace()
        for truc in workspaces_table:
            if truc.doc_id == int(the_id):
                chd(truc["Chemin"])
                rmd(truc["Workspace_name"])

        workspaces_table.remove(doc_ids=[int(the_id)])
        print("Parait, le workspace à été supprimé")
        sl(2)
        Controller().main_choice()

    # ! Permet d'exporter la base de données JSON sous format csv (fonction secondaire)
    def export_json_to_csv(self):
        """ """
        cols = ["id", "Nom du Projet", "Technologies"]
        data = []
        for item in workspaces_table:
            data.append(
                {
                    "id": item.doc_id,
                    "Nom du Projet": item["Projet"],
                    "Technologies": item["Technologies"],
                }
            )
        with open("workspaces.csv", "w") as f:
            wr = csv.DictWriter(f, fieldnames=cols, delimiter=";")
            wr.writeheader()
            wr.writerows(data)


# """ THE TRIGGER """
# if __name__ == "__main__":
#     Controller().main_choice()
