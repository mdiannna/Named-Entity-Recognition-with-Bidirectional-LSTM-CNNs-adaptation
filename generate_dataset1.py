from faker import Faker
fake = Faker()

# print(fake.name())
# 'Lucy Cechtelar'

# print(fake.address())
# print(fake.phone_number())
# print(fake.email())


f = open('data/mydataset1.txt', 'w')
f.write('-DOCSTART- -X- -X- O\n\n')


for i in range(1, 1000):
	f_address = fake.address().replace('\n', ', ')
	f_phone = fake.phone_number()
	f_email = fake.email()

	f.write(f_address + " -A-\n")
	f.write(f_email + " -E-\n")
	f.write(f_phone + " -P-\n")

f.close()


f = open('data/mydataset_test1.txt', 'w')
f.write('-DOCSTART- -X- -X- O\n\n')


for i in range(1, 300):
	f_address = fake.address().replace('\n', ', ')
	f_phone = fake.phone_number()
	f_email = fake.email()

	f.write(f_address + " -A-\n")
	f.write(f_email + " -E-\n")
	f.write(f_phone + " -P-\n")

f.close()


f = open('data/mydataset_valid1.txt', 'w')
f.write('-DOCSTART- -X- -X- O\n\n')

for i in range(1, 500):
	f_address = fake.address().replace('\n', ', ')
	f_phone = fake.phone_number()
	f_email = fake.email()

	f.write(f_address + " -A-\n")
	f.write(f_email + " -E-\n")
	f.write(f_phone + " -P-\n")

f.close()