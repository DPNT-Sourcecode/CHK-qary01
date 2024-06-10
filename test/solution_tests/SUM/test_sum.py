from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_non_integers(self):
        with self.assertRaises(ValueError):
            sum_solution.compute(1, "2")
        
        with self.assertRaises(ValueError):
            sum_solution.compute("1", 2)
        
        with self.assertRaises(ValueError):
            sum_solution.compute("1", "2")
