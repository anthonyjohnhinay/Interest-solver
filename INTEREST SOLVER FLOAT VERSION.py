import math
from datetime import date
rp = 'y'
while rp == 'y' or rp == 'yes':
	print('''  
	               
 |_ _| \| |_   _| __| _ \ __/ __|_   _|
  | || .` | | | | _||   / _|\__ \ | |  
 |___|_|\_| |_|_|___|_|_\___|___/ |_|  
 / __|/ _ \| |\ \ / / __| _ \          
 \__ \ (_) | |_\ V /| _||   /          
 |___/\___/|____\_/ |___|_|_\          
                                       ''')
	print('''=============CHOOSE OPERATION BELOW============
************************************************	
	        [1] TO COMPUTE FINAL AMOUNT
	        [2] TO COMPUTE INTEREST
	        [3] TO COMPUTE PRINCIPAL
	        [4] TO COMPUTE TIME
	        [5] TO COMPUTE RATE
	        [6] TO COMPUTE ORDINARY INTEREST''')
	a = input('operation ==> ')
	if a == '1':
		print('===COMPUTING FINAL AMOUNT===')
		try:
			p = float(input('PRINCIPLE AMOUNT: '))
			rate = float(input('RATE(%): '))
			r = (rate / 100)
			ti = float(input('TIME IN MONTHS: '))
			t = (ti / 12)
			f = (p * (1 + r * t))
			print('Final Amount is ====> %s' %f)
		except ValueError:
			print('Wrong Input please retry again')
			continue
	elif a == '2':
		print('====COMPUTING INTEREST====')
		try:
			p = float(input('PRINCIPAL: '))
			rate = float(input('RATE(%): '))
			r = (rate / 100)
			ti = float(input('TIME IN MONTHS: '))
			t = (ti / 12)
			i = (p * r * t)
			print('Interest is %s' %i)
		except ValueError:
			print('Wrong Input please retry again')
			continue
	elif a == '3':
		print('====COMPUTING PRINCIPAL====')
		try:
			i = float(input('INTEREST: '))
			ra = float(input('RATE(%): '))
			r = (ra / 100)
			ti = float(input('TIME IN MONTHS: '))
			t = (ti / 12)
			p = i / (r * t)
			print('Principal is %s' %p)
		except ValueError:
			print('Wrong Input please retry again')
			continue
	elif a == '4':
		print('====COMPUTING TIME======')
		try:
			p = float(input('PRINCIPLE AMOUNT: '))
			rate = float(input('RATE(%): '))
			r = (rate / 100)
			i = float(input('INTEREST: '))
			t = i / (p * r)
			print('Time is %s' %t)
		except ValueError:
			print('Wrong Input please retry again')
			continue
	elif a == '5':
		print('====COMPUTING RATE======')
		try:
			p = float(input('PRINCIPLE AMOUNT: '))
			i = float(input('INTEREST: '))
			ti = float(input('TIME IN MONTHS:'))
			t = ti / 12
			r1 = p * t
			r = i / r1
			print('Rate is %s' %r)
		except ValueError:
			print('Wrong Input please retry again')
			continue
					
			
			
			
	elif a == '6':
		print('====COMPUTING ORDINARY INTEREST====')
		print('WARNING USED ONLY WHEN QUETION COMPOUND')
		try:
			p = int(input('PRINCIPLE AMOUNT: '))
			rate = float(input('RATE(%): '))
			r = (rate / 100)
			print(''' CHOOSE YOUR MODE OF TIME
			     [A] if Actual Time
			     [B] if Approximate Time''')
			pk = input('TYPE OF TIME: : ')
			if pk == 'B' or pk == 'b':
			  print('APPROX TIME')
			  print('==========================')
			  d = float(input('NUMBER OF APPROX DATE: '))
			  t = (d / 360) * (p * r)
			  print(f'ORDINARY INTEREST IS {t}')
			  	
			
			elif pk == 'A' or pk == 'a':
			  print('ACTUAL TIME')
			  print('PLEASE USE THE FORMAT YYYY, M, D')
			  y, m, d = map(int, input('FIRST DATE: ').split(','))
			  f_date = date(y, m, d)
			  y, m, d = map(int, input('SECOND DATE: ').split(','))
			  l_date = date(y, m, d)
			  delta = l_date - f_date
			  num = delta.days
			i1 = (p * r)
			i2 = (num / 360)
			i = i1 * i2
		 
		  	
		
		
	
			print(f'The Ordinary Interest is {i}')	
		except:
			print('Wrong Input please retry again')
	elif a == '7':
		print('====COMPUTING EXACT INTEREST====')
		print('WARNING USED ONLY WHEN QUETION COMPOUND')
		try:
			p = int(input('PRINCIPLE AMOUNT: '))
			rate = float(input('RATE(%): '))
			r = (rate / 100)
			print(''' CHOOSE YOUR MODE OF TIME
			     [A] if Actual Time
			     [B] if Approximate Time''')
			pk = input('TYPE OF TIME: : ')
			if pk == 'B' or pk == 'b':
			  print('APPROX TIME')
			  print('==========================')
			  d = float(input('NUMBER OF APPROX DATE: '))
			  t = (d / 365) * (p * r)
			  print(f'ORDINARY INTEREST IS {t}')
			  	
			
			elif pk == 'A' or pk == 'a':
			  print('ACTUAL TIME')
			  print('PLEASE USE THE FORMAT YYYY, M, D')
			  y, m, d = map(int, input('FIRST DATE: ').split(','))
			  f_date = date(y, m, d)
			  y, m, d = map(int, input('SECOND DATE: ').split(','))
			  l_date = date(y, m, d)
			  delta = l_date - f_date
			  num = delta.days
			i1 = (p * r)
			i2 = (num / 365)
			i = i1 * i2
		 
			
	
			print(f'The Ordinary Interest is {i}')	
		except:
			print('Wrong Input')
			
			
			
			
	#Simple Annuity Solver
	elif a == '9':
			print('====ANNUITY SOLVER====')
			print('[A] To Input Final / Future value')
			print('[B] To Input Present Value')
			print('[C] To find PERIODIC PAYMENT(FV ONLY)')
			print('[D] To find PERIODIC PAYMENT (PV ONLY)')
			chk = input('Please Input your operation: ')
			if chk == 'A' or chk == 'a':
			 try:
			 	print('/////Annuity Final Value//////')
			 	p = float(input('PERIODIC PAYMENT: '))
			 	tt  = float(input('TIME IN MONTHS: '))
			 	t = tt / 12
			 	rt = float(input('RATE(%): '))
			 	r = rt / 100
			 	print('PLEASE PICK YOUR MODE')
			 	print('''[M] to Monthly [Q] for Quartertly [S] for Semini annual [A] for Annual''')
			 	mt = input('INPUT YOUR MODE OF PAYMENT: ')
			 	if mt == 'M' or mt == 'm':
			 		m = 12
			 	elif mt == 'Q' or mt == 'q':
			 		m = 4
			 	elif mt == 'S' or mt == 's':
			 		m = 2
			 	elif mt == 'A' or mt == 'a':
			 		m = 1
			 		
			 	n = m * t
			 	j = r / m
			 	at = (1 + j) ** n 
			 	a = at - 1
			 	
			 	b = a / j
			 	res = str(round(p * b, 2))
			 	print(f'The Future Value is {res}')
			 	
			 except :
			 	print('wrong input')
			 	continue
			 	
			 
			if chk == 'B' or chk == 'b':
			 try:
			 	print('/////Annuity PRINCIPAL AMOUNT//////')
			 	p = float(input('PERIODIC PAYMENT:  '))
			 	tt  = float(input('TIME IN MONTHS: '))
			 	t = tt / 12
			 	rt = float(input('RATE(%): '))
			 	r = rt / 100
			 	print('PLEASE PICK YOUR MODE')
			 	print('''[M] to Monthly [Q] for Quartertly [S] for Semini annual [A] for Annual''')
			 	mt = input('INPUT YOUR MODE OF PAYMENT: ')
			 	if mt == 'M' or mt == 'm':
			 		m = 12
			 	elif mt == 'Q' or mt == 'q':
			 		m = 4
			 	elif mt == 'S' or mt == 's':
			 		m = 2
			 	elif mt == 'A' or mt == 'a':
			 		m = 1
			 		
			 	n = (m * t) * -1
			 	j = r / m
			 	a = 1 - (1 + j) **n
			 	res1 = (a / j) * p
			 	res = str(round(res1, 3))
			 	print(f'The Present Value is {res}')
			 	
			 except :
			 	print('wrong input')
			 	continue
