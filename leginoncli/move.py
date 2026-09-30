from .projects import search_by_project_name, print_project_query_results
from .sessions import search_by_session_name, print_session_query_results
from sinedon.models.projects import projects
from sinedon.models.projects import projectexperiments

def move_session_to_project_by_name(session_name, project_name):
    session_query_results=search_by_session_name(session_name.strip())
    project_query_results=search_by_project_name(project_name)
    if len(session_query_results) == 0:
        print(f"No matches for the session {session_name}.")
        return
    if len(project_query_results) == 0:
        print(f"No matches for the project {project_name}.")
        return
    if len(session_query_results) == 1:
        session_id=session_query_results[0].def_id
    else:
        valid_ids=set([int(r.def_id) for r in session_query_results])
        session_id=None
        while not session_id:
            print_session_query_results(session_query_results)
            session_id = input("Multiple sessions matched.  Please type in the session ID number based on the list above.\n")
            try:
                session_id = int(session_id)
            except ValueError:
                print(f"Could not interpret '{session_id}' as an integer. Try again.")
                session_id=None
                continue
            if session_id not in valid_ids:
                print(f"{session_id} is not an ID number from the list above.  Try again.")
                session_id=None
    if len(project_query_results) == 1:
        project_id=project_query_results[0].def_id
    else:
        valid_ids=set([int(r.def_id) for r in project_query_results])
        project_id=None
        while not project_id:
            print_project_query_results(project_query_results)
            project_id = input("Multiple projects matched.  Please type in the project ID number based on the list above.\n")
            try:
                project_id = int(project_id)
            except ValueError:
                print(f"Could not interpret '{project_id}' as an integer. Try again.")
                project_id=None
                continue
            if project_id not in valid_ids:
                print(f"{project_id} is not an ID number from the list above.  Try again.")
                project_id=None
    print(f"Moving session {session_id} to project {project_id}.")
    move_session_to_project_by_id(session_id, project_id)
    print(f"Session {session_id} moved to project {project_id}.")

def move_session_to_project_by_id(session_id, project_id):
    project=projects.objects.get(def_id=project_id)
    projectexperiment=projectexperiments.objects.get(ref_sessiondata_session=session_id)
    projectexperiment.ref_projects_project=project
    projectexperiment.save()

