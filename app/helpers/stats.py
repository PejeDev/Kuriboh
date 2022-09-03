""" Stats helper. """

def calculate_stats(num_count, total_count):
    """ Get stats. """
    if total_count > 0 and num_count > 0:
        ratio = num_count / total_count
    else:
        ratio = 0
    return {
        "count": num_count,
        "total": total_count,
        "ratio": ratio
    }
