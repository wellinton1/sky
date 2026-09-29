import importlib.util
import pathlib
import unittest

_SPEC = importlib.util.spec_from_file_location(
    "badges", pathlib.Path(__file__).resolve().parents[1] / "tools" / "badges.py"
)
badges = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(badges)


class ReportTest(unittest.TestCase):
    def test_report_marks_ok(self):
        self.assertIsNone(badges.report("item", True, "detalhe"))

    def test_report_marks_missing(self):
        self.assertIsNone(badges.report("item", False))


class ConfigTest(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(badges.API, "https://api.github.com")
        self.assertEqual(badges.TIMEOUT, 15)

    def test_headers_always_has_user_agent(self):
        self.assertIn("User-Agent", badges._headers())


if __name__ == "__main__":
    unittest.main()
