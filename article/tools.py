#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_last_email_from_this_ip(ip_address):
    try:
        if EmailMessage.objects.filter(ip_address=ip_address):
            em = EmailMessage.objects.filter(ip_address=ip_address)[0]
            return em
    except:
        return False

def send_email(name,message,email):
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
