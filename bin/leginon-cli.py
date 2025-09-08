#!/usr/bin/env python
import argparse
import sinedon.setup
sinedon.setup()
from leginoncli.projects import search_by_project_name, move_session_to_project

def constructParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # Project subcommand
    parser_project = subparsers.add_parser('projects')
    subparsers_project = parser_project.add_subparsers()
    # Project move operation
    parser_project_move = subparsers_project.add_parser('move')
    parser_project_move.add_argument('--sessionid', dest="sessionid", type=int, help='Session ID of the session that you want to move to a different project')
    parser_project_move.add_argument('--projectid', dest="projectid", type=int, help='Project ID for the destination project that you want to move a session to.')
    # Project search operation
    parser_project_move = subparsers_project.add_parser('search')
    parser_project_move.add_argument('--projectname', dest="projectname", type=str, help='Project ID for the destination project that you want to move a session to.')
    return parser

def main():
    parser = constructParser()
    args = parser.parse_args()
    if "sessionid" in dir(args) and "projectid" in dir(args):
        move_session_to_project(args.sessionid, args.projectid)
    if "projectname" in dir(args):
        search_by_project_name(args.projectname)

if __name__ == '__main__':
    main()