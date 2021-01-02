# Law Tracker

This code was designed to check track the in/out of legislative projects in the Chilean Upper and Lower Chamber of Congress.

To configure the script, fill the ketwords.txt file with the keywords (in Spanish) of the projects you want to monitor (eg. banco, retail, autos, agua, etc..)

The code will scrape the sites for those keywords and generate a base file with the projects. Subsequent executions of the code will compare against the base file and generate an output.xlsl showing the new, closed and updated projects. The base file will then be updated with the latest scrape.

Enjoy!
