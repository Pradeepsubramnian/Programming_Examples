def plot_histogram(data, design='=== ', show_labels=True, align=False):
    '''
    plots a text based horizontal histogram
    Args:
        data: A dictionary containing items as key and frequencey as value: {2:3, 4:1,5:7}
        design: The design of a single bar unit (default: '===')
        show_labels: if we should show the frequency value after the bar (default: True)
        align: if frequency values should be aligned. (default: False)

    Examples:
    >>> histogram({2:4, 3:1, 5:9})
    2 |=== === === === 4
    3 |=== 1
    5 |=== === === === === === === === === 9

    >>> histogram({2:4, 3:1, 5:9}, design="❚❚❚')
    2 |❚❚❚❚❚❚❚❚❚❚❚❚4
    3 |❚❚❚1
    5 |❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚9

    >>> histogram({2:4, 3:1, 5:9}, design="❚❚❚', show_labels=False)
    2 |❚❚❚❚❚❚❚❚❚❚❚❚
    3 |❚❚❚
    5 |❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚

    >>> histogram({2:4, 3:1, 5:9}, design="❚❚❚', align=True)
    2 |❚❚❚❚❚❚❚❚❚❚❚❚              4
    3 |❚❚❚                     1
    5 |❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚❚  9


    '''
    for key,value in data.items():
        label= value if show_labels else ''
        print(f'{key}|{design*value} {label}')