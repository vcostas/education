from .base import MessengerBase

class MyMessenger(MessengerBase):

    # Messengers could be addressed by aliases.
    alias = 'mymessenger'

    # Messenger title to show up in UI
    title = 'Super messenger'

    # If we don't want users to subscribe for messages from that messenger
    # (see get_user_preferences_for_ui()) we just forbid such subscriptions.
    allow_user_subscription = False

    def __init__(self):
        """This messenger doesn't accept any configuration arguments.
        Other may expect login, password, host, etc. to connect this messenger to a service.

        """
    @classmethod
    def get_address(cls, recipient):
        address = recipient
        if hasattr(recipient, 'username'):
            # We'll simply get address from User object `username`.
            address = '%s--address' % recipient.username
        return address


    def before_send(self):
        """We don't need that for now, but usually here will be messenger warm up (connect) code."""

    def after_send(self):
        """We don't need that for now, but usually here will be messenger cool down (disconnect) code."""

    def send(self, message_cls, message_model, dispatch_models):
        """This is the main sending method that every messenger must implement."""

        # `dispatch_models` from sitemessage are models representing a dispatch
        # of a certain message_model for a definite addressee.
        for dispatch_model in dispatch_models:

            # For demonstration purposes we won't send a dispatch anywhere,
            # we'll just mark it as sent:
            self.mark_sent(dispatch_model)  # See also: self.mark_failed() and self.mark_error().




