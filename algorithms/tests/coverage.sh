coverage run --source=$PYTHONPATH/algorithms --omit=$PYTHONPATH/algorithms/tests/* all_tests.py
coverage report --omit=$PYTHONPATH/algorithms/tests/* -m
