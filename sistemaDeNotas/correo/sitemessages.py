from sitemessage.messengers.smtp import SMTPMessenger
from sitemessage.messengers.mymessenger import MyMessenger
from sitemessage.toolbox import register_messenger_objects

# We register our messengers to deliver email messages.
# 1. Our custom messenger
register_messenger_objects(MyMessenger())

# 2. Our smtp messenger
register_messenger_objects(
    SMTPMessenger('user1@host.com', 'user1', 'user1password', host='smtp.host.com', use_tls=True),
    )

