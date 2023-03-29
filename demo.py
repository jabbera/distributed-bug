import logging
logging.basicConfig(level=logging.DEBUG)

from distributed import SSHCluster

cluster = SSHCluster(["localhost", "localhost"])
