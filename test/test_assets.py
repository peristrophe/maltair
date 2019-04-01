import helper
import maltair
import unittest
import os

from pprint import pprint

class AssetsTest(unittest.TestCase):

    def setUp(self):
        auth_data = {
            'base_url': os.getenv('MARKETO_BASE_URL'),
            'client_id': os.getenv('MARKETO_CLIENT_ID'),
            'client_secret': os.getenv('MARKETO_CLIENT_SECRET'),
        }

        self.client = maltair.Client(**auth_data)


    def tearDown(self):
        if hasattr(self, 'assets'):
            pprint(self.assets)


    def test_channels(self):
        self.assets = self.client.channels()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Channel))


    def test_email_templates(self):
        self.assets = self.client.email_templates()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.EmailTemplate))


    def test_emails(self):
        self.assets = self.client.emails()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Email))


    def test_files(self):
        self.assets = self.client.files()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.File))


    def test_folders(self):
        self.assets = self.client.folders(maxDepth=0)
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Folder))


    def test_forms(self):
        self.assets = self.client.forms()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Form))


    def test_form_fields(self):
        self.assets = self.client.form_fields()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.FormField))


    def test_landing_page_templates(self):
        self.assets = self.client.landing_page_templates()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.LandingPageTemplate))


    def test_landing_pages(self):
        self.assets = self.client.landing_pages()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.LandingPage))


    def test_programs(self):
        self.assets = self.client.programs()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Program))


    def test_segments(self):
        self.assets = self.client.segments()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Segment))


    def test_smart_lists(self):
        self.assets = self.client.smart_lists()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.SmartList))


    def test_snippets(self):
        self.assets = self.client.snippets()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Snippet))


    def test_static_lists(self):
        self.assets = self.client.static_lists()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.StaticList))


    def test_tags(self):
        self.assets = self.client.tags()
        for asset in self.assets:
            self.assertTrue(isinstance(asset, maltair.models.Tag))


if __name__ == '__main__':
    unittest.main()
