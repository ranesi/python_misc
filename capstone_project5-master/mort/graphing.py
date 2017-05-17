from pygooglechart import PieChart2D
import os

DEFAULT_FILENAME = 'mort_graph'
DEFAULT_EXTENSION = '.png'

'''
    Mortality Causes Graphing Module
    Purpose:
        • generate pie chart of mortality information
        • stored as PNG in mort/static
    Functions:
        • graph_result(r: list)
            - args: list of dict objects from cdc query
            - adds counts for cause of death as chart fields
            - generate number (1 though n) signifying rank
        • generate_filename()
            - programmatically generates filenames to avoid
              caching issues
            - TODO delete old entries
'''


def graph_result(r):

    f_name = generate_filename()

    chart = PieChart2D(500, 300)
    chart.set_title('Top 10 Causes of Mortality')
    counts, causes = [], []
    x = 0  # counter variable
    for result in r:
        counts.append(int(result['count']))
        causes.append('No. ' + str(x + 1))
        x += 1
    chart.add_data(counts)
    chart.set_pie_labels(causes)
    chart.download(f_name)
    return f_name


def generate_filename():
    f = os.path.join('static/images/') + DEFAULT_FILENAME + DEFAULT_EXTENSION
    x = 0  # counter variable
    while True:
        if os.path.exists(f):
            f = os.path.join('static/images/') + \
                DEFAULT_FILENAME + str(x) + DEFAULT_EXTENSION
            x += 1
        else:
            break
    return f
