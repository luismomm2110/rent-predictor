import joblib
import json

model = joblib.load('trained_model.joblib')


def process_city(city):
    cities = {'city_Belo_Horizonte': 0,
              'city_Campinas': 0,
              'city_Porto_Alegre': 0,
              'city_Rio_de_Janeiro': 0,
              'city_Sao_Paulo': 0}
    if city == 'Belo Horizonte':
        cities['city_Belo_Horizonte'] = 1
    elif city == 'Campinas':
        cities['city_Campinas'] = 1
    elif city == 'Porto Alegre':
        cities['city_Porto_Alegre'] = 1
    elif city == 'Rio de Janeiro':
        cities['city_Rio_de_Janeiro'] = 1
    elif city == 'São Paulo':
        cities['city_Sao_Paulo'] = 1
    else:
        raise Exception('City not found')

    return cities


def process_categorical_value(param, param1, param2):
    if param == param1:
        return 1
    elif param == param2:
        return 0
    else:
        raise Exception('Invalid value')


def handler(event, context):
    # Parse the JSON event data
    data = json.dumps(event)
    data = json.loads(data)

    # Extract the required fields from the JSON data
    city = data['city']
    area = data['area']
    rooms = data['rooms']
    bathroom = data['bathroom']
    parking_spaces = data['parking spaces']
    animal = process_categorical_value(data['animal'], 'acept', 'not acept')
    furniture = process_categorical_value(data['furniture'], 'furnished', 'not furnished')
    hoa = data['hoa']
    property_tax = data['property tax']
    fire_insurance = data['fire insurance']

    # Process the city
    city_params = process_city(city)

    # Perform prediction using the loaded model
    try:
        input_data = [
            area,
            rooms,
            bathroom,
            parking_spaces,
            hoa,
            property_tax,
            fire_insurance,
            city_params['city_Belo_Horizonte'],
            city_params['city_Campinas'],
            city_params['city_Porto_Alegre'],
            city_params['city_Rio_de_Janeiro'],
            city_params['city_Sao_Paulo'],
            animal,
            furniture
        ]

        prediction = model.predict([input_data])
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

    # Prepare the response
    response = {'prediction': prediction.tolist()}

    # Return the response
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
