# Перед вами имеется список кортежей names. Каждый кортеж состоит из двух элементов: имени и фамилии. Ваша задача на основании списка names создать новый список new_names, где каждый кортеж должен замениться на строку конкатенации имени и фамилии, между которыми стоит пробел . Вот пример на других данных:
#
# names = [('Monica', 'Waters'), ('Juan', 'Lee'), ('Donna', 'Walker')]
#
# new_names = ['Monica Waters', 'Juan Lee', 'Donna Walker']
# Для преобразования используйте функцию map
#
# В качестве ответа выведите переменную new_names
#
# Sample Input:
#
# Sample Output:
#
# ['Gerald Tucker', 'Tricia Johnson', 'Robert Mendez', 'Shawn Gutierrez', 'Gary Ross', 'Melanie Warren', 'Drew May', 'Jennifer Carroll', 'Ann Lynn', 'Ralph Vazquez', 'Brittany Erickson', 'Mark Montoya', 'Randall Hicks', 'Tyler Miller', 'Bryan Brown', 'Joshua Sawyer', 'Sarah Phillips', 'Donna Davenport', 'Rebekah Johnson', 'Andrew Reynolds', 'April Turner', 'Amanda Ryan', 'Jennifer Poole', 'Jonathan Lane', 'Laura Stone', 'Sara Brown', 'Alexander Johnson', 'Emily Phillips', 'Tyler Smith', 'Victor Kelly', 'Audrey Thomas', 'Melissa Green', 'Bethany Holt', 'Christopher Kerr', 'Gabrielle Black', 'Jennifer Wade', 'Douglas Horton', 'Steven Welch', 'Terri Thompson', 'Cassandra Nelson', 'Andrew Jones', 'James Schultz', 'Richard Castillo', 'Shaun Logan', 'Danielle Lane', 'Mark Anderson', 'Charles Shaw', 'Derrick Grant', 'Tracy Pierce', 'Robert Washington']

names = [('Gerald', 'Tucker'), ('Tricia', 'Johnson'), ('Robert', 'Mendez'),
         ('Shawn', 'Gutierrez'), ('Gary', 'Ross'), ('Melanie', 'Warren'),
         ('Drew', 'May'), ('Jennifer', 'Carroll'), ('Ann', 'Lynn'), ('Ralph', 'Vazquez'),
         ('Brittany', 'Erickson'), ('Mark', 'Montoya'), ('Randall', 'Hicks'),
         ('Tyler', 'Miller'), ('Bryan', 'Brown'), ('Joshua', 'Sawyer'),
         ('Sarah', 'Phillips'), ('Donna', 'Davenport'), ('Rebekah', 'Johnson'),
         ('Andrew', 'Reynolds'), ('April', 'Turner'), ('Amanda', 'Ryan'), ('Jennifer', 'Poole'),
         ('Jonathan', 'Lane'), ('Laura', 'Stone'), ('Sara', 'Brown'), ('Alexander', 'Johnson'),
         ('Emily', 'Phillips'), ('Tyler', 'Smith'), ('Victor', 'Kelly'), ('Audrey', 'Thomas'),
         ('Melissa', 'Green'), ('Bethany', 'Holt'), ('Christopher', 'Kerr'), ('Gabrielle', 'Black'),
         ('Jennifer', 'Wade'), ('Douglas', 'Horton'), ('Steven', 'Welch'),
         ('Terri', 'Thompson'), ('Cassandra', 'Nelson'), ('Andrew', 'Jones'),
         ('James', 'Schultz'), ('Richard', 'Castillo'), ('Shaun', 'Logan'),
         ('Danielle', 'Lane'), ('Mark', 'Anderson'), ('Charles', 'Shaw'),
         ('Derrick', 'Grant'), ('Tracy', 'Pierce'), ('Robert', 'Washington')]

new_names = list(map(lambda x: f'{x[0]} {x[1]}', names))
print(new_names)
