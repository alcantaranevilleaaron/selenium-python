from behave import given, when, then
from pages.google_homepage import GoogleHomepage


@given("I am on the Google homepage")
def step_impl(context):
    context.home_page = GoogleHomepage(context.browser)
    context.home_page.navigate_to_homepage()


@when('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search_for(search_term)


@then('I should see search results for "{search_term}"')
def step_impl(context, search_term):
    assert search_term in context.home_page.get_title()
