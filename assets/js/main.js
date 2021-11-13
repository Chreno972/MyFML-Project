let running_projects_container = document.getElementById("running_projects_container");
let paused_projects_container = document.getElementById("paused_projects_container");
let finished_projects_container = document.getElementById("finished_projects_container");
let rapport_en_cours = document.getElementById("rapport_en_cours");
let rapport_en_suspens = document.getElementById("rapport_en_suspens");
let rapport_termine = document.getElementById("rapport_termine");
let rap_une = 1;
let rap_two = 1;
let rap_three = 1;
let separate_workspaces = []
export default function the_rest_test(theworkspaces) {
    for (let one_workspace in theworkspaces) {
        separate_workspaces.push(theworkspaces[one_workspace])
    }
    for (let category in separate_workspaces) {
        let seps = separate_workspaces[category]
        if (seps["Etat"] === "en cours") {
            insert_in_html_skull(running_projects_container, seps["Projet"], seps["Workspace_name"], seps["Categorie"], seps["Technologies"], seps["Etat"])
            let total = rap_une++;
            console.log(rapport_en_cours.innerHTML = total)
        } else if (seps["Etat"] === "en suspens") {
            insert_in_html_skull(paused_projects_container, seps["Projet"], seps["Workspace_name"], seps["Categorie"], seps["Technologies"], seps["Etat"])
            let total = rap_two++;
            console.log(rapport_en_suspens.innerHTML = total)
        } else if (seps["Etat"] === "termine") {
            insert_in_html_skull(finished_projects_container, seps["Projet"], seps["Workspace_name"], seps["Categorie"], seps["Technologies"], seps["Etat"])
            let total = rap_three++;
            console.log(rapport_termine.innerHTML = total)
        } else {
            console.log("Au secours loll, il y a un problème dans le nommage de l'état d'un ou plusieurs états de vos workspaces")
        }
    }
    return separate_workspaces
}

function insert_in_html_skull(the_container, project_title, workspace_name, category, technology, state) {
    the_container.innerHTML += `
    <div class="workspaces" id="${state}">
    <h3 class="workspace_title" id="${project_title}">${project_title}</h3><br/>
    <span>Workspace</span>
    <p class="workspace_name">${workspace_name}</p><br/>
    <span>Catégorie</span>
    <p class="workspace_category">${category}</p><br/>
    <span>Technologies</span>
    <p class="workspace_Technology">${technology}</p><br/>
    <span>Etat</span>
    <p class="workspace_state">${state}</p><br/>
    </div>
    `
}
