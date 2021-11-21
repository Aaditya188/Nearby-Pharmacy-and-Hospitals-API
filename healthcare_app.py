import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
        return render_template("pharmacy.html")

@app.route("/map")
def main2():
        return render_template("hospital.html")

@app.route("/hospital/<float:latitude>/<float:longitude>", methods=['GET'])
def map(latitude, longitude):
        URL = "https://discover.search.hereapi.com/v1/discover"
        api_key = 'DXnwDkzLUZhFvDkFmEeZDRVm3W5SITTXX5V5-TWw63E'
        query = 'hospital'
        limit = 8

        PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
                }
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        hospitalOne = data['items'][0]['title']
        hospitalOne_address =  data['items'][0]['address']['label']
        hospitalOne_latitude = data['items'][0]['position']['lat']
        hospitalOne_longitude = data['items'][0]['position']['lng']

        hospitalTwo = data['items'][1]['title']
        hospitalTwo_address =  data['items'][1]['address']['label']
        hospitalTwo_latitude = data['items'][1]['position']['lat']
        hospitalTwo_longitude = data['items'][1]['position']['lng']

        hospitalThree = data['items'][2]['title']
        hospitalThree_address =  data['items'][2]['address']['label']
        hospitalThree_latitude = data['items'][2]['position']['lat']
        hospitalThree_longitude = data['items'][2]['position']['lng']

        hospitalFour = data['items'][3]['title']
        hospitalFour_address =  data['items'][3]['address']['label']
        hospitalFour_latitude = data['items'][3]['position']['lat']
        hospitalFour_longitude = data['items'][3]['position']['lng']

        hospitalFive = data['items'][4]['title']
        hospitalFive_address =  data['items'][4]['address']['label']
        hospitalFive_latitude = data['items'][4]['position']['lat']
        hospitalFive_longitude = data['items'][4]['position']['lng']

        hospitalSix = data['items'][5]['title']
        hospitalSix_address =  data['items'][5]['address']['label']
        hospitalSix_latitude = data['items'][5]['position']['lat']
        hospitalSix_longitude = data['items'][5]['position']['lng']

        hospitalSeven = data['items'][6]['title']
        hospitalSeven_address =  data['items'][6]['address']['label']
        hospitalSeven_latitude = data['items'][6]['position']['lat']
        hospitalSeven_longitude = data['items'][6]['position']['lng']

        hospitalEight = data['items'][7]['title']
        hospitalEight_address =  data['items'][7]['address']['label']
        hospitalEight_latitude = data['items'][7]['position']['lat']
        hospitalEight_longitude = data['items'][7]['position']['lng']
        return render_template('map.html',
                            latitude=latitude,
                            longitude=longitude,
                            apikey=api_key,
                            oneName=hospitalOne,
                            OneAddress=hospitalOne_address,
                            oneLatitude=hospitalOne_latitude,
                            oneLongitude=hospitalOne_longitude,
                            twoName=hospitalTwo,
                            twoAddress=hospitalTwo_address,
                            twoLatitude=hospitalTwo_latitude,
                            twoLongitude=hospitalTwo_longitude,
                            threeName=hospitalThree,
                            threeAddress=hospitalThree_address,
                            threeLatitude=hospitalThree_latitude,
                            threeLongitude=hospitalThree_longitude,
                            fourName=hospitalFour,		
                            fourAddress=hospitalFour_address,
                            fourLatitude=hospitalFour_latitude,
                            fourLongitude=hospitalFour_longitude,
                            fiveName=hospitalFive,
                            fiveAddress=hospitalFive_address,
                            fiveLatitude=hospitalFive_latitude,
                            fiveLongitude=hospitalFive_longitude,
                            sixName=hospitalSix,		
                            sixAddress=hospitalSix_address,
                            sixLatitude=hospitalSix_latitude,
                            sixLongitude=hospitalSix_longitude,
                            sevenName=hospitalSeven,		
                            sevenAddress=hospitalSeven_address,
                            sevenLatitude=hospitalSeven_latitude,
                            sevenLongitude=hospitalSeven_longitude,
                            eightName=hospitalEight,		
                            eightAddress=hospitalEight_address,
                            eightLatitude=hospitalEight_latitude,
                            eightLongitude=hospitalEight_longitude)


