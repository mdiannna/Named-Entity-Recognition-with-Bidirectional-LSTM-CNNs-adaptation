from faker import Faker
fake = Faker()

# print(fake.name())
# 'Lucy Cechtelar'

# print(fake.address())
# print(fake.phone_number())
# print(fake.email())

file_sizes =[700, 150, 150]
file_names = ['data/mydataset2.txt', 'data/mydataset_test2.txt', 'data/mydataset_valid2.txt']

for i in range(0, len(file_names)):
	file_name = file_names[i]
	file_size = file_sizes[i]
	
	f = open(file_name, 'w')
	f.write('-DOCSTART- -X- -X- O\n\n')


	for i in range(1, file_size):
		f_address = fake.address().replace('\n', ', ')
		f_phone = fake.phone_number()
		f_email = fake.email()
		f_word = fake.word()

		f.write(f_address + " -A-\n")
		f.write(f_email + " -E-\n")
		f.write(f_phone + " -P-\n")
		f.write(f_word + " -O-\n")

	f.close()

