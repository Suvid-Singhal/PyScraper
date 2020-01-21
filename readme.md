# PyScraper
PyScraper is a tool that crawls the given webage and lists all the directories it finds in that page. Thi tool can disclose information about the directories present in the web server and lead to a potential vulnerability.

## What is Directory Listing?
Directory listing is a web server function that displays a list of all the files when there is not an index file, such as index.php and default.asp in a specific website directory.

## How to prevent Directory Listing Attacks?
To prevent the listing of the folder's contents on your server, you should add the following line to the .htaccess file in the folder (if there is no .htaccess file, you can create a new one):
```php
Options -Indexes
```

Also, you should not put any article or information that is publicly visible on your website in the pages that contain your personal information or web server files. In this way, attacker can use directory listing to leak your personal information.
