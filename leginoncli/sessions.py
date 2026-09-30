from sinedon.models.leginon import SessionData
from .util import print_query_results

def search_by_session_name(session_name):
    query_results=SessionData.objects.filter(name__contains=session_name)
    return query_results

def print_session_query_results(query_results):
    print_query_results(query_results, ["Session Name", "Session ID"])
