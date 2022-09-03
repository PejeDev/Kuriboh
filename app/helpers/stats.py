""" Stats helper. """

def calculate_stats(count, stats):
    """ Get stats. """
    if stats['successful'] > 0:
        ratio = count / stats['successful']
    else:
        ratio = 0
    return {
        "count": count,
        "total": stats['total'],
        "ratio": ratio
    }
