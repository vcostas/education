from django.utils.translation import ugettext as _

from .base import MessengerBase
from ..exceptions import MessengerException


class VKontakteMessengerException(MessengerException):
    """Exceptions raised by VKontakte messenger."""


class VKontakteMessenger(MessengerBase):
    """Implements VKontakte page wall message publishing.

    Uses `requests` module: https://pypi.python.org/pypi/requests
    
    Steps to be done:

    1. Create a user/community page.
    2. Create `Standalone` application at http://vk.com/apps?act=manage
    3. Get your Application ID (under Settings menu item in left menu)
    4. To generate an access token go to using your browser:

        https://oauth.vk.com/authorize?client_id={app_id}&scope=wall,offline&display=page&response_type=token
        &v=5.52&redirect_uri=https://oauth.vk.com/blank.html
        
        * Replace {app_id} with actual application ID.

    5. Copy token from URL in browser (symbols after `access_token=` but before &)
    6. Use this token.

    """
    alias = 'vk'
    title = _('VKontakte')

    _url_wall = 'https://api.vk.com/method/wall.post'

    def __init__(self, access_token):
        """Configures messenger.

        :param str access_token: Unique authentication token to access your VK user/community page.

        """
        import requests

        self.lib = requests
        self.access_token = access_token

    @classmethod
    def get_address(cls, recipient):
        return getattr(recipient, 'vkontakte', None) or recipient

    def _test_message(self, to, text):
        return self._send_message(to, text)

    def _send_message(self, to, text):

        try:
            # Automatically deduce message type.
            message_type = 'attachments' if text.startswith('http') else 'message'

            response = self.lib.post(
                self._url_wall,
                data={
                    message_type: text,
                    'owner_id': to,
                    'from_group': 1,
                    'access_token': self.access_token,
                    'v': '5.73',
                })

            json = response.json()

            if 'error' in json:
                error = json['error']
                raise VKontakteMessengerException('%s: %s' % (error['error_code'], error['error_msg']))

            return json['response']['post_id']  # Returns post ID.

        except self.lib.exceptions.RequestException as e:
            raise VKontakteMessengerException(e)

    def send(self, message_cls, message_model, dispatch_models):
        for dispatch_model in dispatch_models:
            try:
                self._send_message(dispatch_model.address, dispatch_model.message_cache)
                self.mark_sent(dispatch_model)

            except Exception as e:
                self.mark_error(dispatch_model, e, message_cls)
