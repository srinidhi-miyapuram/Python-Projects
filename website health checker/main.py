import datetime, csv, requests
from dateutil import parser


class Checker:
    
    def __init__(self):
        self.fileName = 'response.csv'
        print("Starting Checker \n ----------------")
        with open(self.fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['TimeStamp', 'URL', 'Response Time (ms)', 'Status_Code', "Status"])
            f.close()
    
    
    
    def __checker(self, web):
        try:
            self.response = requests.get(url=web)
            self.req_date = parser.parse(self.response.headers['date'])
            
            self.state = "Online"
            self.res_time = round(self.response.elapsed.total_seconds()*1000, 3)
            self.code = self.response.status_code
        except:
            self.req_date = datetime.datetime.now()
            self.state = "Offline"
            self.code = "N/A"
            self.res_time = "N/A"
            print("Failed to connect to", web)
        finally:
            with open(self.fileName, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([self.req_date, web, self.res_time, self.code, self.state])
                f.close()
    
    
    def update_file(self):
        with open("website.txt", 'r') as f:
            for line in f:
                web = line.rstrip('\n')
                print(web, '\n --------------------------')
                self.__checker(web)



if __name__ == '__main__':
    checker = Checker()
    checker.update_file()