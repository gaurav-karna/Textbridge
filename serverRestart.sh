# script to restart servers upon redeployment automatically
echo "###---Script to restart servers---###"

echo

# sleep cycles used to allow breakage between commands
# no need to force restarts.
echo "###---Phase 1 of 4---###"
echo -n "Restarting gunicorn daemon"
sleep 1
echo -n "."
sleep 1
echo -n "."
sleep 1
echo "."
# VPS COMMAND - won't work locally.
sudo systemctl daemon-reload
echo "###---Phase 1 of 4 DONE---###"

echo ""

echo "###---Phase 2 of 4---###"
echo -n "Restarting gunicorn server"
sleep 1
echo -n "."
sleep 1
echo -n "."
sleep 1
echo "."
# VPS COMMAND - won't work locally.
sudo systemctl restart gunicorn
echo "###---Phase 2 of 4 DONE---###"

echo ""

echo "###---Phase 3 of 4---###"
echo -n "Performing nginx test"
sleep 1
echo -n "."
sleep 1
echo -n "."
sleep 1
echo "."
# VPS COMMAND - won't work locally.
sudo nginx -t
echo "###---Phase 3 of 4 DONE---###"

echo ""

echo "###---Phase 4 of 4---###"
echo -n "Restarting nginx reverse proxy"
sleep 1
echo -n "."
sleep 1
echo -n "."
sleep 1
echo "."
# VPS COMMAND - won't work locally.
sudo systemctl restart nginx
echo "###---Phase 4 of 4 DONE---###"

echo ""

echo "Successful reboot. Check to make sure with sudo systemctl status [gunicorn/nginx]"