from prettytable import PrettyTable
from sinedon.models.leginon import SessionData

def search_by_session_name(session_name):
    query_results=SessionData.objects.filter(name__contains=session_name)
    if query_results:
        table=PrettyTable()
        table.field_names = ["Session Name", "Session ID"]
        for result in query_results:
            table.add_row([result.name, result.def_id])
        print(table)
        print()
    else:
        print("No matching sessions for %s." % session_name)
