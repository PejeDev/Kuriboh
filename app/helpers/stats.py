""" Stats helper. """

def get_stats(calcs, stats, result):
    """ Get stats. """
    stats = stats.get_stats()
    count = calcs.get_calcs_count_by_result(result)
    ratio = count / stats['successful']
    return {
        "count": count,
        "total": stats['total'],
        "ratio": ratio
    }
