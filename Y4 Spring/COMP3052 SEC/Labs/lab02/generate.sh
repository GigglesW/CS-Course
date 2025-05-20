echo -n "Password" 	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "HELLO"    	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "MYSECRET" 	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "Test1234" 	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "P455w0rd" 	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "GuessMe" 	 | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "S3CuReP455Word" | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "pass1234"       | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "1234pass"       | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "guessme"        | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "GUESSME"        | openssl md5 | cut -c 13-44 | tee -a hashes.txt
echo -n "H4d+"	         | openssl md5 | cut -c 13-44 | tee -a hashes.txt

