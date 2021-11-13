class MdFile {
    constructor(title, technologies, path, file_name, description) {
        this.title = title;
        this.technologies = technologies;
        this.path = path;
        this.file_name = file_name;
        this.description = description;
    }

    serialize_md_file() {
        md_file = {
            "titre": this.title,
            "technologies": this.technologies,
            "chemin": this.path,
            "nom_fichier": this.file_name,
            "description": this.description
        }
        return md_file;
    }
}