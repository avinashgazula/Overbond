import sys
import unittest
from unittest import result

from Benchmark import Benchmark


class BenchmarkTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BenchmarkTest, self).__init__(*args, **kwargs)
        self.overbond = Benchmark(input_path)

    def test_best_benchmark_index(self):
        self.assertEqual(self.overbond.best_benchmark_index(0), 0)

    def test_spread(self):
        result = self.overbond.spread()
        self.assertEqual(len(result), len(self.overbond.corporate_bonds))
        self.assertEqual(result[0]['corporate_bond_id'], "c1")
        self.assertEqual(result[0]['government_bond_id'], "g1")
        self.assertEqual(result[0]['spread'], "160 bps")


if __name__ == '__main__':
    print(sys.argv)
    if(len(sys.argv) < 3):
        raise Exception(
            "Please make sure input and output files are mentioned in the command")
    else:
        input_path = sys.argv[-1]
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
