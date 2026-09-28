#  Watermark 
In this project I have tried to demonstrate how we can implement watermark in the 
text.

Scenario: For example I have an app which answers users query. I want to later confirm that this text belongs to my app or is generated through my app. The I can use this watermark system.

Methods:
In this mainly I have used 2  types of watermark techniques:
1. Zero Width Character: In this method we  encode a signature and embed it to the beginning and end of the text . Later check if that signature is still there or not.This signature is not displayed to user as it is encoded in zero width character and not visisble
2. Homoglyph Text: In this method we replace some charcters with homoglyph characters and the differrence in those characters are almost equal to zero. It is hard to separate from unicode characters.



## Setup

```bash
python3 -m pip install -r requirements.txt
export API_KEY="your-gemini-api-key"
python3 app.py
```

## Generate text

```bash
curl -X POST http://localhost:5000/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"prompt":"Who is Himal"}'
```

This response contain watermarked text.

 Output:

```json
{"prompt":"...","text":"...","watermarked":true}
```

## Detect a watermark

```bash
curl -X POST http://localhost:5000/api/detect \
  -H 'Content-Type: application/json' \
  -d '{"text":"This is watermarked text"}'
```
output:

```json
{"watermarked":true,"zero_width":true,"homoglyph":false}
```

## Health
Status of server. It donot check api key
`GET /api/health` returns `{"status":"ok"}` 
