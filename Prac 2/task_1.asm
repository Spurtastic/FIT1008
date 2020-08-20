# author Ashwin Sarith, 29940478

.text				
	main:
	la $a0, printString                                 # the string is loaded into a0 
	li $v0, 4                                           # string in a0 is printed out in i/o terminal, as its 4 bytes for a word
	syscall                                      
	li $v0, 10
	syscall
.data
	printString: .asciiz "I really enjoy MIPS"          # here the label contains a string stored as an asciiz key

