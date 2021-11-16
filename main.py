import os
from python_local_json_API.app.controllers.controller import Controller


def main():
    if os.path.exists("./python_local_json_API/app/data/workspaces.json"):
        # Controller().auto_erase_non_existing_folders()
        Controller().auto_search_and_record_new_folders()
    else:
        pass
    Controller().main_choice()


if __name__ == "__main__":
    main()
