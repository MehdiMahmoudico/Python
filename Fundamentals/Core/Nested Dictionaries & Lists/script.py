x = [ [5,2,3], [10,8,9] ] 

x[1][0]=15

print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name']="Bryant"
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]="Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]

z[0]['y']=30

print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]




def iterateDictionary(students):
    for key in students:
        print(f"first_name - {key['first_name']}, last_name - {key['last_name']}")

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for kname in students :
        print(kname[key_name])

iterateDictionary2("first_name" , students)
iterateDictionary2("last_name" , students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict) :
    print(len(dojo["locations"]),"LOCATIONS",)
    for i in dojo["locations"] :
        print(i)

    print(len(dojo["instructors"]),"INSTRUCTORS",)
    for b in dojo["instructors"] :
        print(b)


printInfo(dojo)
