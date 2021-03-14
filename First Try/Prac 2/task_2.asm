.data
   msg1: .asciiz "Enter first: "
   msg2: .asciiz "Enter second: "
   msg3: .asciiz "Result: "

.text
   #print string
   li $v0, 4
   la $a0, msg1
   syscall
  
   #read int
   li $v0, 5
   syscall
   move $t1, $v0
  
   #print string
   li $v0, 4
   la $a0, msg2
   syscall
  
   #read int
   li $v0, 5
   syscall
   move $t2, $v0
  
if:
   bgt $t1,0, cond2
elif:
   beq $t1, $t2, elifblock
   blt $t1, $t2, elifblock
else:
   mul $t3, $t2, 2
   b print

cond2:
   bge $t2, 0, ifblock
   b elif

ifblock:
   div $t2, $t1
   mflo $t3 #get quotient of integer division
   b print
elifblock:
   mul $t3, $t1, $t2
   b print

print:
   #print string
   li $v0, 4
   la $a0, msg3
   syscall
  
   #print int
   move $a0, $t3
   li $v0, 1
   syscall
exit:
   li $v0, 10
   syscall