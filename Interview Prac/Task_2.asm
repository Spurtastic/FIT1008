#Author Ashwin Sarith
# here the an array input size is recieved

.data
	size_prompt: .asciiz "Array Length: "				# the prompt for recieving the input size
      number_prompt: .asciiz "Enter num: " 				# prompt to recieve the integers for input
         min_str: .asciiz "The minimum element in this list is " 	# prompt to show the min item in the list 
            newline_str: .asciiz "\n" 
               size: .word 0 						# the value for size to be stored here
           the_list: .word 0 						# the is the list itself, where the inputed values will be stored
              	min: .word 0						# this is where the min value will be stored for return later 
               	  i: .word 0						# the index to be used in the forloop later on
               item: .word 0 						# the item that the for loop will be retrieving from the list
     

.text
	# size = int(input("Array length: "))
	la $a0, size_prompt						# "Array length: "
	addi $v0, $0, 4							# to print the string in a0
	syscall
	
	addi $v0, $zero, 5						# this is to place the instruction recieve input into v0
	syscall								# the instruction in v0 is executed
	sw $v0, size							# the value in $v0 is stored in label size
	
	
	
	# the_list = [None] * size
	addi $v0, $0, 9							# this is to place the instrucion to allocate memory in the v0 register
	lw $t0, size							# the value is then loaded to t0
	mul $t1, $t0, 4							# this is where t1 = size * 4 to initialise array length the size of one element in the array is 4 bytes 
	addi $a0, $t1, 4						# here the eq to determine array[k], so start + (size*k) 
	syscall
	sw $v0, the_list						# v0 is stored in array 
	sw $t0, ($v0) 							# and the contents of v0 are loaded to $t0 which is basically the length of the_list
	
	# for i in range(len(the_list)):
	addi $t0, $0, 0							# here the register t0 is set to zero to later be stored in i
	sw $t0, i							# this is to store in i to be called up later for implementation in the for loop 
	for:
		# the code here represents the len(the_list) and the exit condition
		lw $t0, i						# this the index
		lw $t1, size						# this size
		beq $t0, $t1, for_exit					# if the index i equates to the size of the list, then the loop will exit
		
		#  "Enter num: "
		la $a0, number_prompt					# printing "Enter num" from label number_prompt 
		addi $v0, $0, 4
		syscall
		
		
		#the_list[i] =int(input("Enter num: "))
		lw $t0, i
		lw $t1, the_list
		mul $t0, $t0, 4
		add $t0, $t0, $t1
		addi $v0, $0, 5						# to read integer input into v0 
		syscall
		sw $v0, 4($t0)						# the value is then stored in the head i.e. the_list[i]
		
		
		
			
			
		
		#i= i+1
		lw $t0, i
		addi $t0, $t0, 1
		sw $t0, i 
		
		j for
		
	for_exit:

	# if i == 0 or min_item > the_list[i]:
	if:
    	lw $t0, size					# $t0 = size
    	slt $s0, $t0, $0
    	beq $s0, 1, exitIf				# if $s0 == 1, skip to else
    	beq $t0, 0, exitIf
    	
    	
    	# min = the_list[0]
    	addi $t0, $0, 0
    	lw $t1, the_list				# $t1 = the_list
    	add $t0, $t0, $t1				# $t0 = (0 * 4) + the_list = 0 + the_list
    	lw $t2, 4($t0)					# $t2 = the_list[0]
    	sw $t2, min					# min = the_list[0]
    	
    	# for i in range(1, size)
    	
    	# i = 1
    	addi $t0, $0, 1
    	sw $t0, i					# i = 1
    	for1:
    		lw $t0, i				# $t0 = i
    		lw $t1, size				# $t1 = size
    		beq $t0, $t1, exitFor1			# if i == size, exit loop
    		
    		# item = the_list[i]
    		lw $t0, i				# $t0 = i
    		lw $t1, the_list			# $t1 = the_list
    		sll $t0, $t0, 2				# $t0 = i * 4
    		add $t0, $t0, $t1			# $t0 = (i * 4) + the_list
    		lw $t2, 4($t0)				# $t2 = the_list[i]
    		sw $t2, item				# item = the_list[i]
    		
    		# if min > item:
    		if1:
    			lw $s0, item			# $s0 = item
    			lw $s1, min			# $s1 = min
    			slt $s2, $s0, $s1		# if item > min, $s2 = 1
    			beq $s2, 0, exitIf1		# if $s2 == 0, exit if1
    			beq $s0, $s1, exitIf1		# if min = item, branch to exitIf1
    			
    			# min = item
    			lw $s0, item			# $s0 = item	
    			sw $s0, min			# min = $s0
    			
    		exitIf1:
    		
    		lw $t0, i				# $t0 = i
    		addi $t0, $t0, 1			# $t0 = i + 1
    		sw $t0, i				# i = i + 1
    		
    		j for1					# jump to start of for1
    		
    	exitFor1:
    	
	# print("\n")
    	
    	la $a0, newline_str				# $a0 = "\n"
    	addi $v0, $0, 4
    	syscall						# Execute

    	# print("The minimum element in this list is " + str(min) + "\n")
    	
    	# print("The minimum element in this list is ")
    	
    	la $a0, min_str					# stores prompt for min to $a0
    	addi $v0, $0, 4
    	syscall						# Execute
    
    	# print(str(min))
    
    	lw $a0, min					# stores min integer in $a0
    	addi $v0, $0, 1
    	syscall						# Execute
    	
	# print("\n")
    	
    	la $a0, newline_str				# $a0 = "\n"
    	addi $v0, $0, 4
    	syscall						# Execute
    	
    	exitIf:
    	


	exit:
		addi $v0, $0, 10
		syscall
	
	
		
		
		
		
	
	
	
	
	
	
	
	
