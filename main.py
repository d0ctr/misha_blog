import logging

from dotenv import load_dotenv

from src.bot import start

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('main')

if __name__ == '__main__':
    logger.debug('Starting bot')
    start(logger)
