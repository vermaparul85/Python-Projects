from faker import Faker
import pandas as pd

fake = Faker()

# 1. Create list of 10 fake profile using list comprehension
profiles = [fake.profile() for _ in range(10)]

# 2. Create list of 10 fake profile using loop
# profiles = []
# for _ in range(10):
#     profiles.append(fake.profile())
# print(profiles)

# 3. Create dataframe
df = pd.DataFrame(profiles)

# 4. Select few columns and update dataframe
df = df[['name', 'job', 'company', 'address', 'mail']]

# 5. Create list of 10 fake phone number using list comprehension
phone_numbers = [fake.phone_number() for _ in range(10)]
df['phone'] = phone_numbers

# 6. rename the column name. mail => email
df.rename(columns={'mail':'email'}, inplace=True)

# 7. Save the data to CSV file
df.to_csv('fake_profiles.csv',index=False)
