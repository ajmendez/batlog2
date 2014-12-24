date "+%s" >> ~/data/.batlog.dat
/usr/sbin/ioreg -l | egrep "CycleCount|Capacity" >> ~/data/.batlog.dat
echo "$(date '+%s') $(/usr/local/bin/osx-cpu-temp)" >> ~/data/.templog.chargino.dat
