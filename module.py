#modules= a file containing code you want to include in your programme
#        use import to include a module (built-in or your own)
#        useful to break up a large programme reusable seperate files

print(help("modules"))

print(help('math'))

import example ## in different folder
print(example.pi)

print(f'cude is: {example.cube(2)}')


