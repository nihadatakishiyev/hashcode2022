import sys

import utils
import models

if __name__ == '__main__':
    files = utils.read_input_file_names()
    for i in files:
        data = open('src/in/' + i)
        C, P = data.readline().split()
        contributors = []
        projects = []
        last_day = 0
        for j in range(0, int(C)):
            name, num_skills = data.readline().split()
            skills = {}
            for o in range(0, int(num_skills)):
                s_name, level = data.readline().split()
                skills[s_name] = int(level)

            contributors.append(models.Contributor(name, int(num_skills), skills))

        for k in range(0, int(P)):
            p_name, deadline, score, b_before, num_roles = data.readline().split()
            roles = {}
            for x in range(0, int(num_roles)):
                s_name, level = data.readline().split()
                roles[s_name] = int(level)

            last_day += int(deadline)
            projects.append(models.Project(p_name, int(deadline), int(score), int(b_before), int(num_roles), roles))

        current_day = 0
        print(contributors)
        print(projects)
        print(last_day)

        while True:
            current_day += 1
            for p in projects:
                if not p.is_started and not p.is_completed:
                    hasAll = 0
                    for role in p.roles:
                        for conts in contributors:
                            if not conts.isBusy:
                                if conts.skill_level(role) >= p.roles[role]:
                                    conts.start_working()
                                    p.add_contributor(conts)
                                    hasAll += 1
                                elif p.has_higher_skill(role, p.roles[role]) and conts.skill_level(role)+1 >= p.roles[role]:
                                    conts.start_working()
                                    p.add_contributor(conts)
                                    hasAll += 1

                    if hasAll == p.num_roles:
                        p.start()
                    else:
                        for cont in p.contributors:
                            cont.stop_working()
                        p.clear_contributors()

            for p in projects:
                if p.is_started and not p.is_completed:
                    p.add_day()
                    if p.is_completed:
                        for index, skill in enumerate(p.roles):
                            p.contributors[index].increase_skill(skill)
                            p.contributors[index].stop_working()

            completed = [p for p in projects if p.is_completed == True]

            if current_day == last_day:
                writable = open('src/out/' + i, 'w')
                oldstdout = sys.stdout
                sys.stdout = writable  # Change the standard output to the file we created.
                print(len(completed))
                for p in completed:
                    print(p.name)
                    names = ''
                    for con in p.contributors:
                        names += con.name + ' '

                    print(names)

                sys.stdout = oldstdout  # Reset the standard output to its original value
                break
