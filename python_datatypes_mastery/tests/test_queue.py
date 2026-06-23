"""Tests for SimpleQueue implementation."""
import pytest

from python_datatypes_mastery.exercises.queue import SimpleQueue


def test_enqueue_dequeue_size():
    q = SimpleQueue()
    assert q.size() == 0
    q.enqueue(1)
    q.enqueue(2)
    assert q.size() == 2
    assert q.dequeue() == 1
    assert q.size() == 1


def test_dequeue_empty_raises():
    q = SimpleQueue()
    with pytest.raises(IndexError):
        q.dequeue()
