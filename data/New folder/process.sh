echo Processing Complex64 radar data into plottable data.
echo WARNING THIS COULD TAKE SOME TIME
echo COPYRIGHT JAY @RF INTERCEPT 2019 
#truncate -s 5600000 test_multi.bin

hexdump -v -e '1/4 "%f"  "\n"' test_multi.bin > test_multi.dat

sed -i '$d' test_multi.dat

sed -i 's/,/./g' test_multi.dat


#truncate -s 5600000 test_saw.bin

hexdump -v -e '1/4 "%f"  "\n"' test_saw.bin > test_saw.dat

sed -i '$d' test_saw.dat

sed -i 's/,/./g' test_saw.dat

