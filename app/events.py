import logging

from django.conf import settings
from django.core.mail import mail_managers, send_mail, send_mass_mail

from twilio.rest import Client as TwilioClient

log = logging.getLogger(__name__)

_sms_client = None

def strip_lines(lines):
    return '\n'.join(line.lstrip() for line in lines.split('\n'))

def sms_client():
    global _sms_client
    if _sms_client is None and settings.TWILIO_ACCOUNT_SID:
        _sms_client = TwilioClient(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN)

    return _sms_client


def new_user_created(member):
    user = member.user
    mail_managers(
        f'New user {user.username} registered at T13 web',
        strip_lines(f'''Hej admin!

        '{user.first_name} {user.last_name}' har precis registrerat sig på  Team 13's webbapplikation.

        Go to https://macke.eu.pythonanywhere.com/admin/auth/user/{user.id}/change/'
        för att kolla status och se om de är legitima, samt justera deras status om det behövs

        mvh,
        /Team13's aktivitetswebb
        '''))


def adr_approved(adr):
    log.info(f"ADR {adr} has been approved")

    if settings.DEFAULT_FROM_EMAIL:
        log.info("Sending email to " + adr.member.user.email)
        send_mail('Avbokning godkänd',
            strip_lines(f'''Hej {adr.member.fullname}

            Din önskan om avbokning från {adr.activity}
            har blivit godkänd av {adr.approver.fullname}.

            mvh
            /Team13 aktivitetswebb'''),
            settings.DEFAULT_FROM_EMAIL,
            [adr.member.user.email])

    sms_target = adr.member.phone_number
    body = f"Din begäran om avbokning av {adr.activity} har blivit godkänd. mvh /Team13",
    log.info(f"About to send SMS to {sms_target}: {body}")

    if sms_target is None:
        log.warning(f"No phone_number set for {adr.member}")
    elif sms_client():
        log.info(f"Sending SMS to {sms_target}")
        sms_client().messages.create(
            body=body,
            from_=settings.SMS_FROM_NUMBER,
            to=sms_target)
    else:
        log.warning("SMS is disabled")

def adr_rejected(adr):
    log.info(f"ADR {adr} has been rejected,")

    if settings.DEFAULT_FROM_EMAIL:
        recipients = [adr.member.user.email, adr.approver.user.email]
        log.info(f"Sending email to {recipients}")
        send_mass_mail('Avbokning ej godkänd',
            strip_lines(f'''Hej {adr.member.fullname},

            Din önskan om avbokning från {adr.activity}
            har tyvärr blivit avvisad av {adr.approver.fullname} ({adr.approver.user.email})
            med följande meddelande:\n\n"{adr.reject_reason}"

            Vänligen tag kontakt om du har frågor.

            mvh
            /Team13 aktivitetswebb'''),
            settings.DEFAULT_FROM_EMAIL,
            recipients)

    sms_target = adr.member.phone_number
    body = f"Hej! Din begäran om avbokning från {adr.activity} har tyvärr avvisats. mvh /Team13"
    log.info(f"About to send SMS to {sms_target}: {body}")

    if not sms_target:
        log.warning(f"No phone_number set for {adr.member}")
    elif sms_client():
        log.info(f"Sending SMS to {sms_target}")
        sms_client().messages.create(
            body=body,
            from_=settings.SMS_FROM_NUMBER,
            to=sms_target)
    else:
        log.warning("SMS is disabled")


def notify_upcoming_activity(activity):
    if activity.assigned is None:
        # TODO: Notify event coordinator/responsible with summary in this case?
        log.warning(f"Activity '{activity}' is not assigned, cannot notify")
        return

    log.info(f"Notifying {activity.assigned} that they are assigned to {activity}, which occurs soon.")

    message = strip_lines(f'''Hej!

        Här kommer en påminnelse om att du är inbokad på uppgiften {activity}
        den {activity.date} mellan {activity.start_time} och {activity.end_time}.

        mvh /Team13''')

    if settings.DEFAULT_FROM_EMAIL:
        send_mail(f"Påminnelse om {activity}",
            message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[activity.assigned.user.email])

    sms_target = activity.assigned.phone_number
    log.info(f"About to send SMS to {sms_target}: {message}")

    if not sms_target:
        log.warning(f"No phone_number set for {activity.member}")
    elif sms_client():
        log.info(f"Sending SMS to {sms_target}")
        sms_client().messages.create(
            body=message,
            from_=settings.SMS_FROM_NUMBER,
            to=sms_target)
    else:
        log.warning("SMS is disabled")


def send_verification_email(member):
    link = f"https://macke.eu.pythonanywhere.com/api/verify/email/check/{member.email_verification_code}"

    if settings.DEFAULT_FROM_EMAIL:
        log.info(f"Sending verification link to {member.email}:\n{link}")
        send_mail(subject='Team13 email verification',
            message=strip_lines(f'''Hej {member.fullname},

            Klicka på länken för att verifiera din emailadress:

            {link}

            mvh
            /Team13'''),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member.email])
    else:
        log.info(f"Email disabled, verification link for {member.email}:\n{link}")