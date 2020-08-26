.globl 		get_minimum

.data
	newline_str:.asciiz "\n"
	 prompt_len: .asciiz "Array length: "
	 prompt_num: .asciiz "Enter num: "
	    min_str: .asciiz "The minimum element in this list is "
	       size: .word 0
		  i: .word 0
		arr: .word 0
    

.text
           
main:      

      la $a0, prompt_len
      addi $v0, $zero, 4
      syscall
      
      addi $v0, $zero, 5
      syscall
      
      sw $v0,size
      lw $t0,size
      la $t1,arr
      lw $t2,i
readNum:

      beq $t0,$t2,endFor
      la $a0, prompt_num
      addi $v0, $zero, 4
      syscall
      

      addi $v0, $zero, 5
      syscall
      
      sw $v0,0($t1)
      addi $t1,$t1,4
      addi $t2,$t2,1
      j readNum
endFor:
      la $t1,arr 

      add $a0, $t1, $zero
      sw $t1, 0($sp) # store it as arg 1 of get_minimum
      jal get_minimum # call get_minimum
      addi $sp, $sp, 4 # remove the argument

      addi $t0, $v0, 0 # Keep track of the result

      # Print the min_str
      addi $v0, $0, 4
      la $a0, min_str
      syscall

      # Print the minimum
      addi $a0, $t0, 0 # $a0 = get_minimum(my_list)
      addi $v0, $0, 1 # $v0 = 1 for printing integer
      syscall

      # print "\n"
      addi $v0, $0, 4 # $v0 = 4 for printing a string
      la $a0, newline_str # $a0 = newline_str for printing a new line
      syscall

      # Exit the program
      addi $v0, $0, 10 # $v0 = 10 for exiting the program
      syscall

get_minimum :
     lw $t0,0($a0) #min_item = the_list[0] here min_item is $t0
     addi $a0,$a0,4 #go to next index value of list_int
     addi $t1, $zero, 1
     lw $a1,size 
     #label for loop
for:     
      bge $t1,$a1,return  #if $t1 >= $a1 than go to return label
      #store byte from address $a0 into $t2
      lw $t2,0($a0)
      #if list item $t2 greater or equal go to else label otherwise
      
      #min_item assign from $t2 to $t0
      slt $s0, $t2, $t0
      beq $s0, $zero, else
      
      add $t0, $t2, $zero
  
else:   
      addi $t1,$t1,1 #incremet i
      addi $a0,$a0,4 #go to next pointer address
      j for #jump to for label
  
  
return :
 #move min_item value($t0) to $v0 which return value
      add $v0, $t0, $zero
      jr $ra #return address from it called in main function