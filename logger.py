# Step 1: Add Logging for Debugging
# Using the logging module helps capture errors and track execution flow

import logging

# Configure Logging
logging.basicConfig(
    filename="app.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

logger.info("Logging initialized")
