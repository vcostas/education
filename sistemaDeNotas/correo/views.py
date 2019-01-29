from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from sitemessage.messengers.smtp import SMTPMessenger
from sitemessage.messengers.mymessenger import MyMessenger
from sitemessage.models import Dispatch, Message
from sitemessage.shortcuts import schedule_email
from sitemessage.toolbox import schedule_messages, recipients, send_scheduled_messages
from sitemessage.messages.email import EmailHtmlMessage



def index(request):
    return HttpResponse("Hello, {}. Welcome to the sitemessage internal mailbox.".format(request.user.username))

def inbox(request):
    """
    Retrieves all the messages for the logged in user and renders the admin Mailbox template.
    """
    inboxMessagesId = Dispatch.objects.filter(recipient_id=request.user.id)
    inboxMessages = []
    for m in inboxMessagesId:
        msg = Message.objects.get(id=m.message_id)
        inboxMessages.append(msg.context)
    return HttpResponse(inboxMessages)
    # return render(request, 'correo/read-mail.html', context=context)
    
def sent(request):
    """
    Retrives all the messages sent to the logged in user and renders the admin Mailbox template.
    """
    sentMessages = Message.objects.filter(sender_id = request.user.id).values('context')
    return HttpResponse(sentMessages)
    #render(request, 'correo/mailbox.html', {})
    
def compose(request):
    """
    Allows logged in user to write a new message for another user in the system.
    """
    context = {}
    send_messages_view(request, 4)
    return HttpResponseRedirect(reverse('correo:inbox'))
    #render(request, 'correo/compose.html', context=context)


def drafts(request):
    """
    Creates a message and stores it. These messages have not been dispatched yet.
    """
    draftMessages = Message.objects.filter(sender_id = request.user.id).values('context')
    return HttpResponse(draftMessages)
    # render(request, 'correo/mailbox.html', context=context)
    
def junk(request):
    """
    Returns all the messages which are marked deleted by the logged in user.
    """
    context = {}
    render(request, 'correo/mailbox.html', context=context)

def trash(request):
    """
    Returns all the messages which are marked deleted by the logged in user.
    """
    context = {}
    render(request, 'correo/mailbox.html', context=context)

def send_messages_view(request, id):
    """
    Sends an internal email to the desired recipients.
    """
    # We extract the recipient's id.
    
    to_user = User.objects.get(pk=id)
    sender = request.user
    
    # Here we define the smtp recipients to inform them via email that
    # they have an unread notification.
    # my_smtp_recipients = recipients(SMTPMessenger, [to_user.email]),

    # Here we define the internal mail recipients 
    # my_recipients = recipients(MyMessenger, [to_user])
      
    # schedule_email('There is hope.', [to_user, sender.username])
    #schedule_email('You have an unread notification in eduanalytics.',[my_smtp_recipients, sender]
    # schedule_messages('You are awesome VEER.', recipients('mymessenger', ['user1--address', user2]))

    schedule_messages(
    # You can pass one or several message objects:
    [
        # The first param of this Message Type is `subject`. The second a dictionary.  
        EmailHtmlMessage('Congratulations Nancy for your baby', {'title': 'Message to my Sister', 'entry': 'I will stand by you.'}),
        ],

    # The same applies to recipients: add one or many as required:
    recipients(MyMessenger, [to_user,]),
    # It's useful sometimes to know message sender in terms of Django users:
    sender=request.user
    )

    # this function sends all scheduled messages.
    send_scheduled_messages(ignore_unknown_messengers=True, ignore_unknown_message_types=True)
    HttpResponseRedirect(reverse('correo:inbox'))