# DNS Shimir
A python tool to get the best DNS for your machine! At the moment, we are developing it just to improve our programming/git skills but maybe can be a good solution for you.
## Installation
We recommend to install Python 3.10 before used because it is developed with it.

Install the dependencies with this command on repository folder:

`pip install -r requirements.txt`

After this you can start to use it.

## Usage
Basically, the tool will ping 10 times in each DNS given to it, and you have two ways to give these DNS:
+ **Local Verification**: DNS Shimir will ask for your location and after that will get available DNS on it in https://public-dns.info/ website.
+ **Custom Verification**: DNS Shimir will create a text file for you to fill with the DNS you want to check.
 + You just have to fill each line of the text file with an DNS.
 + You can make comments on the text file just putting a `#` in the beginning of line you want to comment.
 
Example of text file for Custom Verification:
```
#My DNS List

1.1.1.1
#200.189.80.43
#200.189.80.5
#200.175.182.139
#143.107.51.2
200.175.5.139
#143.107.253.3
```
>During execution, just DNS on lines 3 and 8 will be verified.