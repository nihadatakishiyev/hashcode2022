class Contributor:
    def __init__(self, name, num_skill, skills):
        self.name = name
        self.num_skill = num_skill
        self.skills = skills
        self.isBusy = False

    def increase_skill(self, skill):
        self.skills[skill] += 1

    def start_working(self):
        self.isBusy = True

    def stop_working(self):
        self.isBusy = False

    def skill_level(self, role):
        return self.skills[role]

    def __repr__(self):
        return str(self.name)

class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return str(self)


class Project:
    def __init__(self, name, deadline, score, b_before, num_roles, roles):
        self.name = name
        self.deadline = deadline
        self.score = score
        self.b_before = b_before
        self.num_roles = num_roles
        self.roles = roles

    def __repr__(self):
        return str(self.name) + ' : ' + str(self.roles)
