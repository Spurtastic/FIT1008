.data 
 
 	number:   .word 0
 	text_prompt: .asciiz "Input your integer to be squared: " 
 	newline: .asciiz "\n"
 	result_squared: .word  0
 	
.text
 
  
   
    		la $a0, text_prompt
    		addi $v0, $0, 4
    		syscall 
    		
    		la $a0, newline
    		addi $v0, $0, 4
    		syscall 
    		
    		addi $v0, $0, 5
    		syscall
    		sw $v0, number
    		lw $t0, number
    		
    		mult $t0, $t0
    		mflo $t1
    		sw $t1, result_squared
    		
    		la $a0, ($t1)
    		addi $v0, $0, 1
    		syscall
    		
    		 
 	