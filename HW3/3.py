import pickle

class UnigramMorphAnalyzer():

    statistics = {}
    result_statistics = {}
    results = []

    def __init__(self, train_data, test_data=None):
        self.train_data = train_data
        self.test_data = test_data or []

    def train(self):
        for line in self.train_data:
            word = line.split()[0]
            tag = line.split()[-1]
            endings = []
            ending1 = word[-1]
            endings.append(ending1)
            if len(word) >= 2:
                ending2 = word[-2:]
                endings.append(ending2)
            if len(word) >= 3:
                ending3 = word[-3:]
                endings.append(ending3)
            if len(word) >= 4:
                ending4 = word[-4:]
                endings.append(ending4)
            for ending in endings:
                if ending in self.statistics:
                    if tag in self.statistics[ending]:
                        self.statistics[ending][tag] += 1
                    else:
                        self.statistics[ending][tag] = 1
                else:
                    self.statistics[ending] = {}
                    self.statistics[ending][tag] = 1
        return self.statistics

    def predict(self, token):
        endings = []
        ending1 = token[-1]
        endings.append(ending1)
        if len(token) >= 2:
            ending2 = token[-2:]
            endings.append(ending2)
        if len(token) >= 3:
            ending3 = token[-3:]
            endings.append(ending3)
        if len(token) >= 4:
            ending4 = token[-4:]
            endings.append(ending4)
        for ending in endings:
            if ending in self.statistics:
                result = self.statistics[ending]
                for key in result:
                    if key in self.result_statistics:
                        self.result_statistics[key] += result[key]
                    else:
                        self.result_statistics[key] = result[key]
        probable = max(self.result_statistics, key=self.result_statistics.get)
        return probable

    def save(self):
        f = open('saved_model', 'wb')
        pickle.dump(self.statistics, f)

    def load(self):
        f = open('saved_model', 'rb')
        self.statistics = pickle.load(f)

    def __getitem__(self, ending):
        return self.statistics[ending]

    def eval(self):
        correct = 0
        counter = 0
        for line in self.test_data:
            word = line.split()[0]
            tag = line.split()[-1]
            result = self.predict(word)
            if result == tag:
                correct += 1
            counter += 1
        return(f'Effective tag assignment is {correct/counter}.')
        
        
train_file = open('pos_data_train.txt', 'r', encoding='utf-8')
test_file = open('pos_data_test.txt', 'r', encoding='utf-8')
model = UnigramMorphAnalyzer(train_file, test_file)
model.train()
print(model.predict('караван'))
print(model.predict('бежать'))
print(model.predict('нарочно'))
print(model['ать'])
print(model.eval())
