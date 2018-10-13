import os
import nexmo


NEXMO_API_KEY = os.environ['NEXMO_API_KEY']
NEXMO_SECRET_KEY = os.environ['NEXMO_SECRET_KEY']

client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_SECRET_KEY)


def send_verification(number_to_verify):
    print('sending text with verification code')
    response = client.start_verification(number=number_to_verify,
            brand='Telephone')

    print('status = ', response['status'])

    if response['status'] == '0':
      print('Started verification request_id=' + response['request_id'])
    else:
      print('Error:', response['error_text'])

    return response['request_id']


def get_verification_code():
    return input("What is your verification code? ")


def check_verification(request_id, user_code):
    check_verification = client.check_verification(request_id, code=user_code)

    if check_verification['status'] == '0':
        print('User verification complete!')


if __name__ == "__main__":
    number_to_verify = str(input("What is your telephone number (with 44 on the
    front, please)? ")
    request_id = send_verification(number_to_verify)
    user_code = get_verification_code()
    check_verification(request_id, user_code)

