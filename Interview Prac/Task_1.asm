# Author Ashwin Sarith
# only beq bne slt slti

.data
	prompt_integer1: .asciiz "Enter first integer: "	# prompt string for the first integer
	prompt_integer2: .asciiz "enter second: "		# prompt string for the second integer 
	print_result:    .asciiz "Result: " 			# here is were the string that will show at the end of the run 
	result:		 .word 0				# this is where the result will be stored 
	int1:		 .word 0 				# the first integer
	int2:		 .word 0				# the second integer
.text
	# first = int(input("Enter first: "))
	la  $a0 , prompt_integer1
	addi $v0, $0 , 4
	syscall
	
	# This will be the area where the integer is inputed and stored
	addi $v0, $0, 5
	syscall
	sw $v0, int1
	
	# second = int(input("Enter second: "))
	la  $a0 , prompt_integer2
	addi $v0, $0 , 4
	syscall
	
	# This will be the area where the integer is inputed and stored
	addi $v0, $0, 5
	syscall
	sw $v0, int1

	
	
	
	if:
		lw $t1, int1  			# now $t1 is 6
		lw $t2, int2  			# now $t2 is 2
		
		
		slt $s0, $t1, $zero		# if int1 < 0 then we know that $s0 is 1 else it will be 0, i.e. the truth values
		beq $s0, 1, elif		# if the value in $s0 == 1 then it means that int1 < 0 so the code must move to elif
		beq $t1, $zero, elif    	# this is if int1 == 0
		
		
			
		slt $s0, $zero, $t2		# if 0 < int2 then s0 = 1
		beq $t2, $zero, if_block	# if int2 == 0 then go to the ifblock
		beq $s0, 1    , if_block	# if s1==1 then go to ifblock
		
		
		
	# elif first == second or first < second: 
	
	elif:
		beq $t1, $t2, elif_block
		slt $s0, $t1, $t2
		beq $s0, 1, elif_block 
		
		
		
	
	else:
		# result = second * 2
		mul $t3, $t2, 2
		b print
	 
		
	
	if_block:
		# result = second // first
		
		b print
		
	elif_block:
		# result = first * second
		mul $t3, $t1, $t2
		b print
	
	print:
		# print("Result: " + str(result))
		li $v0, 4
		la $a0, print_result
		syscall
		
		lw $t3, result
		li $v0,1
		syscall
	exit:
		addi $v0, $0, 10
		syscall
	
	
	