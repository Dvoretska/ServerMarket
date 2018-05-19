import json

from behave import given, when, then

from applications.accounts.models import UserProfile


@given('{username} user with {email} and {password}')
def user_creation(context, username, email, password):
    UserProfile.objects.create_user(username=username, email=email, password=password)


@when('user login with {email} and {password}')
def login(context, email, password):
    context.response = context.test.client.post(
        context.get_url('accounts:account_login'), {'email': email, 'password': password}
    )


@then('we have {data} in response')
def data_in_response(context, data):
    context.test.assertIn(data, json.loads(context.response.content))


@then('we have {error} error with {data}')
def errors_in_response(context, error, data):
    context.test.assertEqual(data, json.loads(context.response.content).get(error)[0])


@then('status code will be {status_code}')
def status_code_in_response(context, status_code):
    context.test.assertEqual(int(status_code), context.response.status_code)
