# Worklog
Stuyvesant Cybersecurity 2022: Final Project

Deven Maheshwari & Jerry Liang

## Log

#### 5/19
**Jerry:** Created file structure and testing main method. Wrote encoder (matches expected output), fixed small bug with PRGA (number of iterations).

**Deven:** Added XOR function, needs tweaking for comparing plaintext and RGA specified values. Ciphertext produced in byte string.

#### 5/20-22
**Jerry:** Commented out extraneous code. Wrote decoder method. Created new encode method that takes file arguments and returns file output (needs to be tested).

**Deven:** Added basic commenting. Also included decoder file method in decoder.py. Will test next
session.

#### 5/23
**Jerry:** Fixed encode method that takes in file arguments and returns file output. Wrote helper KSA_byte function. Tested file encoder and had expected output.

**Deven:** Notes for all functions within encoding. Ran into type errors while testing, looked at byte
types for arrays.

#### 5/24
**Jerry:** Wrote decode method that takes in file arguments and returns file output. Tested file decoder and had expected output.

**Deven:** Configuring makefile and presentation/readme files. Planning out homework activity with NLP.

#### 5/25
**Jerry:** Updated encode and decode to work with makefile. Fixed makefile to have proper instructions.

**Deven:** Completed insecurities file to use bar graphs instead of a line chart. Updated file structure.

#### 5/26
**Jerry:** Updated README and PRESENTATION with correct information and linked more resources.

**Deven:** Added terminal output for encoder and decoder. Tested makefile and worked on lesson plan for the presentation.

#### 5/27-5/30
**Jerry:** Finished presentation and homework assignment.

**Deven:** Created file structure for homework scavenger using bash script run.sh. Testing finished HW assignment. 

## References and Resources
* Wikipedia: (https://en.wikipedia.org/wiki/RC4)
* _A Practical Attack on Broadcast RC4_ by Itsik Mantin and Adi Shamir: (https://link.springer.com/content/pdf/10.1007%2F3-540-45473-X_13.pdf)
* "What is RC4?": (https://www.encryptionconsulting.com/education-center/what-is-rc4/)
* "What Is RC4 and Why Is It A Vulnerability" by Borislav Kiprin: (https://crashtest-security.com/disable-ssl-rc4/)
* Online Encoder/Decoder: (https://www.dcode.fr/rc4-cipher)
