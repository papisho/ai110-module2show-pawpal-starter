import pytest
from datetime import datetime, timedelta

from pawpal_system import Task, Pet, Priority, Scheduler


def test_mark_complete_changes_status():
    """Task Completion: Verify that calling mark_complete() 
    actually changes the task's status."""
    task = Task("Morning walk", 30, Priority.HIGH, time_of_day="morning")
    
    # Before completion
    assert task.completed == False
    
    # After calling mark_complete()
    task.mark_complete()
    assert task.completed == True


def test_add_task_increases_count():
    """Task Addition: Verify that adding a task to a Pet 
    increases that pet's task count."""
    pet = Pet(name="Mochi", species="cat", age=3)
    
    # Initial state: no tasks
    assert len(pet.get_tasks()) == 0
    
    # Add one task
    task = Task("Feeding", 10, Priority.MEDIUM, time_of_day="morning")
    pet.add_task(task)
    
    # Task count should be 1
    assert len(pet.get_tasks()) == 1


def test_sorting_correctness_returns_chronological_order():
    """Sorting Correctness: tasks should be returned in chronological HH:MM order."""
    pet = Pet(name="Mochi", species="cat", age=3)
    pet.add_task(Task("Evening walk", 20, Priority.MEDIUM, time="18:30"))
    pet.add_task(Task("Morning feed", 10, Priority.HIGH, time="07:15"))
    pet.add_task(Task("Lunch meds", 5, Priority.HIGH, time="12:00"))

    scheduler = Scheduler(pet)
    sorted_tasks = scheduler.sort_by_time()

    assert [task.time for task in sorted_tasks] == ["07:15", "12:00", "18:30"]


def test_recurrence_logic_daily_completion_creates_next_day_task():
    """Recurrence Logic: completing a daily task should create the next day's task."""
    pet = Pet(name="Rex", species="dog", age=5)
    scheduler = Scheduler(pet)
    start_due = datetime(2026, 3, 31, 8, 0)

    daily_task = Task(
        title="Morning feed",
        duration_minutes=10,
        priority=Priority.HIGH,
        time="08:00",
        recurring=True,
        frequency="daily",
        due_date=start_due,
    )
    pet.add_task(daily_task)

    next_task = scheduler.mark_task_complete_with_recurrence(daily_task)

    assert daily_task.completed is True
    assert next_task is not None
    assert next_task.title == daily_task.title
    assert next_task.completed is False
    assert next_task.due_date == start_due + timedelta(days=1)
    assert len(pet.get_tasks()) == 2


def test_conflict_detection_flags_duplicate_times():
    """Conflict Detection: scheduler should warn when two tasks share the same time."""
    pet = Pet(name="Buddy", species="dog", age=4)
    pet.add_task(Task("Morning walk", 30, Priority.HIGH, time="07:00"))
    pet.add_task(Task("Morning grooming", 15, Priority.MEDIUM, time="07:00"))

    scheduler = Scheduler(pet)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "CONFLICT at 07:00" in conflicts[0]