########test##############



#uses if find future valur			 
			if chk == 'C' or chk == 'c':
			 try:
			 	print('/////PERIODIC PAYMENT BUT FUTURE VALUE AVAILABLE//////')
			 	p = float(input('present value:  '))
			 	tt  = float(input('TIME IN MONTHS: '))
			 	t = tt / 12
			 	rt = float(input('RATE(%): '))
			 	r = rt / 100
			 	print('PLEASE PICK YOUR MODE')
			 	print('''[M] to Monthly [Q] for Quartertly [S] for Semini annual [A] for Annual''')
			 	mt = input('INPUT YOUR MODE OF PAYMENT: ')
			 	if mt == 'M' or mt == 'm':
			 		m = 12
			 	elif mt == 'Q' or mt == 'q':
			 		m = 4
			 	elif mt == 'S' or mt == 's':
			 		m = 2
			 	elif mt == 'A' or mt == 'a':
			 		m = 1
			 	j
			 	
			 	
			 except :
			 	print('wrong input')
			 	continue
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
			 
	
			 
			 
			 
			 
			
			if chk == 'D' or chk == 'd':
			 try:
			 	print('/////Annuity PRINCIPAL AMOUNT//////')
			 	p = float(input('PERIODIC PAYMENT:  '))
			 	tt  = float(input('TIME IN MONTHS: '))
			 	t = tt / 12
			 	rt = float(input('RATE(%): '))
			 	r = rt / 100
			 	print('PLEASE PICK YOUR MODE')
			 	print('''[M] to Monthly [Q] for Quartertly [S] for Semini annual [A] for Annual''')
			 	mt = input('INPUT YOUR MODE OF PAYMENT: ')
			 	if mt == 'M' or mt == 'm':
			 		m = 12
			 	elif mt == 'Q' or mt == 'q':
			 		m = 4
			 	elif mt == 'S' or mt == 's':
			 		m = 2
			 	elif mt == 'A' or mt == 'a':
			 		m = 1
			 		
			 	n = (m * t) * -1
			 	j = r / m
			 	a = 1 - (1 + j) **n
			 	res1 = (a / j) * p
			 	res = str(round(res1, 3))
			 	print(f'The Present Value is {res}')
			 	
			 except :
			 	print('wrong input')
			 	continue
			 
						
			
	#Compute Compound Interest		
	elif a == '8':
			print('============COMPOUND INTEREST====== ')
			print('[A] TO COMPUTE COMPOUND FINAL AMOUNT')
			print('[B] TO COMPUTE PRINCIPAL')
			print('[C] TO COMPUTE COMPOUND INTEREST')
			print('[D] TO COMPUTE COMPOUND RATE')
			print('[E] TO COMPUTE COMPOUND TIME')
			comp = input('PLEASE CHOOSE OPERATION ==> ')
			if comp == 'A' or comp == 'a':
				try:
					print('///////Final Amount///////')
					p = float(input('PRINCIPAL AMOUNT: '))
					ttemp = float(input('TIME IN MONTHS: '))
					t = ttemp / 12
					rtemp = float(input('Rate(%): '))
					r = rtemp / 100
					print('=======================')
					print('''[M] to monthly [Q] to quarterly [S] to semi annual [A] to annual ''')
					mt = input('INPUT YOUR MODE OF PAYMENT: ')
					if mt == 'm':
						m = 12
					elif mt == 'q':
						m = 4
					elif mt == 's':
						m = 2
					elif mt == 'a':
						m = 1
					n = m * t
					fe = (1 + (r / m))**n
					f = p * fe
					print(f'Your Compound Interest Is: {f}')
						
				except ValueError:
					print('Seems wrong value try again')
					continue
			
			if comp == 'b' or comp == 'B':
				try:
					print('///////PRINCIPAL AMOUNT///////')
					f = float(input('FINAL AMOUNT: '))
					ttemp = float(input('TIME IN MONTHS: '))
					t = ttemp / 12
					rtemp = float(input('Rate(%): '))
					r = rtemp / 100
					print('=======================')
					print('''[M] to monthly [Q] to quarterly [S] to semi annual [A] to annual ''')
					mt = input('INPUT YOUR MODE OF PAYMENT: ')
					if mt == 'm':
						m = 12
					elif mt == 'q':
						m = 4
					elif mt == 's':
						m = 2
					elif mt == 'a':
						m = 1
					n = -1 * (m * t)
					pt = r / m
					pe = f * (1 + pt) ** n
					print(pe)
					
					
					
				except ValueError:
					print('Seems wrong value try again')
					continue
		
			if comp == 'C' or comp == 'c':
				try:
					print('///////INTEREST///////')
					p = float(input('PRINCIPAL AMOUNT: '))
					F = float(input('FINAL AMOUNT: '))
					res = F - p
					print('The Interest Amount Is %s'%res)
			
						
				except ValueError:
					print('Seems wrong value try again')
					continue
		
			if comp == 'D' or comp == 'd':
				try:
					print('///////RATE///////')
					p = float(input('PRINCIPAL AMOUNT: '))
					f = float(input('FINAL AMOUNT: '))
					ttemp = float(input('TIME IN MONTHS: '))
					t = ttemp / 12
					print('=======================')
					print('''[M] to monthly [Q] to quarterly [S] to semi annual [A] to annual ''')
					mt = input('INPUT YOUR MODE OF PAYMENT: ')
					if mt == 'm':
						m = 12
					elif mt == 'q':
						m = 4
					elif mt == 's':
						m = 2
					elif mt == 'a':
						m = 1
					n = m * t
					nth = (f/p) ** (1/n) -1
					rt = nth * m
					res = str(round(rt * 100, 2))
					print(f'Compund Rate is == {res}%')
						
				except ValueError:
					print('Seems wrong value try again')
					continue
			if comp == 'E' or comp == 'e':
				try:
					print('///////RATE///////')
					p = float(input('PRINCIPAL AMOUNT: '))
					f = float(input('FINAL AMOUNT: '))
					rt = float(input('RATE(%): '))
					r = rt / 100
					
					print('=======================')
					print('''[M] to monthly [Q] to quarterly [S] to semi annual [A] to annual ''')
					mt = input('INPUT YOUR MODE OF PAYMENT: ')
					if mt == 'm':
						m = 12
					elif mt == 'q':
						m = 4
					elif mt == 's':
						m = 2
					elif mt == 'a':
						m = 1
					a = math.log10(f/p)
					b = m * math.log10(1 + r/m)
					res = str(round(a / b, 2))
					print(f'The Compound Time is {res} years')
					
						
				except ValueError:
					print('Seems wrong value try again')
					continue
					
					
		
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
									
	#please dont touch 				
	elif a == input():
				break
					
					
				
				
					
			
			
		    
     

			
    
			
			
			
			
			
			

	
	
			
	