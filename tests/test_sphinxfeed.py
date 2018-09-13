import filecmp
from atelier.test import TestCase

class AllTests(TestCase):
    def test_all(self):

        args = ['sphinx-build']
        args += ["-b"]
        args += ["html"]
        args += ["tests/docs1"]
        args += ["tmp"]
        self.run_subprocess(args)

        common = ["rss.xml", "index.html", "first.html",
                  "search.html", "genindex.html", "searchindex.js"]
        
        match, mismatch, errors = filecmp.cmpfiles(
            "tests/docs1/expected", "tmp", common)

        

        self.assertEqual(match, common)
