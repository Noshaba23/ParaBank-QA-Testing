from playwright.sync_api import sync_playwright


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open ParaBank
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # Enter valid credentials
        page.locator('input[name="username"]').fill("alish")
        page.locator('input[name="password"]').fill("12345")

        # Click Login
        page.get_by_role("button", name="Log In").click()

        # Verify successful login
        page.get_by_role("heading", name="Accounts Overview").wait_for()

        assert "Accounts Overview" in page.locator("body").inner_text()

        print("TC-07 PASS: Valid login was successful.")

        browser.close()


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open ParaBank
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # Enter valid username but incorrect password
        page.locator('input[name="username"]').fill("alish")
        page.locator('input[name="password"]').fill("Wrong@999")

        # Click Login
        page.get_by_role("button", name="Log In").click()

        # Verify error message
        error_message = "The username and password could not be verified."

        page.get_by_text(error_message).wait_for()

        assert error_message in page.locator("body").inner_text()

        print("TC-08 PASS: Invalid login was rejected successfully.")

        browser.close()


def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open ParaBank
        page.goto("https://parabank.parasoft.com/parabank/index.htm")

        # Login
        page.locator('input[name="username"]').fill("alish")
        page.locator('input[name="password"]').fill("12345")
        page.get_by_role("button", name="Log In").click()

        # Verify login
        page.get_by_role("heading", name="Accounts Overview").wait_for()

        # Click Log Out
        page.get_by_text("Log Out").click()

        # Verify logout
        page.get_by_role("heading", name="Customer Login").wait_for()

        assert "Customer Login" in page.locator("body").inner_text()

        print("TC-14 PASS: Logout was successful.")

        browser.close()