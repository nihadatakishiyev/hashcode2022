import utils
import models

if __name__ == '__main__':
    files = utils.read_input_file_names()
    for i in files:
        data = open('src/in/' + i)
        C, P = data.readline().split()
        contributors = []
        projects = []
        for j in range(0, int(C)):
            name, num_skills = data.readline().split()
            skills = {}
            for o in range(0, int(num_skills)):
                s_name, level = data.readline().split()
                skills[s_name] = int(level)

            contributors.append(models.Contributor(name, num_skills, skills))

        for k in range(0, int(P)):
            p_name, deadline, score, b_before, num_roles = data.readline().split()
            roles = {}
            for x in range(0, int(num_roles)):
                s_name, level = data.readline().split()
                roles[s_name] = int(level)

            projects.append(models.Project(p_name, deadline, score, b_before, num_roles, roles))

