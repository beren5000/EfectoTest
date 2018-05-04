from django.core.management.base import BaseCommand, CommandError
from apps.GeoSports.models import Profile
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        f = open("apps/GeoSports/management/commands/userprofiles.txt", "r")
        lines = f.readlines()
        x=0
        for line in lines:
            line = line.split(',')
            name = line[1].split()
            l = len(name)
            ##acomodo los nombres para su insercion en el usuario
            if l == 1:
                first_name = name[0]
                last_name = ''
            elif l == 2:
                first_name = name[0]
                last_name = name[1]
            elif l == 3:
                first_name = name[0] + " " + name[1]
                last_name = name[2]
            else:
                first_name = name[0] + " " + name[1]
                last_name = name[2] + " " + name[3]

            ##acomodo los generos de igual manera
            if line[3]=='male':
                gender=0
            else:
                gender=1
            new_user = User(first_name=first_name, last_name=last_name, email="dummy@dummy.com", username=line[0])
            new_user.save()
            new_profile = Profile(gender=gender,nationality=line[2])
            new_profile.user = new_user
            new_profile.id = line[0]
            new_profile.save()
        f.close()
        self.stdout.write(self.style.SUCCESS('Successfully upload UserProfiles'))

