"""Module interface.py"""
import logging
import os

import config
import src.data.dictionary
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.elements.text_attributes as txa
import src.functions.streams
import src.s3.ingress


class Interface:
    """
    Interface
    """

    def __init__(self, service: sr.Service,  s3_parameters: s3p):
        """

        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching Amazon S3 (Simple Storage Service)
                              parameters settings of this project, e.g., region code
                              name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # The instances for (a) global configuration settings, (b) reading & writing CSV files,
        # and (c) summarising the details of the files to be transferred to Amazon S3.
        self.__configurations = config.Config()
        self.__streams = src.functions.streams.Streams()
        self.__dictionary = src.data.dictionary.Dictionary()

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def __get(self):
        """
        Reads the raw data file.

        :return:
        """

        text = txa.TextAttributes(uri=self.__configurations.source, header=0)

        return self.__streams.api(text=text)

    def exc(self):
        """

        :return:
        """

        # Read
        data = self.__get()

        # Write
        message = self.__streams.write(
            blob=data, path=os.path.join(self.__configurations.raw_, 'dataset.csv'))
        self.__logger.info(message)

        # Inventory of data files
        strings = self.__dictionary.exc(
            path=self.__configurations.warehouse, extension='*',
            prefix=self.__s3_parameters.path_internal_data)

        # Transfer
        messages = src.s3.ingress.Ingress(
            service=self.__service, bucket_name=self.__s3_parameters.internal).exc(strings=strings)

        return messages
