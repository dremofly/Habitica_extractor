from datetime import datetime
import json

class habitica:
    def __init__(self, filename, begin, end):
        with open(filename) as f:
            self.data = json.load(f)
        self.data = self.data['tasks'] 
        self.begin = begin
        self.end = end
        self.todos = []
        self.dailys = {}
        self._extract_todos()
        self._extract_dailys()

    def _timeExtract(self, timestamp):
    # for todos
        dateStr = timestamp[:10]
        newTime = datetime.strptime(dateStr, '%Y-%m-%d') 
        return newTime
    
    def _timestampExtract(self, timestamp):
    # for dailys
        dateStr = timestamp[:10]
        newTime = int(datetime.strptime(dateStr, '%Y-%m-%d').timestamp())
        return newTime
    
    def _extract_todos(self):
       begin = self._timeExtract(self.begin)
       end = self._timeExtract(self.end) 
       for item in self.data['todos']:
            try:
               if self._timeExtract(item['dateCompleted'])>=begin and self._timeExtract(item['dateCompleted'])<=end:
                   self.todos.append(item['text'])
            except:
                pass
    
    def _extract_dailys(self):
        tbegin = self._timestampExtract(self.begin)
        tend = self._timestampExtract(self.end)
        for item in self.data['dailys']:
            historys = item['history']
            self.dailys[item['text']] = 0
            #print(tbegin)
            for h in historys:
                if h['value']>0:
                    if h['date']/1000 >= int(tbegin) and h['date']/1000 <= int(tend):
                        self.dailys[item['text']] += 1
    
    def get_todos(self):
        print("这一周完成了"+str(len(self.todos))+"件工作。")
        for item in self.todos:
            print(item) 
        #return self.todos
    
    def get_dailys(self):
        print("这一周的习惯完成情况:")
        for key in self.dailys:
            print(key, self.dailys[key])
        #return self.dailys
