from pprint import pprint
my_dict = {'firs': 'so eay'}
def dict_maker(**kwargs):
    my_dict.update(**kwargs)
dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Миша', age=31, weight=70, eyes_color='blue')
pprint(my_dict)
