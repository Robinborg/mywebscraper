'''websraper'''
Input website to search with selenium
Open website
Search website for emails on fronpage
print emails to .txt
   Search the website for contactpage, info, about us etc.
        loop for a href 
        match them to  contactpage, info, about us etc.
        Open site
            loop for emails
            print emails to a .txt
Search for the inquiry email







Tech with Tim tutorial
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
#     )
#     element.clear()
#     element.click()
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "sow-button-19310003"))
#     )
#     element.click()

#     driver.back()
#     driver.back()
#     driver.back()
#     driver.forward()
#     driver.forward()
#     driver.forward()
# except:
#     driver.quit()

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-title")
#         print(header.text)


# finally:
#     driver.quit()


# print(main.text)
