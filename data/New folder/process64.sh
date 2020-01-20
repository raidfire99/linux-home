echo Processing Complex64 radar data into plottable data.
echo WARNING THIS COULD TAKE SOME TIME
echo COPYRIGHT JAY @ RF INTERCEPT 2019 
#truncate -s 5600000 test_multi.bin

hexdump -n 64 -v -e '1/4 "%f"  "\n"' test_multi.bin > test_1.dat

sed -i '$d' test_1.dat

sed -i 's/,/./g' test_1.dat


#truncate -s 5600000 test_saw.bin

hexdump  -n 64 -v -e '1/4 "%f"  "\n"' test_saw.bin > test_2.dat

sed -i '$d' test_2.dat

sed -i 's/,/./g' test_2.dat
echo Sleeping until hexdumps are complete

sleep 15
gnuplot plot.plg
