class Contributor:
    def __init__(self, name, num_skill, skills):
        self.name = name
        self.num_skill = num_skill
        self.skills = skills
        self.isBusy = False

    def increase_skill(self, skill):
        if skill in self.skills:
            self.skills[skill] += 1
        else:
            self.skills[skill] = 1

    def start_working(self):
        self.isBusy = True

    def stop_working(self):
        self.isBusy = False

    def skill_level(self, role):
        if role in self.skills:
            return self.skills[role]
        else:
            return 0

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
        self.is_completed = False
        self.is_feasible = False
        self.day = 0
        self.is_started = False
        self.contributors = []

    def start(self):
        self.is_started = True

    def add_day(self):
        self.day += 1
        self.is_completed = self.completed()

    def add_contributor(self, contributor):
        self.contributors.append(contributor)

    def clear_contributors(self):
        self.contributors = []

    def has_higher_skill(self, skill, level):
        has = False
        for i in self.contributors:
            if i.skill_level(skill) >= level:
                has = True
                break

        return has

    def completed(self):
        # print(self.name+ " : " + str(self.day) + " : " + str(self.deadline) + "   == " + str(self.day == self.deadline))
        return self.day == self.deadline

    def __repr__(self):
        return str(self.name) + ' ' + str(self.score) + ' : ' + str(self.roles)
