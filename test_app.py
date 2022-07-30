from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            # test that you're getting a template
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- THIS IS THE HOMEPAGE -->', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.post('/api/new-game')
            json = response.get_json()

            self.assertTrue(isinstance(json["gameId"], str))
            self.assertTrue(isinstance(json["board"], list))
            self.assertTrue(isinstance(json["board"][0], list))
            self.assertIn(json["gameId"], games)


    def test_score_word(self):
        """Test if the word is legal"""

        with self.client as client:
           game =

            response = client.post('/api/score-word', json={"word": "CAT", "gameId": "123"})
            json_response = response.get_json()
            breakpoint()
            self.assertEqual({"result": "ok"}, json_response)

            games["gameId"] = [["C", "A", "T", "X", "X"],
                        ["T", "A", "T", "X", "X"],
                        ["P", "A", "T", "X", "X"]
                        ["P", "A", "T", "X", "X"]
                        ["P", "A", "T", "X", "X"]]
        # with self.client as client:
        #     response = client.post('/api/score-word', json={"word": "ZZZ", "gameId": "123"})
        #     self.assertEqual({"result": "not-word"}, response.get_json())

        # with self.client as client:
        #     response = client.post('/api/score-word', json={"word": "FAT", "gameId": "123"})

        #     self.assertEqual({"result": "not-on-board"}, response.get_json())



        #change board in games object

            """ checks if word is legal
                returns json
                    if not a word:  {result: "not-word"}
                    if not on board:  {result: "not-on-board"}
                    if a valid word:  {result: "ok"}
            """


# make own board to test words, after
