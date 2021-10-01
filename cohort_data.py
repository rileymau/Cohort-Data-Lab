"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    #filename = "cohort_data.txt"
    houses = set()

    the_file = open(filename)

    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      if line[2] != '': 
        houses.add(line[2])

    return houses


def students_by_cohort(filename, cohort="All"):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    #cohort = cohort
    students = []

    the_file = open(filename)
    
    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      #if line[4] == "I" or line[4] == "G":
        
      if cohort == "All" and line[4] != "I" and line[4] != "G":
        students.append(f"{line[0]} {line[1]}")

      elif cohort == line[4] and line[4] != "I" and line[4] != "G":
        students.append(f"{line[0]} {line[1]}")

      #elif line[4] == []:
        #print(line)
       # students.append(f"{line[0]} {line[1]}")

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    all_houses = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    the_file = open(filename)


    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      # if line[2] == '':
      #   pass

      i = 0
      while i < len(all_houses)-1:
        if line[2] == all_houses[i] and line[2] != '':
          all_houses[i].append(f"{line[0]} {line[1]}")
        i = i + 1
        

    

    return all_houses


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    the_file = open(filename)

    all_data = []

    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      student_tuple = ((f"{line[0]} {line[1]}"), line[2], line[3], line[4])

      all_data.append(student_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    the_file = open(filename)

    student_tuple = tuple()

    for line in the_file:
      line = line.rstrip()
      line = line.split('|')
      
      student_tuple = ((f"{line[0]} {line[1]}"), line[2], line[3], line[4])

      if name == student_tuple[0]:
        return line[4]
  

def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    last_names = []
    # all last names 

    the_file = open(filename)
    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      last_names.append(line[1])
    #make list of all last names

    
    # make a set of that list
    # has names only once

    dif = [lastname for lastname in last_names if last_names.count(lastname) > 1]
    # subtract those

    ln_set = set(dif)

    #dupe = []
    # if line[1] not in dupe:
      #dupe.append(line[1])
    # make set of difference
    return(ln_set)
    


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    the_file = open(filename)

    housemates_list = []
    house_name = ''
    cohort = ''

    for line in the_file:
      line = line.rstrip()
      line = line.split('|')

      student_name = f"{line[0]} {line[1]}")
      

      #student_tuple = ((f"{line[0]} {line[1]}"), line[2], line[3], line[4])


      if name == student_name:
        house_name = line[2]
        cohort = line[4]

      
      *
      if house_name == line[2]:
        housemates_list.append(f"{line[0]} {line[1]}"))

      return housemates_list
    





##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == "__main__":
    import doctest

    result = doctest.testfile(
        "doctests.py",
        report=False,
        optionflags=(doctest.REPORT_ONLY_FIRST_FAILURE),
    )
    doctest.master.summarize(1)
    if result.failed == 0:
        print("ALL TESTS PASSED")
