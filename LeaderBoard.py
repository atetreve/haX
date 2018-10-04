import random

class LeaderBoard:
    def __init__(self):
        self.player_ids = []
        self.player_scores = []

    def generate_rand_id():
        new_id = random.randint(-2^32 - 1, 2^32 - 1)
        if new_id not in self.player_ids:
            return new_id
        else:
            self.generate_rand_id()
        
    def add_score(self, player_id, score):

        if player_id not in self.player_ids:
            self.player_ids.append(int(player_id))
            self.player_scores.append([float(score)])
            print(float(score))
        else:
            ind = self.player_ids.index(player_id)
            self.player_scores[ind] = self.player_scores[ind]+[float(score)]
            print(sum(self.player_scores[ind])/float(len(self.player_scores[ind])))
            #print(sum(self.player_scores[ind]/len(self.player_scores[ind])))
        
    def top(self, max_num):
        score_averages = []
        for score_list in self.player_scores:
            score_averages.append(sum(score_list)/len(score_list))
        
        sorted_score_averages = sorted(score_averages)[::-1]
        top_n = sorted_score_averages[:max_num]

        ''''
        top_n_ids = []
        count = 0
        while count < max_num:
            for ind in range(len(self.player_ids)):
                avg_s = sum(self.player_scores[ind])/float(len(self.player_scores[ind]))
                if avg_s in top_n:
                    top_n_ids.append(self.player_ids[score_averages.index(avg_s)])
                    count += 1
                else:
                    count += 1
        print(top_n_ids)
        '''
        top_n_ids = []
        for tops in top_n:
            top_n_ids.append(self.player_ids[score_averages.index(tops)])
        print(top_n_ids)


    def reset(self, player_id):
        ind = self.player_ids.index(player_id)
        self.player_scores[ind] = [0]