# -*- coding: UTF-8 -*-
# Copyright 2018-2019 Rumma & Ko Ltd

import filecmp
from atelier.test import TestCase

class AllTests(TestCase):
    def test_all(self):
        """
        Run a sphinx-build and then check whether the generated files (in
        `tmp`) are the same as in `expected`.

        The tests fail when the Sphinx version has changed.  In that case::

          $ diff tmp/ tests/docs1/expected

        and if there is no other changes, update the expected files::

          $ cp tmp/*.html tmp/*.js tests/docs1/expected

        """
        args = ['sphinx-build']
        args += ["-b"]
        args += ["html"]
        args += ["tests/docs1"]
        args += ["tmp"]
        self.run_subprocess(args)

        common = ["index.html", "first.html",
                  "search.html", "genindex.html", "searchindex.js"]
        # common.append("rss.xml")

        match, mismatch, errors = filecmp.cmpfiles(
            "tests/docs1/expected", "tmp", common)

        self.assertEqual(mismatch, [])
        self.assertEqual(match, common)
