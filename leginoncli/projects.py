from prettytable import PrettyTable
from sinedon.models.projects import projects
from sinedon.models.projects import projectexperiments

def search_by_project_name(project_name):
    query_results=projects.objects.filter(name__contains=project_name)
    return query_results

def print_project_query_results(query_results):
    table=PrettyTable()
    table.field_names = ["Project Name", "Project ID"]
    for result in query_results:
        table.add_row([result.name, result.def_id])
    print(table)
    print()

