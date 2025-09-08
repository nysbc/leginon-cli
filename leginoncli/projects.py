from prettytable import PrettyTable
from sinedon.models.projects import projects
from sinedon.models.projects import projectexperiments

def move_session_to_project(session_id, project_id):
    project=projects.objects.get(def_id=project_id)
    projectexperiment=projectexperiments.objects.get(ref_sessiondata_session=session_id)
    projectexperiment.ref_projects_project=project
    projectexperiment.save()

def search_by_project_name(project_name):
    query_results=projects.objects.filter(name__contains=project_name)
    if query_results:
        table=PrettyTable()
        table.field_names = ["Project Name", "Project ID"]
        for result in query_results:
            table.add_row([result.name, result.def_id])
        print(table)
        print()
    else:
        print("No matching projects for %s." % project_name)