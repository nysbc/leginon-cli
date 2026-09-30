#!/usr/bin/env python
import argparse
import sinedon.setup
sinedon.setup()
from .projects import search_by_project_name, print_project_query_results
from .sessions import search_by_session_name, print_session_query_results
from .move import move_session_to_project_by_id, move_session_to_project_by_name

def constructParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Project subcommand
    parser_project = subparsers.add_parser('projects')
    subparsers_project = parser_project.add_subparsers()
    # Project search operation
    parser_project_search = subparsers_project.add_parser('search')
    parser_project_search.add_argument('--projectname', dest="projectname", type=str, help='Project name whose ID you are searching for.')

    # Session subcommand
    parser_session = subparsers.add_parser('sessions')
    subparsers_session = parser_session.add_subparsers()
    # Session search operation
    parser_session_search = subparsers_session.add_parser('search')
    parser_session_search.add_argument('--sessionname', dest="sessionname", type=str, help='Session name whose ID you are searching for.')

    # Move operation
    parser_move = subparsers.add_parser('move')
    subparsers_move = parser_move.add_subparsers()
    # Move by ID
    parser_move_id = subparsers_move.add_parser('id')
    parser_move_id.add_argument('--sessionid', dest="sessionid", type=int, help='Session ID of the session that you want to move to a different project')
    parser_move_id.add_argument('--projectid', dest="projectid", type=int, help='Project ID for the destination project that you want to move a session to.')
    # Move by name
    parser_move_name = subparsers_move.add_parser('name')
    parser_move_name.add_argument('--sessionname', dest="sessionname", type=str, help='Session name of the session that you want to move to a different project')
    parser_move_name.add_argument('--projectname', dest="projectname", type=str, help='Project name for the destination project that you want to move a session to.')

    return parser

def main():
    parser = constructParser()
    args = parser.parse_args()
    if "sessionid" in dir(args) and "projectid" in dir(args):
        move_session_to_project_by_id(args.sessionid, args.projectid)
    if "projectname" in dir(args) and "sessionname" in dir(args):
        move_session_to_project_by_name(args.sessionname, args.projectname)
    elif "projectname" in dir(args):
        project_query_results=search_by_project_name(args.projectname)
        if project_query_results:
            print_session_query_results(project_query_results)
        else:
            print("No matching projects for %s." % args.projectname)
    elif "sessionname" in dir(args):
        session_query_results=search_by_session_name(args.sessionname)
        if session_query_results:
            print_session_query_results(session_query_results)
        else:
            print("No matching sessions for %s." % args.sessionname)
