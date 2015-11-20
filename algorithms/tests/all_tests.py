"""Run all of the tests."""
import sys
import unittest2 as unittest


def main(args=None):
    unittest_dir = '.'
    unittest_suite = unittest.defaultTestLoader.discover(unittest_dir)

    kwargs = {}
    if args and '-v' in args:
        kwargs['verbosity'] = 2
    runner = unittest.TextTestRunner(sys.stdout, "Unittests",
                                     **kwargs)
    results = runner.run(unittest_suite)
    return results.wasSuccessful()

if __name__ == '__main__':
    status = main(sys.argv[1:])
    sys.exit(int(not status))
