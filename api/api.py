# write your web service here
from flask import Flask, request, jsonify
from simple_python import remove_null, reverse_substrings

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/clean_string', methods=['POST'])
def clean_string():
    """
    Cleans a raw string by removing null characters and reversing substrings.

    Returns:
        A JSON response containing the original raw string, the raw string without null characters,
        and the cleaned string with reversed substrings.
    """
    data = request.get_json()
    raw_string = data['raw_string']

    # First apply remove_null 
    raw_string_without = remove_null(raw_string)

    # Then apply reverse_substrings
    cleaned_string = reverse_substrings(raw_string_without)

    return jsonify({
        'raw_string': raw_string,
        'raw_string_without': raw_string_without,
        'cleaned_string': cleaned_string})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5001, debug=True)
