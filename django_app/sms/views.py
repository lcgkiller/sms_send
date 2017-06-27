from django.shortcuts import render

from config import settings
from .forms import smsForm

## cool_sms
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

##

# Create your views here.
def sms_send(request):

    api_key = settings.SMS_KEY
    api_secret = settings.SMS_SECRET

    if request.method == "POST":
        form = smsForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            content = form.cleaned_data['text']
            print("전화번호 :", phone_number, "내용 :", content)

            params = dict()
            params['type'] = 'sms'  # Message type ( sms, lms, mms, ata )
            params['to'] = phone_number  # Recipients Number '01000000000,01000000001'
            params['from'] = '01029953874'  # Sender number
            params['text'] = content  # Message

            cool = Message(api_key, api_secret)

            try:
                response = cool.send(params)
                print("Success Count : %s" % response['success_count'])
                print("Error Count : %s" % response['error_count'])
                print("Group ID : %s" % response['group_id'])

                if "error_list" in response:
                    print("Error List : %s" % response['error_list'])

                else:
                    return render(request, 'ok.html', {'phone_number' : phone_number, 'content' : content})

            except CoolsmsException as e:
                print("Error Code : %s" % e.code)
                print("Error Message : %s" % e.msg)

    else:
        form = smsForm()
    context = {
        'form': form
    }
    return render(request, 'sms_send.html', context)