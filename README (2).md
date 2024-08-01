# JSON Transformer

```python
import json
import re
from datetime import datetime

def parse_value(value):
  if 'S' in value:
      return process_string(value['S'])
  elif 'N' in value:
      return process_number(value['N'])
  elif 'BOOL' in value:
      return process_boolean(value['BOOL'])
  elif 'NULL' in value:
      return process_null(value['NULL'])
  elif 'L' in value:
      return process_list(value['L'])
  elif 'M' in value:
      return process_map(value['M'])
  else:
      return None

def process_string(value):
  value = value.strip()
  if value == '':
      return None
  if re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', value):
      return int(datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").timestamp())
  return value

def convert_to_number(value):
  try:
    # Try to convert the string to an integer
    return int(value)
  except ValueError:
    try:
      # If it fails, try to convert the string to a float
      return float(value)
    except ValueError:
      # If both conversions fail, return the original string
      return None

def process_number(value):
  return convert_to_number(value.strip())

def process_boolean(value):
  value = value.strip().lower()
  if value in ['1', 't', 'true']:
      return True
  elif value in ['0', 'f', 'false']:
      return False
  return None

def process_null(value):
  value = value.strip().lower()
  if value in ['1', 't', 'true']:
      return None
  return None

def process_list(value):
  if not isinstance(value, list):
      return None
  result = []
  for item in value:
      parsed_item = parse_value(item)
      if parsed_item is not None:
          result.append(parsed_item)
  return result

def check_null(item):
  return 'NULL' in item or ' NULL' in item or 'NULL ' in item

def process_map(value):
  result = {}
  for key, item in sorted(value.items()):
      cleaned_key = key.strip()
      if cleaned_key == '':
          continue
      parsed_item = parse_value(item)
      print(cleaned_key, parsed_item, item)
      if parsed_item is not None or (check_null(item) and parsed_item is None):
          result[cleaned_key] = parsed_item
  return result

def transform_json(input_json):
  output = {}
  for key, item in input_json.items():
      cleaned_key = key.strip()
      if cleaned_key == '':
          continue
      parsed_item = parse_value(item)
      if parsed_item is not None or (check_null(item) and parsed_item is None):
          output[cleaned_key] = parsed_item

  return [output]

def main():
  with open('input.json', 'r') as file:
    input_json = json.load(file)
    output = transform_json(input_json)
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
```

Save above code in file `transform.py`

## Execution

- **Must** 
```
python transform.py
```

- **Must** not include any content from the **original** document.
- Provide any additional information that may be helpful to the reviewer.
