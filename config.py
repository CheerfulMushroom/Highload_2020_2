import logging
import pathlib


class Config:
    base_dir = str(pathlib.Path().absolute()) + '/http-test-suite'
    index_filename = 'index.html'

    # CONNECTION
    addr = '0.0.0.0'
    port = 3000
    max_connections = 100
    bytes_per_recv = 1024
    sendfile = False
    bytes_per_send = 1024  # ignored if sendfile = True

    # WORKERS
    workers_process_amount = 4

    # LOGGING
    log_level = logging.DEBUG
    log_format = '%(asctime)s %(levelname)s\t%(name)s[%(process)d]  \t%(message)s'
    log_date_format = '%H:%M:%S'

    log_worker_spawner_verbose = False
    log_worker_verbose = False
