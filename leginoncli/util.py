from prettytable import PrettyTable

def print_query_results(query_results, field_names):
    table=PrettyTable()
    table.field_names = field_names
    for result in query_results:
        table.add_row([result.name, result.def_id])
    print(table)
    print()

