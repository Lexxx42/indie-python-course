"""
Симметрическая разность ( от английского symmetric difference) двух множеств – это операция,
позволяющая получить новое множество, в которое включены все элементы двух множеств,
не принадлежащие одновременно обоим исходным множествам.

Также симметрическую разность можно рассматривать как разность между объединением и пересечением исходных множеств.
В математике симметрическая разность множеств A и В обозначается так A△B.

Симметрическая разность множеств в python
"""

my_friend = {'Bill', 'Ash', 'Jim'}
jack_friends = {'Bill', 'Kir'}

symm_diff_me_jack = my_friend ^ jack_friends
print('Симметрическая разность с Джеком', symm_diff_me_jack)

terry_friends = {'Zara', 'Pit'}
symm_diff_me_terry = my_friend ^ terry_friends
print('Симметрическая разность с Терри', symm_diff_me_terry)
