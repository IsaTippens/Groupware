from core.template.example import add_numbers

# Example for how tests should be setup
# In the terminal run 'pytest'
# This will succeed
def test_add():
    assert add_numbers(400, 20) == 420

# This will fail
"""
def test_add_2():
    assert add_numbers(400, 20) == 1337  
"""