# Live Hacking Commands

* **John The Ripper**
	* Cracking ZIP/RAR password.
		1. Creating password protected zip/rar file.
		2. Generating the hash of that file.
			1. sudo zip2john ./path-of-zip-file>./path-of-hash-file
		3. Cracking with John The Ripper.
			1. sudo john --format=zip ./path-of-hash-file

	* Cracking Windows Password.
		1. Get SAM and SYSTEM file from `C:\Windows\System32\config` folder.
		2. Genrate & save the hash file out of it.
			1. samdump2 SYSTEM SAM>./path-to-hash-file
			2. john --format=LM --user=<Username> ./path-to-hash-file
			3. john --show --user=<Username> ./path-to-hash-file

	* Cracking MD5 Hashes.
		1. Generate using anu utility.
		2. Save it in a file. `./path-of-hash-file`
		3. Crack it using John The Ripper.
			1. sudo john --format=raw-MD5 ./path-of-hash-file
	
	* *Important Notes*
		1. Path where john store the save password.
			* ~/.john/john.pot
		2. To use custom wordlist.
			* Provide `--wordlist=./path-of-wordlist`

* **Crunch-Wordlist generator.**
	* Genrating Wordlist
		* crunch <min> <max> 
		* Example below
		* crunch 6 6 0123456789abcdef -o 6chars.txt
		* This will generate the wordlist of 6 characters containing letters from 
		* `0123456789abcdef` only.

