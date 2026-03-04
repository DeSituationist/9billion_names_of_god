cardinal_numbers = ('first', 'second', 'third')
print(cardinal_numbers[1])
position_1, position_2, position_3 = cardinal_numbers
print(position_1)
print(position_2)
print(position_3)
my_name = ('Ilia')
print('x' in my_name)
new_name = my_name[1:]
print(new_name)
food = ['rice', 'beans']
food.append('broccoli')
food.extend(['bread', 'pizza'])
print(food[:3])
print(food[-1])
breakfast = 'eggs, fruit, orangejuice'.split(', ')
print(len(breakfast))
lengths = [len(s) for s in breakfast]
print(lengths)
data = ((1, 2), (3, 4))
for i, row in enumerate(data): print(f'Row {i+1} summ: {sum(row)}')
numbers = [4, 3, 2, 1]
new_nums = numbers[:]
numbers.sort()
print(new_nums)
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(unis: list[list[str, int, int]]) -> tuple[list, list]:
    '''Splits university data into two lists'''
    enrol_data, pay_data = [], []
    for uni in unis:
        enrol_data.append(uni[1])
        pay_data.append(uni[2])
    return (enrol_data, pay_data)
def mean(info: list[int]) -> int:
    '''Returns Average number'''
    return sum(info) / len(info)
def median(info: list[int]) -> int:
    '''Return number in middle'''
    if len(info) % 2 != 0: return info[len(info) // 2]
    else: return (info[len(info) // 2] + info[len(info) // 2 - 1]) // 2
info_about_unis = enrollment_stats(universities)
money_mean, money_meadian = mean(info_about_unis[1]), median(info_about_unis[1])
student_mean, student_median = mean(info_about_unis[0]), median(info_about_unis[0])
print(f'''{'*' * 20}
Total students: {sum(info_about_unis[0]):,}
total tuition: {sum(info_about_unis[1]):,}\n
Student mean: {student_mean:,.2f}
Student median: {student_median:,.0f}\n
Tuition mean: {money_mean:,.2f}
Tuition median: {money_meadian:,.0f}
{'*' * 20}''')
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
pretexts = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = [ "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
import random
three_nouns = [random.choice(nouns) for _ in range(3)]
three_verbs = [random.choice(verbs) for _ in range(3)]
three_adjectives = [random.choice(adjectives) for _ in range(3)]
two_pretexts = [random.choice(pretexts) for _ in range(2)]
adverb = random.choice(adverbs)
print(f'''
A/An {three_adjectives[0]} {three_nouns[0]}\n
A/An {three_adjectives[0]} {three_nouns[0]} {three_verbs[0]} {two_pretexts[0]} the {three_adjectives[1]} {three_nouns[1]}
{adverb}, the {three_nouns[0]} {three_verbs[1]}
the {three_nouns[1]} {three_verbs[2]} {two_pretexts[1]} a {three_adjectives[2]} {three_nouns[2]}
''')
captains = {}
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'
if 'Enterprise' not in captains: captains['Enterprise'] = 'unknown'
if 'Discovery' not in captains: captains['Discovery'] = 'unknown'
for name in captains: print(f'The {name} is captained by {captains[name]}')
captains.pop('Discovery')
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}
import random
state, city = random.choice(list(capitals_dict.items()))
while True:
    user_input = input(f'Try to guess the capital of {state} or leave: ').lower()
    if user_input == 'exit': 
        print(f'The correct answer was {city}\nGoodbye!')
        break
    if user_input == city:
        print('Correct')
        break
    else:
        print('Wrong, try again.')
cats = [0] * 100
for _ in range(1, 101):
    for c_position in range(1, 101):
        if c_position % _ == 0:
            if cats[c_position - 1] == 0: cats[c_position - 1] = 1
            else: cats[c_position - 1] = 0
print([c_position for c_position in range(1, 101) if cats[c_position - 1] == 1])