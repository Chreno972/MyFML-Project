import the_rest_test from './assets/js/main.js';

let unfetched_data = [];
let all_workspaces;

fetch("./python_local_json_API/app/data/workspaces.json").then(results => results.json()).then((data) => {
    unfetched_data.push(data); // Je récupères les données brutes
    all_workspaces = unfetched_data[0]["workspaces"]
    the_rest_test(all_workspaces)
});


