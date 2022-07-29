Deven Maheshwari  
April 4, 2022  
Cybersecurity  
Lab 04 - CTF Walkthrough 

# CTF Walkthrough by Deven Maheshwari

*Task 1* - Log in to tryhackme.  
*Task 2* - Convert the given string from base 64 to decimal. Recognize that the string ends with a ==, which is a quality of base 64 strings (they can be padded a maximum of 2x with a =).   
*Task 3* - Meta refers to the meta data of the given file. Either use the exif tool by installing it with ```sudo apt install exif``` and making sure java is already downloaded or simply use an online exif tool.  
*Task 4* - Since "something is hiding," stegonagraphy, the art of placing secrets within easily accessed files. Use steghide functionality with ```steghide extract -sf path/to/Extinction.jpg```. Install steghide with sudo.   
*Task 5* - This one is less cybersecurity knowledge but rather fun. Highlight the text of task 5.   
*Task 6* - The file is a QR code!   
*Task 7* - Check the file type of hello.hello with ```file hello.hello```. With that, open it using the strings command, which is for ELF files.   
*Task 8* - This one required knowledge of base 58 which only uses alphanumeric characters and ones that do not look like each other since base 58 is commonly used for bitcoin addresses.  
*Task 9* - Rot 13 is a caeser cipher shift of 13 letters. Since 26 (number of letters in the alphabet) is a multiple of 13, it is a special case where both encoding and decoding is done with the same algorithm. This just requires you to solve the caeser cipher, but be careful since rot13 is too simple and therefore not the correct shift. The flag should again begin with THM.  
*Task 10* - Like task 5, you must delve into the dev console and find the flag.  
*Task 11* - View the contents of this png using xxd for hex and plaintext. PNG's commonly have issues in their header so pipe this to head and note that the first 8 bits must be 89504E47. Then open the image.  
*Task 12* - The social media account they are talking about in the blurb is reddit, from the hint.   
*Task 13* - Interesting because the only characters used are +, [], >, -, and . The clue says binaryfuck, which is related to brainfuck.   
*Task 14* - The title exclusive makes reference to the xor function. Also notice how the first string is in base 16 due to the use of the letter f so use hex input for both strings and the output should be in ascii text using this [tool](https://xor.pw/#).  
*Task 15* - Binary walk sounds like binwalk, which is used on binary images to separate files/code within the image file. Use binwalk with the flag -e, that specifies extraction. Then go to the resulting directory and cat the text file.  
*Task 16* - This is similar to task 4 with the use of stegsolve, since the image is not broken and its just a black image, theoretically with something hiding in it. Use stegsolve, download instructions can be found online.  
*Task 17* - Download the image and open it to see if you can do anything with it. Turns out you can since it is a QR code so scan it and listen to soundcloud.  
*Task 18* - The combination of the words "machine" with the date indicate use of the [Wayback Machine](https://archive.org/web/). Input the website and find the correct date.  
*Task 19* - The hint says to look at a vigenere cipher, and that can potentially be deduced by trying different combinations of already constructed crackers on the plaintext tryhackme and the ciphertext MYKAHODTQ{RVG_YVGGK_FAL_WXF}. Usually, flags begin with THM instead of TRYHACKME so try different combinations of those as keys and a pattern will reveal itself.  
*Task 20* - The given string looks normal, and therefore decimal. Play around with convering it into binary and hex and then int ascii and the correct answer will begin with THM.  
*Task 21* - Using Wireshark, which is a network protocol analyzer and in this context can tell you information about the neighbor's WIFI connections and data transfers. Try to find the flag by using the capture tool. One way of doing it is to check for transfered packets with a get request. 
