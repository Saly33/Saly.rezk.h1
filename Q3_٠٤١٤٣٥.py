questions = [] 
with open('questions.txt') as f: 
    lines = f.read() 
    lines = lines.split('\n')
    
for line in lines: 
    questions.append(line.split('='))
    
name = input('Please, Enter Your name: ') 
mark = 0

print('Please, Ask for this questions..')

for q in questions: 
    answer = input('{} = '.format(q[0])) 
    if answer==q[1]: 
        mark+=1
        
print('Thank you, your mark is: {}'.format(mark))

with open('results.txt', 'a') as f: 
    f.write('{}: {}\n'.format(name,mark))
