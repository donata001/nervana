import os
from .models import Houses
from django.contrib.auth.models import User
from django.utils.timezone import now

ready_file = 'housing.csv'



# raw big file cutter to 1000 lines to further trim
def read_truncate_csv(file):
    if not os.path.isfile(file):
        raise Exception('No such file.')
    
    counter = 0
    with open(file, 'r') as f1:
        with open('cutted', 'w+') as f2:

            for line in f1:
                f2.write(line)
                f2.flush()
                counter += 1
                if counter > 1000:
                    break
    
    
    
def import_to_db():
    if not os.path.isfile(ready_file):
        raise Exception('No such file.')
    tobe_created = []
    with open(ready_file, 'r') as f:
        #skip first line
        f.readline()
        for line in f:
            fields = line.split(',')
            hs = Houses(age=int(fields[0]),
                        region=fields[1],
                        weight=float(fields[2]),
                        bedrooms=int(fields[3]),
                        built_year=int(fields[4]),
                        value =int(fields[5]),
                        vacancy = int(fields[6]),
                        nunit =int(fields[7]),
                        rooms = int(fields[8]),
                        utility = float(fields[9]),
                        type = fields[-1].split("'")[0])

            tobe_created.append(hs)
        Houses.objects.bulk_create(tobe_created, 500)   
            
 
def create_superuser():
    User.objects.create_user(password='sesame',
                              last_login=now(), 
                              username='open',
                              first_name='dd', 
                              last_name='ff', 
                              email='fake@fa.com')         
            
if __name__ == "__main__":
    import_to_db()           
    create_superuser()      
            
            
            
            
            
            
        