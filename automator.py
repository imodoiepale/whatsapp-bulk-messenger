from playwright.sync_api import sync_playwright

def open_whatsapp_web():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://web.whatsapp.com/")
        
        page.get_by_role("button", name="Link with phone number", exact=True).click()
        page.get_by_label("Type your phone number.").click()
        page.get_by_label("Type your phone number.").fill("+254 743 854888")
        page.get_by_role("button", name="Next").click()

        # Wait for the div element to appear (optional)
        page.wait_for_selector("div[aria-details='link-device-phone-number-code-screen-instructions']")

        # Get the div element
        data_link_code_element = page.query_selector("div[aria-details='link-device-phone-number-code-screen-instructions']")

        if data_link_code_element:
            # Get the data-link-code attribute value
            data_link_code_value = data_link_code_element.get_attribute("data-link-code")

            if data_link_code_value:
                print(f"get_data_link_code: {data_link_code_value}")
            else:
                print("data-link-code attribute not found or empty.")
        else:
            print("Div element with aria-details='link-device-phone-number-code-screen-instructions' not found.")
        
        # Prompt for user confirmation
        confirmation = input("Have you input the code on your phone? (yes/no): ")
        if confirmation.lower() == "yes":
            page.get_by_role("textbox", name="Search input textbox").fill("⊙ (You)")
            
            # Find the element with translateY(72px) style attribute value
            element = page.query_selector('div[style="transform: translateY(72px);"]')

            if element:
                # Click on the element
                element.click()
            else:
                print("Element not found")
                
            page.get_by_role("textbox", name="Type a message").fill("Hi James, Master Developer")
            page.get_by_label("Send").click()

        page.wait_for_timeout(0)
        page.close()

if __name__ == "__main__":
    open_whatsapp_web()
