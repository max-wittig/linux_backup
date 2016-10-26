# linux_backup
Backs up your important directorys in a zip file and uploads it to google drive

# usage  
1. Download gdrive CLI client from `https://github.com/prasmussen/gdrive`
2. Put it in "gdrive_bin" dir
3. Run it from terminal with `./gdrive about` and complete the auth
4. Create a new dir with `gdrive mkdir DIRNAME`
5. Copy the folder id into the config json `gdrive_dir_id`
6. Specifiy the directories you want to have backup up by the tool
7. Run the tool or add a cronjob for it `python3 __main__.py`
