#!/bin/bash

#export SCRIPT_DIR=$(pwd)

echo 'begin script'
cd ~jtritz/bitbucket/ecoach_webapps/mydata14/mts14
svn update
#svn update -r1444 mts.dictionary
source ~jtritz/virtualenv/v1/bin/activate
python ~jtritz/bitbucket/ecoach_webapps/manage.py collectstatic --noinput --settings=mydata14.settings
echo 'end of script'




