'''Tests for the right proper execution of the dependency resolver'''

import unittest

from src.dependancy_resolver import dependency_resolver


class TestDependency(unittest.TestCase):
    '''Defining my class name for the tests as TestDependency'''


    def test_dependency_with_e(self):
        '''Test for dependency resolver with E'''
        self.assertEqual(dependency_resolver('E'), ['G','D','E'])

    def test_dependency_with_b(self):
        '''Test for dependency resolver with B'''
        self.assertEqual(dependency_resolver('B'), ['F','B'])

    def test_dependency_with_a(self):
        '''Test for dependency resolver with A'''
        self.assertEqual(dependency_resolver('A'), ['F', 'B', 'G', 'D','G', 'D', 'E', 'A'])

    def test_dependency_with_d(self):
        '''Test for dependency resolver with D'''
        self.assertEqual(dependency_resolver('D'), ['G', 'D'])

    def test_dependency_with_c(self):
        '''Test for dependency resolver with C'''
        self.assertEqual(dependency_resolver('C'), ['G', 'F', 'B', 'G','D', 'G', 'D',
                                                    'E', 'A', 'F', 'B', 'H', 'C'])

    def test_dependency_with_f(self):
        '''Test for dependency resolver with F'''
        self.assertEqual(dependency_resolver('F'), ['F'])

    def test_dependency_with_g(self):
        '''Test for dependency resolver with G'''
        self.assertEqual(dependency_resolver('G'), ['G'])

    def test_dependency_with_h(self):
        '''Test for dependency resolver with H'''
        self.assertEqual(dependency_resolver('H'), ['F', 'B', 'G', 'D', 'G', 'D', 'E',
                                                    'A', 'F', 'B', 'H'])

    def test_dependency_with_i(self):
        '''Test for dependency resolver with I'''
        self.assertEqual(dependency_resolver('I'), ['F', 'B', 'G', 'D', 'G', 'D', 'E',
                                                    'A', 'F', 'B', 'H', 'I'])



if __name__ == '__main__':
    unittest.main()
