#!/bin/sh
# This script will take a single file that needs pushed to a given repo programmatically
# This could be leveraged for self updating repos where needed, not a standard practice
# but useful for applications like, weather tracking from a weather station, gathering
# specifc data for use in the rest of the repository/etc
# This script is given without warranty and with the warning the you SHOULD KNOW WHAT YOU ARE DOING
# before programmatically updating any git based repository with these methods, and is presented here
# as an example.

# Path to local repository
REPO_DIR="/tmp/repo_directory"
STAGING_FILE="/path/to/staging_file" # Path to the specific file that will be commit/pushed
LOG_FILE="/var/log/git_updater.log"

# Navigate to REPO_DIR
cd $REPO_DIR || { echo "[$(date)] Repository not found" >> $LOG_FILE; exit 1; }

# Fetch the latest changes from the repository
echo "[$(date)] Fetching changes from GitHub..." >> $LOG_FILE
git pull origin main || { echo "[$(date)] Git pull failed" >> $LOG_FILE; exit 1; }

# Only run the repo update if the staging file exists
if [ -f "$STAGING_FILE" ]; then
  # Process the staging file and append new entries to manga_list.txt
  echo "[$(date)] Processing the staging file..." >> $LOG_FILE

  # Commit and push changes to GitHub
  echo "[$(date)] Committing changes to GitHub..." >> $LOG_FILE
  git add "$STAGING_FILE"
  if git commit -m "Automated update: Added [$(STAGING_FILE)] to repo."; then
      echo "[$(date)] Commit successful, pushing changes to GitHub..." >> $LOG_FILE
      if git push origin main; then
          echo "[$(date)] Repository updated successfully." >> $LOG_FILE
      else
          echo "[$(date)] Git push failed after successful commit." >> $LOG_FILE
      fi
  else
      echo "[$(date)] Git commit failed, not pushing changes." >> $LOG_FILE
  fi
fi
