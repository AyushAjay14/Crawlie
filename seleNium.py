import time
def screenshot(driver , url , ss):
    driver.get(url)

    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    time.sleep(2)
    driver.find_element_by_tag_name('body').screenshot("screenshot" + str(ss) + ".png")
