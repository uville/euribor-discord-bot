import requests
import xmltodict

URL = "https://www.suomenpankki.fi/WebForms/ReportViewerPage.aspx?report=/tilastot/markkina-_ja_hallinnolliset_korot/euribor_korot_today_xml_en&output=xml"


class Euribor:
    def __init__(self):
        pass

    def get_euribor_data(self):
        response = requests.get(URL)
        return xmltodict.parse(response.content)

    def parse_title(self, tree):
        return tree["Report"]["@title"]

    def parse_twelve_months_euribor(self, tree):
        return tree["Report"]["data"]["period_Collection"]["period"][
            "matrix1_Title_Collection"
        ]["rate"][5]["intr"]["@value"]

    def reply_to_12_months(self):
        data = self.get_euribor_data()
        title = self.parse_title(data)
        euribor = self.parse_twelve_months_euribor(data)
        return str(title + ": " + euribor)
