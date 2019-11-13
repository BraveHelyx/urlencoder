# urlencoder.py
Performs a _full_ URL encoding of an input file or string. Outputs to stdout.

## Usage
```
python urlencoder.py -f <FILE>
python urlencoder.py -s <STRING>
```

## Usage Examples
#### Full String URL Encoding
```
python urlencoder.py -s "<script>alert(1)</script>"
%3c%73%63%72%69%70%74%3e%61%6c%65%72%74%28%31%29%3c%2f%73%63%72%69%70%74%3e
```

#### Full File URL Encoding
```
python urlencoder.py -f ./payloads.txt
%3c%69%6d%67%20%73%72%63%3d%78%20%6f%6e%65%72%72%6f%72%3d%22%6a%41%76%41%73%43%72%49%70%54%3a%61%6c%65%72%74%28%64%6f%63%75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%29%22%3e
%27%20%4f%52%20%27%31%27%3d%27%31%27%20%3b%20%2d%2d
```
