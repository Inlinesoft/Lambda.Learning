import smtplib
import datetime
import time
from utilities import email

def lambda_handler(event, context):
    start_process()

def start_process():
    try:
        start_time = datetime.datetime.now()
        time.sleep(60)
        end_time = datetime.datetime.now()
        _email = email.Email()
        is_email_sent = _email.send_mail_using_smtp(
            send_from='kashif.mehali@gmail.com',
            send_to='kashif.ali@hotmail.co.uk',
            subject='A test email from lambda - ' +
                    datetime.datetime.strftime(datetime.datetime.now(), '%a %d-%b-%Y %X'),
            text='A test email from lambda - \r\n' +
                    'Start Time : ' + datetime.datetime.strftime(start_time, '%a %d-%b-%Y %X') + '\r\n' +
                    'End Time : ' + datetime.datetime.strftime(end_time, '%a %d-%b-%Y %X'),
            text_type='html')


        print ("Email sent!")
    except Exception as exp:
        print (f"Something went wrong... : {exp}" )


if __name__ == "__main__":

    print("****************************************************************************************************")
    print("*                                                                                                  *")
    print("*                                        [START] >>> Lambda                                        *")
    print("*                                                                                                  *")
    print("****************************************************************************************************")

    # call the main method
    start_process()

    print("****************************************************************************************************")
    print("*                                                                                                  *")
    print("*                                           [END] >>> Lambda                                       *")
    print("*                                                                                                  *")
    print("****************************************************************************************************")