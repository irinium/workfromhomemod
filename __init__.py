from S4CL.sims4communitylib.exceptions.common_exceptions_handler import CommonExceptionHandler
from S4CL.sims4communitylib.mod_support.mod_identity import CommonModIdentity
from S4CL.sims4communitylib.utils.common_log_registry import CommonLogRegistry

from S4CL.sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry

MOD_ID = 'work_from_homemod'
MOD_NAME = 'Work From Home'
MOD_AUTHOR = 'Iryna Shvets'
MOD_VERSION = '1.0.0'

mod_identity = CommonModIdentity(MOD_AUTHOR, MOD_ID, MOD_NAME, MOD_VERSION)

log = CommonLogRegistry.get().register_log(mod_identity, LOG_FILENAME)

_COMMUNITY_LIB_INSTALLED = False

try:
    # Try importing the Sims 4 Community Library
    from sims4communitylib import CommonLib

    _COMMUNITY_LIB_INSTALLED = CommonLib.is_installed()
except ImportError:
    pass


def _init_work_from_home_mod() -> None:
    """Initialize the Work From Home mod."""

    log.info(f'{MOD_NAME} v{MOD_VERSION} : INIT STARTED')

    if not _COMMUNITY_LIB_INSTALLED:
        log.warn(f'{MOD_NAME} requires the Sims 4 Community Library to be installed.')
        return

    log.info(f'{MOD_NAME} v{MOD_VERSION} : INIT COMPLETED')


# Initialize the mod once the game starts.
if _COMMUNITY_LIB_INSTALLED:

    @CommonEventRegistry.handle_events(mod_identity)
    def handle_work_from_home_mod_events(event_data) -> bool:
        """
        Handle Work From Home mod events.

        :param event_data: Data related to in-game events
        :type event_data: CommonEventData
        :return: True if the event was handled successfully, False otherwise
        :rtype: bool
        """

        if event_data.event_type == CommonEvent.ON_WARDROBE_LOADED:
            CommonExceptionHandler.run_with_async_exception_reporting(
                _init_work_from_home_mod,
                'Failed to initialize the Work From Home mod.'
            )
        return True
else:
    log.warn(f'{MOD_NAME} mod will not work since the Sims 4 Community Library is not installed.')
