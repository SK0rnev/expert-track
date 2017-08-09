import pytest


def detect_cancellations(receipt_items):
    """Detect pairs of cancelled receipt items.

    "Cancelled" in this context means that an item was e.g. wrongly scanned
    by the cashier and therefore removed again from the receipt or the
    customer changed his mind during the scanning process.

    In this case, the same item will appear twice on the receipt, once with
    a negative and once with a positive price.

    Parameters:
    -----------
    receipt_items: list
        A (text, price) tuple for each item on the receipt. All texts
        should be strings and all prices integers.

    Returns:
    --------
    result: list
        Indicator for each receipt item whether it is part of a cancellation
        pair or not (either True or False)
    """
    pass


def test_detect_cancellations_empty():
    assert detect_cancellations([]) == []


def test_detect_cancellations_bad_input():
    with pytest.raises(TypeError):
        detect_cancellations([(1, 2)])

    with pytest.raises(TypeError):
        detect_cancellations([('one', 'two')])

    with pytest.raises(TypeError):
        detect_cancellations([('one', 3.14)])


def test_detect_cancellations_no_match():
    items = [('Boring 1', 5),
             ('Boring 2', 3),
             ('Fancy Product', -10)]
    expected = [False, False, False]
    assert detect_cancellations(items) == expected


def detect_detect_cancellations_one_match():
    items = [('Fancy Product', 10),
             ('Boring 1', 5),
             ('Boring 2', 3),
             ('Fancy Product', -10)]
    expected = [True, False, False, True]
    assert detect_cancellations(items) == expected


def test_detect_cancellations_one_negative_multiple_positives():
    items = [('Fancy Product', 10),
             ('Fancy Product', 10),
             ('Boring 1', 5),
             ('Boring 2', 3),
             ('Fancy Product', -10)]
    expected = [True, False, False, False, True]
    assert detect_cancellations(items) == expected


def test_detect_cancellations_one_positive_multiple_negatives():
    items = [('Fancy Product', 10),
             ('Boring 1', 5),
             ('Boring 2', 3),
             ('Fancy Product', -10),
             ('Fancy Product', -10)]
    expected = [True, False, False, True, False]
    assert detect_cancellations(items) == expected


def test_detect_cancellations_two_pairs():
    items = [('Fancy Product', 10),
             ('Boring 1', 5),
             ('Boring 2', 3),
             ('Boring 2', -3),
             ('Fancy Product', -10)]
    expected = [True, False, True, True, True]
    assert detect_cancellations(items) == expected


def test_detect_cancellations_negative_before_positive():
    items = [('Fancy Product', -10),
             ('Boring 1', 5),
             ('Boring 2', 3),
             ('Fancy Product', 10)]
    expected = [False, False, False, False]
    assert detect_cancellations(items) == expected
