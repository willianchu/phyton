##############################################################################
#
# With XlsxWriter Python module 
# how to transpose Json to a xlsx file
#
import XlsxWriter

json_data = {
  "Actors": [
    {
      "name": "Tom Cruise",
      "age": 56,
      "Born At": "Syracuse, NY",
      "Birthdate": "July 3, 1962",
      "photo": "https://jsonformatter.org/img/tom-cruise.jpg",
      "wife": null,
      "weight": 67.5,
      "hasChildren": true,
      "hasGreyHair": false,
      "children": [
        "Suri",
        "Isabella Jane",
        "Connor"
      ]
    },
    {
      "name": "Robert Downey Jr.",
      "age": 53,
      "Born At": "New York City, NY",
      "Birthdate": "April 4, 1965",
      "photo": "https://jsonformatter.org/img/Robert-Downey-Jr.jpg",
      "wife": "Susan Downey",
      "weight": 77.1,
      "hasChildren": true,
      "hasGreyHair": false,
      "children": [
        "Indio Falconer",
        "Avri Roel",
        "Exton Elias"
      ]
    }
  ]
}

def json2xlsx(data):
  workbook = xlsxwriter.Workbook('destinationWorkSheet.xlsx') # first layer - File
  worksheet = workbook.add_worksheet() # Second layer - Worksheet
  print(data[0].keys())
  row = 0 
  column = 0

  

  # Add a bold format to use to highlight cells.
  bold = workbook.add_format({'bold': True})

  # Write some simple text.
  worksheet.write('A1', 'Hello')

  # Text with formatting.
  worksheet.write('A2', 'World')

  # Write some numbers, with row/column notation.
  worksheet.write(2, 0, 123)
  worksheet.write(3, 0, 123.456)


  workbook.close() # Save the file

json2xlsx(json_data)

