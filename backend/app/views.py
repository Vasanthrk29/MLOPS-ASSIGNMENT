from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class PredictView(APIView):
    def get(self, request):
        return Response({'message': 'All ok'}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get input values from the request data
        square_Meters = request.data.get('squareMeters')
        number_Of_Rooms = request.data.get('numberOfRooms')
        city_Part_Range = request.data.get('cityPartRange')
        num_Prev_Owners = request.data.get('numPrevOwners')

        # Check if any input value is missing
        if square_Meters is None or number_Of_Rooms is None or city_Part_Range is None or num_Prev_Owners is None:
            return Response({'error': 'One or more input values are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert input values to float
        try:
            square_Meters = float(square_Meters)
            number_Of_Rooms = float(number_Of_Rooms)
            city_Part_Range = float(city_Part_Range)
            num_Prev_Owners = float(num_Prev_Owners)
        except ValueError:
            return Response({'error': 'One or more input values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST)

        # Use LabelEncoder to encode categorical variables
        data = pd.read_csv("D:\\ParisHousing.csv")

        # Prepare input features
        x = data.iloc[:, [0,1,6,7]]
        y = data.iloc[:, [-1]]

        # Train a linear regression model
        rg = LinearRegression()
        rg.fit(x, y)

        # Predict the output based on input values
        out = rg.predict([[square_Meters, number_Of_Rooms, city_Part_Range, num_Prev_Owners]])

        # Process the output
        output = round(float(out[0]), 2)
        output_formatted = f'House price: {output}'

        # Allow requests from any origin (CORS)
        response = Response({'output': output_formatted}, status=status.HTTP_200_OK)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    def options(self, request, *args, **kwargs):
        # Allow CORS preflight requests
        response = Response()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
