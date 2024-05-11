import logging

# logger objects
signupLogger = logging.getLogger('signupLogger')
signupLogger.setLevel(logging.INFO)

loginLogger = logging.getLogger('loginLogger')
loginLogger.setLevel(logging.INFO)

# handlers for signup
signupHandler = logging.FileHandler('signup.log')
signupHandler.setLevel(logging.INFO)

# handlers for login
loginHandler = logging.FileHandler('login.log')
loginHandler.setLevel(logging.INFO)

# Create logger objects
signupLogger = logging.getLogger('signupLogger')
signupLogger.setLevel(logging.INFO)

loginLogger = logging.getLogger('loginLogger')
loginLogger.setLevel(logging.INFO)

errorLogger = logging.getLogger('errorLogger')
errorLogger.setLevel(logging.ERROR)

# Create file handlers
signupHandler = logging.FileHandler('signup.log')
signupHandler.setLevel(logging.INFO)

loginHandler = logging.FileHandler('login.log')
loginHandler.setLevel(logging.INFO)

errorHandler = logging.FileHandler('errors.log')
errorHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(message)s')

signupHandler.setFormatter(formatter)
loginHandler.setFormatter(formatter)
errorHandler.setFormatter(formatter)

# Add handlers to loggers
signupLogger.addHandler(signupHandler)
loginLogger.addHandler(loginHandler)
errorLogger.addHandler(errorHandler)


formatter = logging.Formatter('%(asctime)s - %(message)s')

signupHandler.setFormatter(formatter)
loginHandler.setFormatter(formatter)

# handlers to loggers
signupLogger.addHandler(signupHandler)
loginLogger.addHandler(loginHandler)