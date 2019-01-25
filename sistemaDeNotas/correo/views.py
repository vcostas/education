from django.shortcuts import render
from django.http import HttpResponse
# from sitemessage.toolbox import schedule_messages, recipients
# from sitemessage.shortcuts import schedule_email
# from sitemessage.toolbox import recipients, send_scheduled_messages
from sitemessage.messengers.smtp import SMTPMessenger
from sitemessage.messengers.mymessenger import MyMessenger

from sitemessage.models import Dispatch, Message
from django.contrib.auth.user import User
# Create your views here.


def index(request):
    return HttpResponse("Hello, {}. Welcome to the sitemessage internal mailbox.".format(request.user.username))

def inbox(request):
    """
    Retrieves all the messages for the logged in user and renders the admin Mailbox template.
    """
    inboxMessages = Dispatch.objects.filter(recipient_id=request.user.id)
    
    return HttpResponse("Hello, {}. You have sent the following messages {}.".format((request.user.username, inboxMessages)))
    
def sent(request):
    """
    Retrives all the messages sent to the logged in user and renders the admin Mailbox template.
    """
    sentMessages = Message.objects.filter(sender = request.user.id)

    return HttpResponse("Hello, {}. You have sent the following messages {}.".format((request.user.username, sentMessages)))

def compose(request):
    """
    Allows logged in user to write a new message for another user in the system.
    """

    return HttpResponse("Hello, {}. You're at the sitemessage COMPOSE!.".format(request.user.username))

def drafts(request):
    """
    Creates a message and stores it. These messages have not been dispatched yet.
    """

    return HttpResponse("Hello, {}. You're at the sitemessage DRAFTS!.".format(request.user.username))

def junk(request):
    """
    Returns all the messages which are marked deleted by the logged in user.
    """
    return HttpResponse("Hello, {}. You're at the sitemessage JUNK!.".format(request.user.username))

def trash(request):
    """
    Returns all the messages which are marked deleted by the logged in user.
    """
    return HttpResponse("Hello, {}. You're at the sitemessage TRASH!.".format(request.user.username))

def send_messages_view(request, id):
    """
    Sends an internal email to the desired recipients.
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
    