import re
from contextlib import suppress
import logging as loggingmod

from django.core.exceptions import ValidationError

logger = loggingmod.getLogger(__name__)

# required
def common_name(): return "privacy info"  # What short name should others know us as?

# required
def help():
    """Return a list of messages to tell the user about this module. Lead with
    the canonical keyword that would claim a conversation, and then dashes and
    a little pitch for using it. Phrase as: 
    "keyword" -- what I can do for you."""
    return [ '''"{0}" -- tell you how we treat your personal data'''.format(common_name()) ]

# required
def claims_conversation(message):
    """Returns whether the incoming message is sufficient to indicate that user
    wants to start a conversation. Should all future messages from this user be
    directed to this module's handlers? If return value is not falsey, this
    returned value is passed into the first receive() as the third param."""
    if re.search(r"(?i)\bprivacy\s*info(?:rmation)?\b", message): return "en" #en is initial_state_info

# required
def abort(caller_number):
    """User signaled they want to abort all state. Returns nothing. This may be
    called even if a conversation has never started."""

    # with suppress(models.Foo.DoesNotExist):
    #     models.Foo.filter(phone_number=caller_number).delete()

    pass  # No database state to throw away.


# required
def receive(caller_number, incoming_message, initial_state_info=None):
    """Triggers and edges in the finite-state-machine graph. Return a tuple of
    messages,finished. Messages is a list of outgoing response. finished is a
    signal that the next message should not automatically come here, and that
    we want to yield attention to another app-let."""

    # record, _ = models.Foo.objects.get_or_create(caller_number=caller_number)

    outgoing_messages = []

    if initial_state_info or not incoming_message:
        logger.debug("new conversation!")
        #outbound_messages.append("Okay, let's get started. Send \"start over\" any time.")
        #outgoing_messages.append("I'll ask five questions. Please give simple answers.")

    conversation_ends_now = True   # Give up the session. We're done. Next incoming message doesn't come to here.
    outgoing_messages = [ "Thanks for showing interest. We try not to keep any data at all, but there are two exceptions you need to know about:", "First, when we make a new tool and want to make sure it's working, we might keep transactions for a few weeks. Even then, we minimize its storage.", "Second, for services where you're asking for something, we pass your details to the people who need those details to fulfill your request.", "If you have questions, email  textbot@chad.org . ❤" ]

    return outgoing_messages, conversation_ends_now

