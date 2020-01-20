echo Processing FLOAT32 radar data into plottable data.
echo WARNING THIS COULD TAKE SOME TIME
echo COPYRIGHT JAY @ RF INTERCEPT 2019 
#truncate -s 5600000 radar.bin

hexdump  -v -e '1/4  "%f" "\n"' radar.bin > radar.dat

#sed -i '$d' radar.dat

#sed -i 's/,/./g' radar.dat

echo Sleeping until hexdumps are complete

sleep 15


gnuplot plot.plg

