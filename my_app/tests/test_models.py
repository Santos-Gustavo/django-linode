from .test_work_base import WorkTestsBase


class ModelTests(WorkTestsBase):
    def setUp(self):
        super().setUp()
        self.make_job(type_job=1)