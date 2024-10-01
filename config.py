"""config.py"""
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # The temporary local directory where data sets are initially placed,
        # prior to transfer to Amazon S3 (Simple Storage Service)
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.raw_: str = os.path.join(self.warehouse, 'raw')

        # Data source
        self.source = 'https://raw.githubusercontent.com/membranes/.github/refs/heads/master/data/dataset.csv'

        # A template of Amazon S3 (Simple Storage Service) parameters
        self.s3_parameters_template = 'https://raw.githubusercontent.com/membranes/.github/refs/heads/master/profile/s3_parameters.yaml'
