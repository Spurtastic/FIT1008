#tutorial 1 

.data
	input_statement: .asciiz "Enter two integers"
	integer_1:  .word 0
	integer_2:  .word 0
	newLine: .asciiz "\n"
	integer_sum: .word 0 
	output_statement: .asciiz "Sum is "
	

.text


	# print("Enter two integers")
	
	la $a0, input_statement
	addi $v0, $0, 4
	syscall 
	
	la $a0, newLine
	addi $v0, $0, 4
	syscall 
	
	# integer1 = int(input())
	addi $v0, $0, 5
	syscall 
	sw $v0, integer_1
	lw $t0, integer_1
	
	# integer2 = int(input())
	addi $v0, $0, 5
	syscall 
	sw $v0, integer_2
	lw $t1, integer_2
	
	#intgerSum 
	
	la $a0, output_statement
	addi $v0, $0, 4
	syscall 
	
	add $t3, $t0, $t1
	la $a0, ($t3)
	addi $v0, $0, 1
	syscall
	
	
	
	
	
	
	