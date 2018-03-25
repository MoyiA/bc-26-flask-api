import unittest
from flask_script import Manager
from main.app import create_app

app = create_app('develop')

#extending app to accept command arguments
manager = Manager(app)

#add command line arguments here
@manager.command
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
