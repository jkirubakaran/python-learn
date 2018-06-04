import sys

class Employee(object):
	"""docstring for Employee"""

	raise_amount = 1.05
	num_of_emp = 0

	def __init__(self, first, last, pay):
		super(Employee, self).__init__()
		self.first = first
		self.last = last
		self.pay = pay

		Employee.num_of_emp += 1

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * Employee.raise_amount)
	
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

#emp_1 = Employee('foo','bar', 100)
#emp_2 = Employee('joe','moo',200) 

emp_str_1 = 'John-Doe-1000'
emp_str_2 = 'Foo-Mu-2000'
emp_str_3 = 'Happy-Gillmore-3000'

#first, last, pay = emp_str_1.split('-')

#emp1 = Employee(first, last, pay)
emp1 = Employee.from_string(emp_str_1)
print(emp1.email)



	
