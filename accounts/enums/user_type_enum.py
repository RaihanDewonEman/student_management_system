from enum import Enum


class StatusBEnum(Enum):
    STUDENT = 3
    TEACHER = 2
    OFFICER = 1

    @classmethod
    def choice_list(cls):
        options = list()
        for item in cls:
            options.append((item.value, item.name))
            #print(options)
        return options
