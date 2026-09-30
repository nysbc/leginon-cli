#!/usr/bin/env python
import argparse
import sinedon.setup
sinedon.setup()
from .projects import search_by_project_name, print_project_query_results
from .sessions import search_by_session_name, print_session_query_results
from .move import move_session_to_project_by_id, move_session_to_project_by_name

def constructParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="primary_subcommand")

    # Project subcommand
    parser_project = subparsers.add_parser('projects')
    subparsers_project = parser_project.add_subparsers(dest="secondary_subcommand")
    # Project search operation
    parser_project_search = subparsers_project.add_parser('search')
    parser_project_search.add_argument('--projectname', dest="projectname", type=str, help='Project name whose ID you are searching for.')

    # Session subcommand
    parser_session = subparsers.add_parser('sessions')
    subparsers_session = parser_session.add_subparsers(dest="secondary_subcommand")
    # Session search operation
    parser_session_search = subparsers_session.add_parser('search')
    parser_session_search.add_argument('--sessionname', dest="sessionname", type=str, help='Session name whose ID you are searching for.')

    # Move subcommand
    parser_move = subparsers.add_parser('move')
    session_group = parser_move.add_mutually_exclusive_group()
    project_group = parser_move.add_mutually_exclusive_group()
    session_group.add_argument('--sessionid', dest="sessionid", type=int, help='Session ID of the session that you want to move to a different project')
    session_group.add_argument('--sessionname', dest="sessionname", type=str, help='Session name of the session that you want to move to a different project')
    project_group.add_argument('--projectid', dest="projectid", type=int, help='Project ID for the destination project that you want to move a session to.')
    project_group.add_argument('--projectname', dest="projectname", type=str, help='Project name for the destination project that you want to move a session to.')

    return parser

def main():
    parser = constructParser()
    args = parser.parse_args()
    primary_subcommand=args.primary_subcommand
    if "secondary_subcommand" in dir(args):
        secondary_subcommand=args.secondary_subcommand
    else:
        secondary_subcommand=""
    if primary_subcommand == "move":
        if args.sessionid and args.projectid:
            move_session_to_project_by_id(args.sessionid, args.projectid)
        elif args.sessionname and args.projectname:
            move_session_to_project_by_name(args.sessionname, args.projectname)
        else:
            print("Unsupported operation. Cannot mix the following flags: %s" % ", ".join([k for k,v in vars(args).items() if v and k != "primary_subcommand" and k != "secondary_subcommand" ]))
    elif "projectname" in dir(args) and primary_subcommand == "projects" and secondary_subcommand == "search":
        project_query_results=search_by_project_name(args.projectname)
        if project_query_results:
            print_project_query_results(project_query_results)
        else:
            print("No matching projects for %s." % args.projectname)
    elif "sessionname" in dir(args) and primary_subcommand == "sessions" and secondary_subcommand == "search":
        session_query_results=search_by_session_name(args.sessionname)
        if session_query_results:
            print_session_query_results(session_query_results)
        else:
            print("No matching sessions for %s." % args.sessionname)
