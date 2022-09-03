""" Stats helper. """

def calculate_stats(count, stats):
    """ Get stats. """
    ratio = count / stats['successful']
    return {
        "count": count,
        "total": stats['total'],
        "ratio": ratio
    }
