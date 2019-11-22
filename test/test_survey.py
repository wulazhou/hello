import unittest
# import sys
# sys.path.append("..")
from sruvey import AnonymoousSurvery
class TestAnonymousSurey(unittest.TestCase):
    """  """
    def test_store_single_response(self):
        """  """
        question = "What language did you first learn to speak?"  
        my_survey=AnonymoousSurvery(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
unittest.main()
