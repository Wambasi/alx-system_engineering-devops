debugging internal server error retured from curl -sI 127.0.0.1
Steps
install tmux so that u can split the terminals sudo apt install tmux
start tmux: type tmux on the terminal
split the terminal into two: ctrl+b then %
to go to the other terminal: ctrl+b then arrow key
type:ps aux to observe the process id for www-data apache2
after getting the process id, trace it using strace -p process id
Then on the other terminal, curl -sI 127.0.0.1
observe the output returned by strace, 0 indicates success -1 indicates error
we see that all the -1 returns files with .phpp instead of .php with the error no such file or directory
check the files in /var/www/html it contains all the wordpress files
vi into the file wp-settings.php
going line by line check the files that has issues with php eg files with .phpp for instance
easier to search in vim is go to escape mode then type this :/.phpp
locate the line and remove the extra p
restart apache2, sudo service apache2 restart
finally write the puppet file
