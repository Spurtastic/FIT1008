.data 

	g:  .word 123


# def main()
### x = -5 
### y = 0
### z = 230
	#first initialise the values you want within 
.text

main:
	# x
	addi $t0, $0, -5
	sw $t0, -12($fp)
	
	# y
	sw $0, -8($fp)
	
	# z 
	addi $t0, $0, 230 
	sw $t0, -4($fp)
	sw 
	
	
	# y = g+ x 
	lw $t0, g
	lw $t2, -12($fp)
	add $t0, $t0, $t2
	sw $t0, -8($fp)
	
	lw $a0, -8($fp)
	addi $v0, $0, 1
	syscall 
	
	
	addi $v0, $0, 10 
	syscall 
	
	
	
	