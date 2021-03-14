#author Ashwin Sarith, 29940478


.data 
	prompt_m:   .asciiz "Please enter integer m"		#the prompt for entering m
	prompt_n:   .asciiz "Please enter integer n"		# the prompt for entering n
	msg_result: .asciiz "The almost pythogorean triple is " #output string
	m: 	    .word 0					#m integer 
	n: 	    .word 0					#n integer
	a: 	    .word 0					#a integer
	b: 	    .word 0					#b integer
	c: 	    .word 0					#c integer
	triple:     .word 0					#triple integer

.text
	lw $t0, m					        #load m in registry 
	addi $t1, $0, 2					        #result the variable from before
	mul $t2, $t0, $t1 
	mul $t3, $t2, $t1
	lw $t4, n
	mul $t5, $t4, $t1
	mul $t6, $t5, $t1
	sub $t7, $t3, $t6
	sw $t7, a
	
	blt $t7, $0, sub
	j endsub 
  
	sub:
		sub $t8, $0, $t7
		sw $t8, a


	endsub:
		lw $t0, m
		lw $t1, n 
		lw $t2, b
		addi $t3, $0, 2
		mul $t4, $t3, $t0
		mul $t5, $t4, $t1
		sw $t5, b
  
	lw $t0, m
	addi $t1, $0, 2
	
	#finding c value
	mul $t2, $t0, $t1 
	mul $t3, $t2, $t1
	lw $t4, n
	
	mul $t5, $t4, $t1
	mul $t6, $t5, $t1
	add $t7, $t3, $t6
	sw $t7, c
  	
  	#result message
	la $a0, result_msg
	syscall
	
	#print result
	lw $a0, triple 
	li $v0, 1
	syscall
  
  	#end program
	li $v0, 10 
	syscall
