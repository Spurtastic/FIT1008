# Author Ashwin Sarith
# this code is built to apply the concept of if conditions expressed by the python code


.data
	prompt_integer1: .asciiz "Enter first: "	# prompt string for the first integer
	prompt_integer2: .asciiz "Enter second: "		# prompt string for the second integer 
	newLine:         .asciiz "\n" 				# new line for ed
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
	lw $t0, int1
	
	# second = int(input("Enter second: "))
	la  $a0 , prompt_integer2
	addi $v0, $0 , 4
	syscall
	
	# This will be the area where the integer is inputed and stored
	addi $v0, $0, 5
	syscall
	sw $v0, int2
	lw $t1,int2
	
	#first > 0 and second >= 0
	if:
		lw $t0, int1			#integer1 imagine 11
		lw $t1, int2			#integer2 imagine 60
		
		
		#at this point the code will branch to elif
		slt $s0, $t0, $zero		# if first<0 then set $s0 to 1
		bne $s0, $zero, elif		# this will show whether the first<0 
		beq $t0, $zero, elif		# here if the first == 0
		
		#second >=0
		slt $s0, $zero, $t1		# if 0<second then set $s0 to 1
		beq $t1, $zero, ifblock		# if second == 0 then this will move to the ifbranch
		beq $s0, 1    , ifblock		# if $s0==1 then (second>0) will be true 
		
		
	
		
	elif:
		# first == second or first < second:
		beq $t0, $t1, elifblock 	# first == second then branch to elif code block
		slt $s0, $t0, $t1		# if (first < second) then set $s0 to 1
		beq $s0, 1  , elifblock		# here if $s0 ==1 then (first<second) is true therefore it will branch to the elif block
	
	
		 
	
	
	
	else:
		b elseblock
		
	ifblock:
		div $t1, $t0
		mflo $t3
		sw $t3, result
		b print
				
	elifblock:
		# result = first * second
		mul $t3, $t0, $t1
		sw $t3, result
		b print
		
		
		
	elseblock:
		# result = second * 2
		mul $t3, $t1, 2
		sw $t3, result
		b print
		
	
	print:
		la $a0, print_result
		addi $v0, $0 , 4
		syscall
		
		la $a0, ($t3)
		addi $v0, $0, 1
		syscall
		
		la $a0, newLine
		addi $v0, $0 , 4
		syscall

		b exit
		
		
	
	exit:
		addi $v0, $0, 10
		syscall
	
