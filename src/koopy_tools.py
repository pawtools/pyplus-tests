

def set_compute_package(module, package_name):
    '''Set the package used for calculations
    before any actual work is run. The package must
    provide algebraic operations with functions
    having same name as in numpy.

    Parameters
    ----------
    package_name : 'numpy','cupy', or ??
        Package with numpy-like operations

    module : python module
        module with "CPT" global attribute that stores
        the chosen compute package

    '''
    import importlib

    try:
        assert hasattr(module, "CPT")
        module.CPT = importlib.import_module(package_name)

    except Exception as e:
        # If want to fall back to default
        #default = 'numpy'
        #CPT = importlib.import_module(default)
        raise e


def get_logger(logname, loglevel='info', logfile=True):
    '''Logger with nice formatting to inspect
    control flow and residence in targeted
    regions of a code.
    '''

    import logging

    try:
        if loglevel.lower() == 'info':
            _loglevel = logging.INFO
        elif loglevel.lower() == 'debug':
            _loglevel = logging.DEBUG
        elif loglevel.lower() == 'warning':
            _loglevel = logging.WARNING
        elif loglevel.lower() == 'error':
            _loglevel = logging.ERROR
        # catch attempted set values as WARNING level
        elif isinstance(loglevel, str):
            _loglevel = logging.WARNING
        else:
            _loglevel = logging.WARNING

    # catch None's for not set
    except:
        _loglevel = logging.WARNING

    formatter = logging.Formatter(
        fmt="[ %(asctime)s.%(msecs)05d ] %(name)s :: %(levelname)s :: %(lineno)d ||  %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    logging.basicConfig(level=_loglevel)#, format=formatter)
    logger  = logging.getLogger(logname)

    ch = logging.StreamHandler()
    #ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(_loglevel)
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    if logfile:
        logfilename = logname + '.log'
        if logfilename.startswith("__main__"):
            logfilename = "main." + logfilename
        logfilename = "logs/%s" % logfilename
        fh = logging.FileHandler(logfilename)
        fh.setLevel(_loglevel)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.propagate = False

    return logger
