from facebook_scraper import get_profile, set_proxy
import time
import csv

# http://{user}:{password}@{proxy address}:{port}
# set_proxy()

row = ['id', 'mail', 'FB', '名稱', '大頭貼', '教育', '現居', '性別', '生日', '感情狀態']
outputFile = open('fb.csv', 'a')
mailInputFile = open("mail", 'r')
count = 0
sleepTime = 30

with outputFile:
    writer = csv.writer(outputFile)    
    writer.writerow(row)
    for line in mailInputFile:
        try:
            userMail = line.strip()
            count += 1
            print("Count", count, ":", userMail)
            userName = userMail.split("@")[0]                            
            fb_url = "https://www.facebook.com/" + userName
            userProfile = get_profile(userName, cookies="cookies.json")
            print(userProfile)
            id = userProfile.get('id')
            name = userProfile.get('Name')
            profilePicture = userProfile.get("profile_picture")
            education = userProfile.get('Education')
            placesLived = userProfile.get('Places Lived')
            basicInfo = userProfile.get('Basic Info')
            if basicInfo != "":
                basicInfo = userProfile.get('基本資料')

            # GET BASIC INFO
            birthday = ''
            gender = ''
            if basicInfo != "":
                basicInfoSplit = basicInfo.split("\n")
                # print(basicInfoSplit)            
                isBirthdayExists = 'Birthday' in basicInfoSplit
                if isBirthdayExists:
                    pos = basicInfoSplit.index('Birthday') 
                    birthday = basicInfoSplit[pos-1]
                isBirthdayExists = '生日' in basicInfoSplit
                if isBirthdayExists:
                    pos = basicInfoSplit.index('生日') 
                    birthday = basicInfoSplit[pos-1]

                isGenderExists = 'Gender' in basicInfoSplit
                if isGenderExists:
                    pos = basicInfoSplit.index('Gender') 
                    if pos == 0:
                        pos += 1
                    gender = basicInfoSplit[pos-1]            
                isGenderExists = '性別' in basicInfoSplit
                if isGenderExists:
                    pos = basicInfoSplit.index('性別') 
                    if pos == 0:
                        pos += 1
                    gender = basicInfoSplit[pos-1]

            relationship = userProfile.get('Relationship')
            if not relationship:
                relationship = userProfile.get('感情狀況')
            
            # row = ['id', 'mail', 'FB', '名稱', '大頭貼', '教育', '現居', '性別', '生日', '感情狀態']
            outputRow = [id, userMail, fb_url, name, profilePicture, education, placesLived, gender, birthday, relationship]            
            print(outputRow)
            writer.writerow(outputRow)
        except Exception as e:
            print('Error:', fb_url)
            print(e)   
        time.sleep(sleepTime)
        # break

mailInputFile.close