@app.route("/pharmacy/<float:latitude>/<float:longitude>", methods=['GET'])
def pharmacy(latitude, longitude):
        URL = "https://discover.search.hereapi.com/v1/discover"
        api_key = 'DXnwDkzLUZhFvDkFmEeZDRVm3W5SITTXX5V5-TWw63E'
        query = 'pharmacy'
        limit = 8

        PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
                }
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        hospitalOne = data['items'][0]['title']
        hospitalOne_address =  data['items'][0]['address']['label']
        hospitalOne_latitude = data['items'][0]['position']['lat']
        hospitalOne_longitude = data['items'][0]['position']['lng']

        hospitalTwo = data['items'][1]['title']
        hospitalTwo_address =  data['items'][1]['address']['label']
        hospitalTwo_latitude = data['items'][1]['position']['lat']
        hospitalTwo_longitude = data['items'][1]['position']['lng']

        hospitalThree = data['items'][2]['title']
        hospitalThree_address =  data['items'][2]['address']['label']
        hospitalThree_latitude = data['items'][2]['position']['lat']
        hospitalThree_longitude = data['items'][2]['position']['lng']

        hospitalFour = data['items'][3]['title']
        hospitalFour_address =  data['items'][3]['address']['label']
        hospitalFour_latitude = data['items'][3]['position']['lat']
        hospitalFour_longitude = data['items'][3]['position']['lng']

        hospitalFive = data['items'][4]['title']
        hospitalFive_address =  data['items'][4]['address']['label']
        hospitalFive_latitude = data['items'][4]['position']['lat']
        hospitalFive_longitude = data['items'][4]['position']['lng']

        hospitalSix = data['items'][5]['title']
        hospitalSix_address =  data['items'][5]['address']['label']
        hospitalSix_latitude = data['items'][5]['position']['lat']
        hospitalSix_longitude = data['items'][5]['position']['lng']

        hospitalSeven = data['items'][6]['title']
        hospitalSeven_address =  data['items'][6]['address']['label']
        hospitalSeven_latitude = data['items'][6]['position']['lat']
        hospitalSeven_longitude = data['items'][6]['position']['lng']

        hospitalEight = data['items'][7]['title']
        hospitalEight_address =  data['items'][7]['address']['label']
        hospitalEight_latitude = data['items'][7]['position']['lat']
        hospitalEight_longitude = data['items'][7]['position']['lng']
        return render_template('pharmacy1.html',latitude=latitude,
                longitude=longitude,
                apikey=api_key,
                oneName=hospitalOne,
                OneAddress=hospitalOne_address,
                oneLatitude=hospitalOne_latitude,
                oneLongitude=hospitalOne_longitude,
                twoName=hospitalTwo,
                twoAddress=hospitalTwo_address,
                twoLatitude=hospitalTwo_latitude,
                twoLongitude=hospitalTwo_longitude,
                threeName=hospitalThree,
                threeAddress=hospitalThree_address,
                threeLatitude=hospitalThree_latitude,
                threeLongitude=hospitalThree_longitude,
                fourName=hospitalFour,		
                fourAddress=hospitalFour_address,
                fourLatitude=hospitalFour_latitude,
                fourLongitude=hospitalFour_longitude,
                fiveName=hospitalFive,		
                fiveAddress=hospitalFive_address,
                fiveLatitude=hospitalFive_latitude,
                fiveLongitude=hospitalFive_longitude,
                sixName=hospitalSix,		
                sixAddress=hospitalSix_address,
                sixLatitude=hospitalSix_latitude,
                sixLongitude=hospitalSix_longitude,
                sevenName=hospitalSeven,		
                sevenAddress=hospitalSeven_address,
                sevenLatitude=hospitalSeven_latitude,
                sevenLongitude=hospitalSeven_longitude,
                eightName=hospitalEight,		
                eightAddress=hospitalEight_address,
                eightLatitude=hospitalEight_latitude,
                eightLongitude=hospitalEight_longitude)

if __name__ == '__main__':
	app.run(debug = True)
    

