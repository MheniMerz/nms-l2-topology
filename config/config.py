import os
import logging
import configparser

class Config:
    def __init__(self):
        self.repeat_timer = os.environ.get('REPEAT_TIMER')
        self.url_base = os.environ.get('API_SERVER_URL')
        self.ssl_verify = os.environ.get('CERT_VERIFY')=='True'
        self.conf_file_path = os.environ.get('CONF_FILE')
        self.conf_file_contents = self.read_config()
        self.logger = self.init_logger()
    
    def read_config(self):
        # open config file
        try:
            config = configparser.ConfigParser()
            config.read(self.conf_file_path)
            config.sections()
            return config
        except IOError:
            log.critical("*********** ERROR reading config file **********")
            exit(1)

    def init_logger(self):
        log = logging.getLogger()
        console = logging.StreamHandler()
        log.addHandler(console)
        return log
    
