

class Warrior():
    rank_info = {
        0: "Pushover",  # 1-9
        1: "Novice",  # 10-19
        2: "Fighter",  # 20-29
        3: "Warrior",  # 30-39
        4: "Veteran",  # 40-49
        5: "Sage",  # 50-59
        6: "Elite",  # 60-69
        7: "Conqueror",  # 70-79
        8: "Champion",  # 80-89
        9: "Master",  # 90-99
        10: "Greatest"  # 100
    }
    MAX_LVL = 100
    MAX_EXP = 10000
    EXP_IN_LVL = 100
    LVLS_IN_RANK = 10
    
    def __init__(self):
        self.__level: int = 1
        self.__experience: int = 100
        self.__rank: int = 0
        self.__achievements: list = []
    
    @property
    def level(self):
        return self.__level
    
    def __up_level_and_rank(set_exp):
        def wrapper(self, experience_up: int):
            set_exp(self, experience_up)
            if self.level < self.MAX_LVL:
                level = self.experience // self.EXP_IN_LVL
                self.__level = level
                rank = level // self.LVLS_IN_RANK
                self.__rank = rank

        return wrapper
    
    @property
    def experience(self):
        return self.__experience
    
    @__up_level_and_rank
    def __set_experience(self, experience_up: int):
        if self.experience < self.MAX_EXP:
            if (self.experience + experience_up) > self.MAX_EXP:
                self.__experience = self.MAX_EXP
            else:
                self.__experience += experience_up
    
    @property
    def rank(self):
        return self.rank_info[self.__rank]
    
    @property
    def achievements(self):
        return self.__achievements
    
    def __set_achievements(self, achievement: str):
        self.__achievements.append(achievement)
    
    def training(self, npc: list):
        npc_describe = npc[0]
        npc_exp = npc[1]
        
        if npc[2] > self.level:
            return "Not strong enough"
        else:
            self.__set_achievements(npc_describe)
            self.__set_experience(npc_exp)
        
        return npc_describe
    
    @staticmethod
    def count_exp(diff):
        return 20 * diff * diff

    def battle(self, lvl_enemy):
        if 1 <= lvl_enemy <= self.MAX_LVL:
            rank_enemy = lvl_enemy // self.LVLS_IN_RANK
            delta_lvl = lvl_enemy - self.level
            delta_rank = rank_enemy - self.__rank
            
            if delta_lvl == 0:
                self.__set_experience(10)
                return "A good fight"
            
            elif delta_lvl == -1:
                self.__set_experience(5)
                return "A good fight"
            
            elif delta_lvl <= -2:
                self.__set_experience(0)
                return "Easy fight"
            
            elif (delta_lvl >= 5) and (delta_rank >= 1):
                return "You've been defeated"
            
            else:
                exp = self.count_exp(delta_lvl)
                self.__set_experience(exp)
                return "An intense fight"
        else:
            return "Invalid level"

w = Warrior()
print(w.level)
print(w.experience)
print(w.rank)
print(w.training(["Defeated Chuck Norris", 9000, 1]))
print(w.experience)
print(w.level)
print(w.rank)
print(w.battle(99))
print(w.experience)
print(w.achievements)
