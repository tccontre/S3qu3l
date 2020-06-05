import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# create file handler which logs even debug messages
dbg_fh = logging.FileHandler('ScanDebug.log')
dbg_fh.setLevel(logging.DEBUG)

# create file handler which logs even error messages
#err_fh = logging.FileHandler('ErrorDebug.log')
#err_fh.setLevel(logging.ERROR)

# create file handler which logs even scan messages
inf_fh = logging.FileHandler('scan.log')
inf_fh.setLevel(logging.INFO)

# create file handler which logs even scan handle
con = logging.StreamHandler()  # print in the console the log report
con.setLevel(logging.INFO)

#con.setLevel(logging.ERROR)
#con.setLevel(logging.WARNING)

# create formatter and add it to the handlers
c_format = logging.Formatter('%(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

con.setFormatter(c_format)
dbg_fh.setFormatter(f_format)
#err_fh.setFormatter(f_format)
inf_fh.setFormatter(c_format)



# Add handlers to the logger
logger.addHandler(con)
logger.addHandler(dbg_fh)
#logger.addHandler(err_fh)
logger.addHandler(inf_fh)

#logger.debug('debug message')
#logger.info('info message')
#logger.warning('warn message')
#logger.error('error message')
#logger.critical('critical message')


