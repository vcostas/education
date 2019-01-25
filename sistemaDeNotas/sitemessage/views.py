from django.contrib.staticfiles.templatetags.staticfiles import static as get_static_url
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from sitemessage.exceptions import UnknownMessageTypeError
from sitemessage.models import Dispatch
from sitemessage.signals import sig_unsubscribe_failed, sig_mark_read_failed
# from sitemessage.toolbox import schedule_messages, recipients
from sitemessage.shortcuts import schedule_email

from sitemessage.toolbox import recipients, send_scheduled_messages
from sitemessage.messengers.smtp import SMTPMessenger
from sitemessage.messengers.mymessenger import MyMessenger


def _generic_view(message_method, fail_signal, request, message_id, dispatch_id, hashed, redirect_to=None):

    if redirect_to is None:
        redirect_to = '/'

    try:
        dispatch = Dispatch.objects.select_related('message').get(pk=dispatch_id)

        if int(message_id) != dispatch.message_id:
            raise ValueError()

        message = dispatch.message

    except (Dispatch.DoesNotExist, ValueError):
        pass

    else:

        try:
            message_type = message.get_type()
            expected_hash = message_type.get_dispatch_hash(dispatch_id, message_id)

            method = getattr(message_type, message_method)

            return method(
                request, message, dispatch,
                hash_is_valid=(expected_hash == hashed),
                redirect_to=redirect_to
            )

        except UnknownMessageTypeError:
            pass

    fail_signal.send(None, request=request, message=message_id, dispatch=dispatch_id)

    return redirect(redirect_to)


def unsubscribe(request, message_id, dispatch_id, hashed, redirect_to=None):
    """Handles unsubscribe request.

    :param Request request:
    :param int message_id:
    :param int dispatch_id:
    :param str hashed:
    :param str redirect_to:
    :return:
    """
    return _generic_view(
        'handle_unsubscribe_request', sig_unsubscribe_failed,
        request, message_id, dispatch_id, hashed, redirect_to=redirect_to
    )


def mark_read(request, message_id, dispatch_id, hashed, redirect_to=None):
    """Handles mark message as read request.

    :param Request request:
    :param int message_id:
    :param int dispatch_id:
    :param str hashed:
    :param str redirect_to:
    :return:
    """
    if redirect_to is None:
        redirect_to = get_static_url('img/sitemessage/blank.png')

    return _generic_view(
        'handle_mark_read_request', sig_mark_read_failed,
        request, message_id, dispatch_id, hashed, redirect_to=redirect_to
    )


def index(request):
    return HttpResponse("Hello, {}. You're at the sitemessage index.".format(request.user.username))
def inbox(request):
    return HttpResponse("Hello, {}. You're at the sitemessage INBOX!.".format(request.user.username))
def sent(request):
    return HttpResponse("Hello, {}. You're at the sitemessage SENT!.".format(request.user.username))
def compose(request):
    return HttpResponse("Hello, {}. You're at the sitemessage COMPOSE!.".format(request.user.username))
def drafts(request):
    return HttpResponse("Hello, {}. You're at the sitemessage DRAFTS!.".format(request.user.username))
def junk(request):
    return HttpResponse("Hello, {}. You're at the sitemessage JUNK!.".format(request.user.username))
def trash(request):
    return HttpResponse("Hello, {}. You're at the sitemessage TRASH!.".format(request.user.username))

def send_messages_view(request, id):
    """
    Sends an email to the desired recipients.
    """
    # Suppose `user_model` is a recipient User Model instance.
    
    to_user = User.objects.get(pk=id)
    sender = request.user

    # Here we define the smtp recipients to inform them via email that
    # they have an unread notification.
    my_smtp_recipients = recipients(SMTPMessenger, [to_user.email]),

    # Here we define the internal mail recipients 
    my_recipients = recipients(MyMessenger, [to_user])
    
       
    
    schedule_email('There is hope.', [to_user, request.user])
    schedule_email('You have an unread notificatoin in eduanalytics.',[my_smtp_recipients, sender])
    