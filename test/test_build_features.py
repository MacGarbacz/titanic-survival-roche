from src import build_features as bf
import unittest


class TestBuildFeatures(unittest.TestCase):

    def test_feature_expansion_valid(self):
        x, y = bf.feature_expansion("test_data/test_1")

        columns = x.columns.values.tolist()
        novel_columns = ["Title_value", "Fare_cat", "Age_cat", "IsAlone", "FamilySize"]

        # Check the correct output size
        self.assertEqual(len(columns), 10)

        # Check novel columns are present
        for novel_col in novel_columns:
            self.assertTrue(novel_col in columns)

        # Check no NaN values present
        self.assertFalse(x.isnull().any().any())
