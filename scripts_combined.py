import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gamertag = raw_input("Enter PSN\n")

while True:
    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Trials of Osiris
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[4]/option[1]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys('#lfm +2.0 KD player with multiple Lighthouse clears looking to help others! Friend Request and Message me on PSN to join! PSN = ' + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("1st Script Completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Trials of Osiris
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[4]/option[1]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys('#lfm +2.0 KD player with multiple Lighthouse clears looking to help others! Friend Request and Message me on PSN to join! PSN = ' + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("1st Script Completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Iron Banner
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[20]/option[1]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 2 +300's, +2.0 KD player looking for people to join my group. Friend Request and Message me on PSN to join! PSN = " + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(300)
    browser.quit()

    print("Script completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, King's Fall HM Fresh
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[12]/option[9]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 3 for HM FRESH RUN. Must have a mic, know all boss mechanics, and be +300 Light. Friend Request and Message me on PSN to join! PSN = " + gamertag)
    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("Script completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Warpriest CP on HM
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[12]/option[11]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 3 for HM WARPRIEST. Must have a mic, know all boss mechanics, and be +305 Light. Friend Request and Message me on PSN to join! PSN = " + gamertag)
    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("Script completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Golgoroth CP on HM
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[12]/option[12]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 3 for HM GOLGOROTH. Must have a mic, know all boss mechanics, and be +305 Light. Friend Request and Message me on PSN to join! PSN = " + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("Script completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Daughters CP on HM
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[12]/option[13]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 3 for HM DAUGHTERS. Must have a mic, know all boss mechanics, and be +305 Light. Friend Request and Message me on PSN to join! PSN = " + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    print("Script completed at:")
    print datetime.datetime.now()
    print("Opening next script now...\n")

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, Oryx CP on HM
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[12]/option[14]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys("#lfm Need 3 for HM ORYX. Must have a mic, Touch of Malice, know all boss mechanics(No Knight Strategy), and be +305 Light. Friend Request and Message me on PSN to join! PSN = " + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(240)
    browser.quit()

    browser = webdriver.Firefox()
    browser.get('http://destinylfg.net')
    assert 'DestinyLFG.Net | The Original Destiny LFG Site' in browser.title

    # selects ps4 as console and clicks on it via xpath
    ps4_button = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[1]/div[1]/div/a[2]")
    ps4_button.click()

    # finds text field for gamertag and enters in their psn name from user input and other character attributes
    psn_name = browser.find_element_by_xpath(".//*[@id='gamertag-input']")
    psn_name.send_keys(gamertag)
    enter_manually = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[2]/div/div[1]/div[2]/a").click()
    level = browser.find_element_by_xpath(".//*[@id='level-input']")
    time.sleep(2)
    level.send_keys('40')
    time.sleep(2)
    light_level = browser.find_element_by_xpath(".//*[@id='light-input']")
    light_level.send_keys('318')

    # clicks "I have mic" and "Sherpa" buttons
    i_have_mic = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[1]/label/span")
    i_have_mic.click()
    sherpa = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[1]/div[2]/label/span")
    sherpa.click()

    # delay 2 seconds before finding and clicking "Save Guardian" button
    time.sleep(2.5)
    save_guardian = browser.find_element_by_xpath(".//*[@id='guardian-info']/form/div[3]/div[2]/button")
    save_guardian.click()

    # click on "Post My Group"
    post_my_group = browser.find_element_by_xpath("html/body/div[2]/section[3]/div/div[1]/a")
    post_my_group.click()
    time.sleep(1.5)

    # selects PlayStation4 from drop down menu under "Post My Group"
    choose_platform = browser.find_element_by_xpath(".//*[@id='group-platform-select']/option[4]").click()

    # choose activity under "Post My Group". In this case, it's Atheon HM CP
    choose_activity = browser.find_element_by_xpath(".//*[@id='group-activity-select']/optgroup[14]/option[8]").click()

    # finds text field to add notes on finding members
    notes_add = browser.find_element_by_xpath(".//*[@id='group-notes-input']")
    notes_add.send_keys('#lfm I am giving away Atheon CP! Friend Request and Message me on PSN to join! PSN = ' + gamertag)

    # clicks on LFM and then makes LFM post to site
    looking_for_members = browser.find_element_by_xpath(".//*[@id='group-info']/form/div[4]/div/div[1]/div[2]/a").click()
    list_group = browser.find_element_by_xpath(".//*[@id='group-create-button']").click()

    # allows post to remain up for 5 minutes and then quits browser
    time.sleep(300)
    browser.quit()

    print("All scripts completed at:")
    print datetime.datetime.now()
    print("Opening 1st script now...\n")
