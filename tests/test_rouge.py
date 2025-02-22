import unittest
import gem_metrics.rouge
from tests.test_referenced import TestReferencedMetric


class TestRouge(TestReferencedMetric, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.metric = gem_metrics.rouge.ROUGE()
        self.true_results_basic = {
            "rouge1": {
                "low": {
                    "precision": 0.4000000000000001,
                    "recall": 0.2857142857142857,
                    "fmeasure": 0.3333333333333333,
                },
                "mid": {
                    "precision": 0.673015873015873,
                    "recall": 0.5777777777777778,
                    "fmeasure": 0.6203949307397583,
                },
                "high": {
                    "precision": 0.8333333333333334,
                    "recall": 0.7333333333333333,
                    "fmeasure": 0.7692307692307692,
                },
            },
            "rouge2": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {
                    "precision": 0.36130536130536123,
                    "recall": 0.32051282051282054,
                    "fmeasure": 0.3395061728395062,
                },
                "high": {
                    "precision": 0.5454545454545454,
                    "recall": 0.5,
                    "fmeasure": 0.5185185185185186,
                },
            },
            "rougeL": {
                "low": {
                    "precision": 0.20000000000000004,
                    "recall": 0.14285714285714285,
                    "fmeasure": 0.16666666666666666,
                },
                "mid": {
                    "precision": 0.5785714285714286,
                    "recall": 0.5063492063492063,
                    "fmeasure": 0.5391983495431771,
                },
                "high": {
                    "precision": 0.7857142857142857,
                    "recall": 0.7333333333333333,
                    "fmeasure": 0.7586206896551723,
                },
            },
            "rougeLsum": {
                "low": {
                    "precision": 0.20000000000000004,
                    "recall": 0.14285714285714285,
                    "fmeasure": 0.16666666666666666,
                },
                "mid": {
                    "precision": 0.5785714285714286,
                    "recall": 0.5063492063492063,
                    "fmeasure": 0.5391983495431771,
                },
                "high": {
                    "precision": 0.7857142857142857,
                    "recall": 0.7333333333333333,
                    "fmeasure": 0.7586206896551723,
                },
            },
        }
        self.true_results_identical_pred_ref = {
            "rouge1": {
                "low": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "mid": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "high": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
            },
            "rouge2": {
                "low": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "mid": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "high": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
            },
            "rougeL": {
                "low": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "mid": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "high": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
            },
            "rougeLsum": {
                "low": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "mid": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
                "high": {"precision": 1.0, "recall": 1.0, "fmeasure": 1.0},
            },
        }
        self.true_results_mismatched_pred_ref = {
            "rouge1": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rouge2": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rougeL": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rougeLsum": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
        }
        self.true_results_empty_pred = {
            "rouge1": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rouge2": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rougeL": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
            "rougeLsum": {
                "low": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "mid": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
                "high": {"precision": 0.0, "recall": 0.0, "fmeasure": 0.0},
            },
        }


if __name__ == "__main__":
    unittest.main()
