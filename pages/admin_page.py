class AdminPage:
    def __init__(self, page):
        self.page = page

    def go_to_admin(self):
        self.page.click("text=Admin")
        self.page.wait_for_selector("text=User Management")

    def add_user(self, username, password, employee, role="Admin", status="Enabled"):
        self.page.click("button:has-text('Add')")
        self.page.wait_for_selector("div.oxd-dialog-container")

        # USER ROLE
        self.page.locator("//label[text()='User Role']/following::div[1]").click()
        self.page.locator(f"//div[@role='listbox']//span[text()='{role}']").click()

        # EMPLOYEE NAME
        emp = self.page.locator("input[placeholder='Type for hints...']")
        emp.fill(employee)
        self.page.locator(f"div[role='option']:has-text('{employee}')").click()

        # STATUS
        self.page.locator("//label[text()='Status']/following::div[1]").click()
        self.page.locator(f"//div[@role='listbox']//span[text()='{status}']").click()

        # USERNAME
        self.page.locator("input[placeholder='Username']").fill(username)

        # PASSWORD
        self.page.locator("input[type='password']").first.fill(password)
        self.page.locator("input[type='password']").last.fill(password)

        # SAVE
        self.page.click("button:has-text('Save')")

        # VALIDATION
        self.page.wait_for_selector(f"text={username}")

    def search_user(self, username):
        self.page.fill("input[placeholder='Username']", username)
        self.page.click("button:has-text('Search')")
        self.page.wait_for_timeout(1000)

        # VALIDATION
        self.page.wait_for_selector(f"text={username}")

    def edit_user(self, username):
        self.page.locator(
            f"//div[@role='row']//div[text()='{username}']/ancestor::tr//button[text()='Edit']"
        ).click()

        self.page.click("button:has-text('Save')")

        # VALIDATION
        self.page.wait_for_selector("text=Successfully Updated")

    def delete_user(self, username):
        self.page.locator(
            f"//div[@role='row']//div[text()='{username}']/ancestor::tr//button[text()='Delete']"
        ).click()

        self.page.click("button:has-text('Yes, Delete')")

        # VALIDATION
        self.page.wait_for_selector("text=Successfully Deleted")