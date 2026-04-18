import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.test_data import test_data


@pytest.fixture(scope="function")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


def test_full_flow(setup):
    page = setup

    login = LoginPage(page)
    admin = AdminPage(page)

    # LOGIN
    login.login(test_data["admin_user"], test_data["admin_pass"])
    assert page.locator("text=Dashboard").is_visible()

    # ADMIN MODULE
    admin.go_to_admin()

    # ADD USER
    admin.add_user(
        test_data["username"],
        test_data["password"],
        test_data["employee_name"]
    )
    assert page.locator(f"text={test_data['username']}").is_visible()

    # SEARCH USER
    admin.search_user(test_data["username"])

    # EDIT USER
    admin.edit_user(test_data["username"])

    # DELETE USER
    admin.delete_user(test_data["username"])
    assert page.locator(f"text={test_data['username']}").is_hidden()