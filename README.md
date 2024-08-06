## PDF FILES TRANSLATION
Since I have been working with China, I need to translate text in pdf files, on drawings, without affecting other elements and their shifts

## How to use?

**Google translate has limit 200k requiests per day, consider it!**


1. download [```main.py```](https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/main/main.py) and [```requirements.txt```](https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/main/requirements.txt)
2. ```pip install -r requirements.txt``` in terminal where u saved files from 1.
3. then edit [```main.py```](https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/main/main.py):

https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/16cff1fbe5485d8524ecf408a260ca0cbe053cfc/main.py#L85

You can [add](https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/16cff1fbe5485d8524ecf408a260ca0cbe053cfc/main.py#L85) folder or [change](https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/16cff1fbe5485d8524ecf408a260ca0cbe053cfc/main.py#L85) it (i just add in same directory, because in ./pdf_files **will be created** directory _translated_pdfs_): 

https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/16cff1fbe5485d8524ecf408a260ca0cbe053cfc/main.py#L72

Change ```dest_language``` to any which you need:

https://github.com/oaoaoaoaoammm/PDF-FILES-TRANSLATION/blob/16cff1fbe5485d8524ecf408a260ca0cbe053cfc/main.py#L86

If you don't want to use chinese, you should remove ```font_path="./fonts/NotoSansSC-Light.ttf"```

4. enjoy


**Don't use this translated PDFs as main because somewhere it can be incorrect because of white painting(i have no idea how to change it, so i added comments for fabrics that it may has errors)**


## ISSUES
Please, open issues with bugs, let's improve this code together
