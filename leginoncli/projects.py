from sinedon.models.projects import projects
from sinedon.models.projects import projectexperiments
from .util import print_query_results

def search_by_project_name(project_name):
    query_results=projects.objects.filter(name__contains=project_name)
    return query_results

def print_project_query_results(query_results):
    print_query_results(query_results, ["Project Name", "Project ID"])
