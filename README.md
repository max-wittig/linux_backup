# linux_backup
Backs up your important directorys in a zip file and uploads it to google drive

# usage  
1. Download gdrive CLI client from `https://github.com/prasmussen/gdrive`
2. Put it in "gdrive_bin" dir
3. Open terminal and run chmod +x gdrive
4. Run it from terminal with `./gdrive about` and complete the auth
5. Create a new dir with `gdrive mkdir DIRNAME`
6. Specify the settings in the config.json file
    - Insert the name of the gdrive binary that you put in the gdrive_bin folder
    - Copy the folder id into the `gdrive_dir_id`
    - Specify the directories you want to have backup up by the tool
    - Set the clean time -> time, when to cleanup old files in unix seconds. Default = 3 weeks
7. Run the tool or add a cronjob for it `/usr/bin/python3 /home/yourname/__main__.py` --> crontab needs complete path!
