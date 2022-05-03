from mongodb import Mongodb
import csv


class video:
    def __init__(self):
        self.__client = Mongodb("localhost", "italkutalk_db")
        self.col = self.__client.get_col("video")

    def create_game_langs_csv(self):
        test = list(self.col.find(
            {"language": 2}, {"index": 1, "videoInfo.videourl": 1, "videoInfo.title": 1, "videoInfo.duration": 1}))
        print(test)
        rows = []
        with open('test.csv', mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["#", "影片名稱", "秒數"])
            for row in test:
                urlID = str(row["videoInfo"]["videourl"])[-11:]
                italkutalk_url = f'https://manage.italkutalk.com/gameTimeCheck/88B1DA8D836871D21324214AE66A2FD26B741B27?{urlID}'
                videoTitle = row.videoInfo.title
                duration = row["videoInfo"]["duration"]
                index = row["index"]
                test = f'=HYPERLINK("{italkutalk_url}", "{videoTitle}")'
                temp = [index, test, duration]
                rows.append(temp)
            writer.writerows(rows)
