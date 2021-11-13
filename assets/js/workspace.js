class Workspace {
    constructor(
        id,
        projet,
        technologies,
        categorie,
        etat
    ) {
        this.id = id;
        this.projet = projet;
        this.technologies = technologies;
        this.categorie = categorie;
        this.etat = etat;
    }

    serialize_workspace() {
        workspace = {
            "id": this.id,
            "projet": this.projet,
            "technologies": this.technologies,
            "categorie": this.categorie,
            "etat": this.etat
        }
        return workspace;
    }
}