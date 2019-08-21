

def get_logger(logname, loglevel='info', logfile=True):

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
        fh = logging.FileHandler(logfilename)
        fh.setLevel(_loglevel)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    logger.propagate = False

    return logger
