from ..worker_proposal import WorkerProposal
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestWorkerProposal(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(WorkerProposal, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")
